from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui
from view.main_window import Ui_MainWindow
from controllers.ExperimentWindow import ExperimentWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.run()

    def run(self):
        # 双击打开实验窗口
        self.treeWidget.itemDoubleClicked.connect(self.open_ExWin)
        # “实验选择”中根据文字数量自动调整第一列宽度
        self.treeWidget.resizeColumnToContents(0)
        # 用户头像
        self.label.setPixmap(QtGui.QPixmap("srpresources/user.png"))
        self.label.setScaledContents(True)

    def open_ExWin(self):
        # 获取选中的实验
        global selected_item
        selected_item = self.treeWidget.currentItem()
        # 实验所处行的索引,可用来查找实验文件
        global item_index
        item_index = self.treeWidget.currentIndex().row()
        experiment_window = ExperimentWindow()
        experiment_window.show()
        experiment_window.receive_main(self)
        self.close()

    def update_time(self, hour, min, sec):
        if self.treeWidget.currentItem().text(1) != '-':
            list = self.treeWidget.currentItem().text(1).split(':')
            hour = int(list[0]) + hour
            min = int(list[1]) + min
            sec = int(list[2]) + sec
            if sec >= 60:
                min += 1
                sec = sec - 60
                if min >= 60:
                    hour += 1
                    min = min - 60
            self.treeWidget.currentItem().setText(1, "{0}:{1}:{2}".format(str(int(hour)).rjust(2, '0')
                                                                          , str(int(min)).rjust(2, '0')
                                                                          , str(int(sec)).rjust(2, '0')))
        else:
            self.treeWidget.currentItem().setText(1, "{0}:{1}:{2}".format(str(int(hour)).rjust(2, '0')
                                                                          , str(int(min)).rjust(2, '0')
                                                                          , str(int(sec)).rjust(2, '0')))
        # 将时间相加
        hours = 0
        mins = 0
        secs = 0
        for i in range(3):
            time = self.treeWidget.topLevelItem(i).text(1)