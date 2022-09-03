from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from main_window import Ui_mainWindow


class MainWindow(QMainWindow, Ui_mainWindow):
    # 记录当前正在学习的章节
    nowChapter = 1
    # 记录是否已经开始当前章节的学习
    startLearnOrNot = False
    chapterNameList = ["第一章", "第二章", "第三章", "第四章", "第五章", "第六章", "第七章", "第八章", "第九章"]
    chapterBtnNameList = ["chapter_one", "chapter_two", "chapter_three", "chapter_four", "chapter_five", "chapter_six",
                          "chapter_seven", "chapter_eight", "chapter_nine"]

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 设置默认的窗口名(默认第一章)
        self.setWindowTitle(self.chapterNameList[0])

        # 设置默认当前章节的字体颜色为红色(默认第一章)
        self.chapter_one.setStyleSheet('''QPushButton{color:red}''')

        # 初始化禁用掉所有的上一页下一页按钮
        self.pre_steps_page.setEnabled(False)
        self.next_steps_page.setEnabled(False)
        self.pre_principle_page.setEnabled(False)
        self.next_principle_page.setEnabled(False)

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

        # 开始学习按钮的点击触发start_or_finish_learn_click事件
        self.start_or_finish_learn.clicked.connect(self.start_or_finish_learn_click)

    # 章节改变的事件
    def chapter_click(self, num):
        # 章节改变前去掉之前的字体颜色
        self.findChild(QPushButton, self.chapterBtnNameList[self.nowChapter - 1]).setStyleSheet(
            '''QPushButton{color:gray}''')
        self.nowChapter = num
        # 章节改变后变换字体颜色
        self.findChild(QPushButton, self.chapterBtnNameList[self.nowChapter - 1]).setStyleSheet(
            '''QPushButton{color:red}''')
        # 设置窗口的Title为当前章节名
        self.setWindowTitle(self.chapterNameList[num - 1])
        # 显示当前章节的实验原理
        self.principle_ppt.setText("现在正在放映第" + str(self.nowChapter) + "章节的实验原理ppt")
        # 显示当前章节的实验步骤
        self.steps_ppt.setText("现在正在放映第" + str(self.nowChapter) + "章节的实验步骤ppt")

    # 开始学习或结束学习按钮触发的事件
    def start_or_finish_learn_click(self):
        # 判断当前是否在学习并通过该状态调用不同函数
        if self.startLearnOrNot:
            self.startLearnOrNot = False
            self.start_or_finish_learn.setText("开始当前章节的学习")
            self.finish_learn()
        else:
            self.startLearnOrNot = True
            self.start_or_finish_learn.setText("结束当前章节的学习")
            self.start_learn()

    # 开始学习按钮的点击触发事件
    def start_learn(self):
        # 获取当前开始学习章节对应的PushButton对象
        btn = self.findChild(QPushButton, self.chapterBtnNameList[self.nowChapter - 1])
        # 禁用掉除当前章节的其他章节的PushButton
        for chapterBtnName in self.chapterBtnNameList:
            if chapterBtnName == btn.objectName():
                continue
            self.findChild(QPushButton, chapterBtnName).setEnabled(False)

        # 开放下一页按钮
        self.next_principle_page.setEnabled(True)
        self.next_steps_page.setEnabled(True)

    # 结束学习按钮的点击触发事件
    def finish_learn(self):
# TODO 这里需要设置一个确定是否结束学习的弹窗
        finish = True
        if finish:
            # 解禁章节按钮
            for chapterBtnName in self.chapterBtnNameList:
                self.findChild(QPushButton, chapterBtnName).setEnabled(True)
            # 禁用掉所有的上一页下一页按钮
            self.pre_steps_page.setEnabled(False)
            self.next_steps_page.setEnabled(False)
            self.pre_principle_page.setEnabled(False)
            self.next_principle_page.setEnabled(False)

