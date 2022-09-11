import os.path

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton
from main_window import Ui_mainWindow

import SqlTools


class MainWindow(QMainWindow, Ui_mainWindow):
    # 记录当前正在学习的章节
    nowChapter = 1

    # 记录是否已经开始当前章节的学习
    startLearnOrNot = False

    # 记录当前显示的实验原理的图片
    nowPrincipleImg = 1

    # 记录当前显示的实验步骤的图片
    nowStepImg = 1

    # 记录当前正在回答的题目
    nowTestQuestion = 1

    # 保存当前章节的所有test题目
    questionList = []

    # 记录是否结束了测试
    answerList = []

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
        self.pre_test_question.setEnabled(False)
        self.next_test_question.setEnabled(False)

        # 初始化禁用test部分的答题框
        self.answer.setEnabled(False)

        # 设置默认的实验原理和实验步骤的图片(默认第一张)
        self.set_principle_img(1)
        self.set_steps_img(1)

        # 获取本章的test题目
        self.get_test_question()

        # 设置默认的测试的题目(默认本章第一题)
        self.set_test_question()

        # 将所有test模块中的label设置为自动换行
        self.qustion.setWordWrap(True)
        self.section_A.setWordWrap(True)
        self.section_B.setWordWrap(True)
        self.section_C.setWordWrap(True)
        self.section_D.setWordWrap(True)

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

        # 点击实验原理下一页按钮触发next_principle_page_click事件
        self.next_principle_page.clicked.connect(self.next_principle_page_click)

        # 点击实验原理上一页按钮触发pre_principle_page_click事件
        self.pre_principle_page.clicked.connect(self.pre_principle_page_click)

        # 点击实验步骤下一页按钮触发next_steps_page_click事件
        self.next_steps_page.clicked.connect(self.next_steps_page_click)

        # 点击实验步骤上一页按钮触发pre_steps_page_click事件
        self.pre_steps_page.clicked.connect(self.pre_steps_page_click)

        # 点击test部分下一题触发next_test_question_click事件
        self.next_test_question.clicked.connect(self.next_test_question_click)

        # 点击test部分上一题触发pre_test_question_click事件
        self.pre_test_question.clicked.connect(self.pre_test_question_click)

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

        # 章节改变将当前实验原理和实验步骤图片恢复为1
        self.nowPrincipleImg = 1
        self.nowStepImg = 1

        # 显示当前章节的实验原理(默认只显示当前章节的第一张)
        self.set_principle_img(1)
        # 显示当前章节的实验步骤(默认只显示当前章节的第一张)
        self.set_steps_img(1)
        # 显示当前章节的test部分的题目(默认值显示当前章节的第一题)
        self.nowTestQuestion = 1
        self.get_test_question()
        self.set_test_question()
        # 清空test输入框的内容
        self.answer.setText("")
        # 清空回答
        self.answerList = []

    # 开始学习或结束学习按钮触发的事件
    def start_or_finish_learn_click(self):
        self.findChild(QPushButton, self.chapterBtnNameList[self.nowChapter - 1]).setEnabled(False)
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
        self.next_test_question.setEnabled(True)
        # 清空test部分的答题框
        self.answer.setText("")
        # 开放test部分的答题框
        self.answer.setEnabled(True)
        # 默认获取焦点
        self.answer.setFocus()
        self.nowTestQuestion = 1
        # 恢复下一题按钮的文字
        self.next_test_question.setText("下一题")

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
            self.pre_test_question.setEnabled(False)
            self.next_test_question.setEnabled(False)
            # 禁用掉test部分的答题框
            self.answer.setEnabled(False)

    # 设置实验原理图片的函数
    def set_principle_img(self, index):
        self.principle_img.setText("")
        img = os.path.abspath(
            ('resources/Image/principle/chapter' + str(self.nowChapter) + '/principle' + str(index) + '.jpg'))
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        self.principle_img.setScaledContents(True)
        self.principle_img.setPixmap(image)

    # 设置实验步骤的函数
    def set_steps_img(self, index):
        self.steps_img.setText("")
        img = os.path.abspath(
            ('resources/Image/steps/chapter' + str(self.nowChapter) + '/step' + str(index) + '.jpg'))
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        self.steps_img.setScaledContents(True)
        self.steps_img.setPixmap(image)

    # 点击实验原理的下一页触发的事件
    def next_principle_page_click(self):
        # 当前页+1
        self.nowPrincipleImg += 1
        # 上一页按钮可用
        self.pre_principle_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_principle_img(self.nowPrincipleImg)
        # 判断是否为最后一页
        principle_img_num = os.listdir('resources/Image/principle/chapter' + str(self.nowChapter))
        if self.nowPrincipleImg >= len(principle_img_num):
            self.next_principle_page.setEnabled(False)

    # 点击实验原理的上一页触发的事件
    def pre_principle_page_click(self):
        # 当前页-1
        self.nowPrincipleImg -= 1
        # 下一页按钮可用
        self.next_principle_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_principle_img(self.nowPrincipleImg)
        # 判断是否为第一页
        if self.nowPrincipleImg <= 1:
            self.pre_principle_page.setEnabled(False)

    # 点击实验步骤的下一页触发的事件(实现同实验原理)
    def next_steps_page_click(self):
        self.nowStepImg += 1
        self.pre_steps_page.setEnabled(True)
        self.set_steps_img(self.nowStepImg)
        steps_img_num = os.listdir('resources/Image/steps/chapter' + str(self.nowChapter))
        if self.nowStepImg >= len(steps_img_num):
            self.next_steps_page.setEnabled(False)

    # 点击实验的步骤上一页触发的事件(实现同实验原理)
    def pre_steps_page_click(self):
        self.nowStepImg -= 1
        self.next_steps_page.setEnabled(True)
        self.set_steps_img(self.nowStepImg)
        if self.nowStepImg <= 1:
            self.pre_steps_page.setEnabled(False)

    # 点击test部分下一题触发的事件
    def next_test_question_click(self):
        # 判断是否已经填入答案
        if self.answer.text() == "":
            print("请先填写答案再进入下一题")
            return
        # 判断是否为结束测试按钮
        if self.nowTestQuestion >= len(self.questionList):
            # 将答案保存到answerList中
            self.answerList.append(self.answer.text().upper())
            # 调用答题结束的函数
            self.finish_test()
            # 禁用上一题和下一题按钮
            self.next_test_question.setEnabled(False)
            self.pre_test_question.setEnabled(False)
        else:
            # 保存答案(先判断该题是否填过,填过则更新答案,没填过则加入)
            if self.nowTestQuestion > len(self.answerList):
                self.answerList.append(self.answer.text().upper())
            else:
                self.answerList[self.nowTestQuestion - 1] = self.answer.text().upper()
            self.nowTestQuestion += 1
            # 判断是否已经填过答案
            if self.nowTestQuestion <= len(self.answerList):
                self.answer.setText(self.answerList[self.nowTestQuestion - 1])
            else:
                # 清空输入框
                self.answer.setText("")
            # 输入框自动获取焦点
            self.answer.setFocus()
            self.pre_test_question.setEnabled(True)
            self.set_test_question()
            # 判断是否为最后一题
            if self.nowTestQuestion >= len(self.questionList):
                self.next_test_question.setText("结束测试")

    # 点击test部分上一题触发的事件
    def pre_test_question_click(self):
        self.nowTestQuestion -= 1
        self.next_test_question.setEnabled(True)
        self.set_test_question()
        # 点击了上一题那么上一题一定填入了答案,需要取出对应答案并填入输入框中
        self.answer.setText(self.answerList[self.nowTestQuestion - 1])
        # 判断是否为第一题
        if self.nowTestQuestion <= 1:
            self.pre_test_question.setEnabled(False)
            self.next_test_question.setText("下一题")

    # 获取test部分的题目
    def get_test_question(self):
        self.questionList = SqlTools.get_question_by_chapter(self.chapterBtnNameList[self.nowChapter - 1])

    # 设置test部分的题目
    def set_test_question(self):
        question = self.questionList[self.nowTestQuestion - 1]
        section_a = ""
        section_b = ""
        section_c = ""
        section_d = ""
        if question[3] != "":
            section_a = "A." + question[3]
            section_b = "B." + question[4]
            section_c = "C." + question[5]
            section_d = "D." + question[6]
        self.qustion.setText(question[1])
        self.section_A.setText(section_a)
        self.section_B.setText(section_b)
        self.section_C.setText(section_c)
        self.section_D.setText(section_d)

    # 答题结束的函数
    def finish_test(self):
        print("你的答案是: " + str(self.answerList))
        print("正确答案是: " + str(SqlTools.get_correct_answer_by_chapter(self.chapterBtnNameList[self.nowChapter - 1])))
        print("答题结束")
