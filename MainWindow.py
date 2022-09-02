from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_mainWindow


class MainWindow(QMainWindow, Ui_mainWindow):
    chapter = 1
    chapterNameList = ["第一章", "第二章", "第三章", "第四章", "第五章", "第六章", "第七章", "第八章", "第九章"]

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 章节的点击触发改变章节事件
        self.chapter_one.clicked.connect(lambda: self.chapter_click(1))
        self.chapter_two.clicked.connect(lambda: self.chapter_click(2))
        self.chapter_three.clicked.connect(lambda: self.chapter_click(3))
        self.chapter_four.clicked.connect(lambda: self.chapter_click(4))
        self.chapter_five.clicked.connect(lambda: self.chapter_click(5))
        self.chapter_six.clicked.connect(lambda: self.chapter_click(6))
        self.chapter_seven.clicked.connect(lambda: self.chapter_click(7))
        self.chapter_eight.clicked.connect(lambda: self.chapter_click(8))
        self.chapter_nine.clicked.connect(lambda: self.chapter_click(9))

        # 设置默认的窗口名(默认第一章)
        self.setWindowTitle(self.chapterNameList[0])

    # 章节改变的事件
    def chapter_click(self, num):
        self.chapter = num
        self.setWindowTitle(self.chapterNameList[num - 1])
        # 显示当前章节的实验原理
        self.principle_ppt.setText("现在正在放映第" + str(self.chapter) + "章节的实验原理ppt")
        # 显示当前章节的实验步骤
        self.steps_ppt.setText("现在正在放映第" + str(self.chapter) + "章节的实验步骤ppt")
