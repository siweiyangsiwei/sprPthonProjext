from PyQt5.QtWidgets import QMainWindow
from view.main_window import Ui_MainWindow
from controllers.ExperimentWindow import ExperimentWindow
from function import safe_test_fn
from tools import SqlTools

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.run()
        safe_test_fn.show_test(self)
        self.user_list = SqlTools.get_user("admin")[0]
        print(self.user_list)
        self.label_id.setText(self.user_list[0])
        self.sec_list = []
        for i in range(0,9):
            self.sec_list.append(self.user_list[i+3])
        # 总时间
        self.sec_list.append(self.user_list[2])
        self.update_time()

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
        # self.close()

    # def update_time(self, hour, min, sec):
    #     if self.treeWidget.currentItem().text(1) != None:
    #         list = self.treeWidget.currentItem().text(1).split(':')
    #         hour = int(list[0]) + hour
    #         min = int(list[1]) + min
    #         sec = int(list[2]) + sec
    #         if sec >= 60:
    #             min += 1
    #             sec = sec - 60
    #             if min >= 60:
    #                 hour += 1
    #                 min = min - 60
    #         self.treeWidget.currentItem().setText(1, "{0}:{1}:{2}".format(str(int(hour)).rjust(2, '0')
    #                                                                       , str(int(min)).rjust(2, '0')
    #                                                                       , str(int(sec)).rjust(2, '0')))
    #     else:
    #         self.treeWidget.currentItem().setText(1, "{0}:{1}:{2}".format(str(int(hour)).rjust(2, '0')
    #                                                                       , str(int(min)).rjust(2, '0')
    #                                                                       , str(int(sec)).rjust(2, '0')))
    #     # 将时间相加
    #     hours = 0
    #     mins = 0
    #     secs = 0
    #     for i in range(3):
    #         time = self.treeWidget.topLevelItem(i).text(1)

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
