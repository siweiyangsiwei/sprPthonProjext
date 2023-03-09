from PyQt5.QtWidgets import QMainWindow
from view.main_window import Ui_MainWindow
from controllers.ExperimentWindow import ExperimentWindow
from function import safe_test_fn
from tools import SqlTools
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.run()
        # 文字居中
        self.label_safe.setAlignment(Qt.AlignCenter)
        self.label_end.setAlignment(Qt.AlignCenter)
        self.user_list = SqlTools.get_user("admin")[0]
        print(self.user_list)
        self.label_id.setText(self.user_list[0])
        self.sec_list = []
        for i in range(0,9):
            self.sec_list.append(self.user_list[i+3])
        # 总时间
        self.sec_list.append(self.user_list[2])
        self.update_time()
        # 开始答题按钮
        self.start_btn.clicked.connect(self.start_safe_test)
        # 下一题按钮
        self.next_btn.clicked.connect(lambda: safe_test_fn.test_update(self))
        # 返回按钮
        self.back_btn.clicked.connect(self.show_initial)
        # 设置初始页面
        self.stackedWidget.setCurrentIndex(0)
        
        self.answer_1.clicked.connect(lambda: safe_test_fn.answer_1_clicked(self))
        self.answer_2.clicked.connect(lambda: safe_test_fn.answer_2_clicked(self))
        self.answer_3.clicked.connect(lambda: safe_test_fn.answer_3_clicked(self))
        self.answer_4.clicked.connect(lambda: safe_test_fn.answer_4_clicked(self))

    def run(self):
        # 双击打开实验窗口
        self.treeWidget.itemDoubleClicked.connect(self.open_ExpWin)
        # “实验选择”中根据文字数量自动调整第一列宽度
        self.treeWidget.resizeColumnToContents(0)
        # 用户头像
        # self.label.setPixmap(QtGui.QPixmap("srpresources/user.png"))
        # self.label.setScaledContents(True)

    def open_ExpWin(self):
        # 实验所处行的索引,可用来查找实验文件
        self.item_index = self.treeWidget.currentIndex().row()
        self.exp_window = ExperimentWindow()
        self.exp_window.show()
        # 这里去调用一下exp_window的start_learn()方法,进行实验内容的初始化
        self.exp_window.start_learn()
        # 调用一下chapter_click(self, num)方法进行章节的初始化,其中num为当前章节的索引,从1开始
        self.exp_window.chapter_click(self.item_index + 1)
        self.exp_window.receive_main(self)

    def update_time(self):
        total_sec = 0
        total_min = 0
        total_hour = 0
        # 储存时分秒形式的时间的序列
        for i in range(0,9):
            hour = 0
            min = 0
            # 按实验顺序取出秒数(第一个实验的秒数从3开始）
            sec = self.sec_list[i]
            if(sec != None):
                total_sec += sec
                if sec >= 60:
                    min += sec//60
                    sec = sec%60
                    if min >= 60:
                        hour += min//60
                        min = min%60
                time_i = "{0}:{1}:{2}".format(str(int(hour)).rjust(2, '0'), str(int(min)).rjust(2, '0'),
                                     str(int(sec)).rjust(2, '0'))
                # 在表格上显示时间
                self.treeWidget.topLevelItem(i).setText(1, time_i)
            else:
                pass

        # 存入总时间（秒数）
        self.sec_list[-1] = total_sec
        # 显示总时间
        if total_sec >= 60:
            total_min += total_sec // 60
            total_sec = total_sec % 60
            if total_min >= 60:
                total_hour += total_min // 60
                total_min = total_min % 60
        # 时分秒形式的总时间
        total_time = "{0}:{1}:{2}".format(str(int(total_hour)).rjust(2, '0'), str(int(total_min)).rjust(2, '0'),
                                     str(int(total_sec)).rjust(2, '0'))
        self.label_time.setText("学习总时长："+total_time)


    # 原本时间加上实验时间
    def receive_time(self,sec):
        if(self.sec_list[self.item_index] != None):
            self.sec_list[self.item_index] = self.sec_list[self.item_index] + sec
        else:
            self.sec_list[self.item_index] = sec
        self.update_time()

    # 更新数据库
    def update_data(self):
        SqlTools.update_user(self.sec_list)

    # 关闭程序时更新数据库
    def closeEvent(self, event):
        self.update_data()

    # 实验安全
    def start_safe_test(self):
        self.stackedWidget.setCurrentIndex(1)
        # 答对题数
        self.correct_num = 0
        # 记录答题数
        self.now_num = 1
        safe_test_fn.show_test(self)

    # 显示实验安全初始页面
    def show_initial(self):
        self.stackedWidget.setCurrentIndex(0)
        self.next_btn.setText("下一题")
