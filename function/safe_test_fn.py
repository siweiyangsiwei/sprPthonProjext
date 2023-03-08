import safe_test_questions as question
import random
from PyQt5 import QtWidgets


def show_test(self):
    question_num = random.randint(0,1200)
    str_test = question.str_test
    question_item = str_test[question_num]
    answer = question.answer[question_num]
    self.label_question.setText(question_item[0])
    self.answer_1.setText(question_item[1])
    self.answer_2.setText(question_item[2])
    self.answer_3.setText(question_item[3])
    self.answer_4.setText(question_item[4])
    # 查找正确的答案在哪个按钮
    answer_name = "answer_" + str(answer)
    self.answer_button = self.findChild(QtWidgets.QPushButton,answer_name)
    # self.answer_1.linkActivated.connect(lambda checked:answer_1_clicked(self,answer))
    # self.answer_2.linkActivated.connect(lambda checked:answer_2_clicked(self,answer))
    # self.answer_3.linkActivated.connect(lambda checked:answer_3_clicked(self,answer))
    # self.answer_4.linkActivated.connect(lambda checked:answer_4_clicked(self,answer))

    self.answer_1.clicked.connect(lambda checked:answer_1_clicked(self,answer))
    self.answer_2.clicked.connect(lambda checked:answer_2_clicked(self,answer))
    self.answer_3.clicked.connect(lambda checked:answer_3_clicked(self,answer))
    self.answer_4.clicked.connect(lambda checked:answer_4_clicked(self,answer))
    self.next_btn.clicked.connect(lambda checked: test_update(self))


def answer_1_clicked(self,answer):
    if answer == 1:
        # 答案正确则按钮变绿

        self.answer_1.setStyleSheet("background-color: rgb(65, 205, 82,150);")
    else:

        # 答案错误按钮变红，同时正确的答案变成绿色显示出来
        self.answer_1.setStyleSheet("background-color: rgb(223, 76, 76,160);")
        self.answer_button.setStyleSheet("background-color: rgb(65, 205, 82,150);")

def answer_2_clicked(self,answer):
    if answer == 2:
        self.answer_2.setStyleSheet("background-color: rgb(65, 205, 82,150);")
    else:
        self.answer_2.setStyleSheet("background-color: rgb(223, 76, 76,160);")
        self.answer_button.setStyleSheet("background-color: rgb(65, 205, 82,150);")


def answer_3_clicked(self,answer):
    if answer == 3:
        self.answer_3.setStyleSheet("background-color: rgb(65, 205, 82,150);")
    else:
        self.answer_3.setStyleSheet("background-color: rgb(223, 76, 76,160);")
        self.answer_button.setStyleSheet("background-color: rgb(65, 205, 82,150);")


def answer_4_clicked(self,answer):
    if answer == 4:
        self.answer_4.setStyleSheet("background-color: rgb(65, 205, 82,150);")
    else:
        self.answer_4.setStyleSheet("background-color: rgb(223, 76, 76,160);")
        self.answer_button.setStyleSheet("background-color: rgb(65, 205, 82,150);")

# 更新题目
def test_update(self):
    # 清除按钮颜色
    self.answer_1.setStyleSheet("background-color: rgb(225, 225, 225);")
    self.answer_2.setStyleSheet("background-color: rgb(225, 225, 225);")
    self.answer_3.setStyleSheet("background-color: rgb(225, 225, 225);")
    self.answer_4.setStyleSheet("background-color: rgb(225, 225, 225);")
    show_test(self)

