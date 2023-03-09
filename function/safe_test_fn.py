from PyQt5.QtWidgets import QTableWidgetItem

import safe_test_questions as question
import random
from PyQt5 import QtWidgets


def show_test(self):
    # 获取选择的题数
    self.test_num = int(self.comboBox.currentText())
    # 从题库随机抽取
    question_num = random.randint(0,1199)
    # 获取题目
    str_test = question.str_test
    # 获取下标为question_num的题目和答案
    question_item = str_test[question_num]
    self.answer = question.answer[question_num]
    # 显示题目
    self.label_question.setText(str(self.now_num) + "、" +" "+ question_item[0])
    self.answer_1.setText("A"+question_item[1])
    self.answer_2.setText("B"+question_item[2])
    self.answer_3.setText("C"+question_item[3])
    self.answer_4.setText("D"+question_item[4])
    # 查找正确的答案在哪个按钮
    answer_name = "answer_" + str(self.answer)
    self.answer_button = self.findChild(QtWidgets.QPushButton,answer_name)
    # self.answer_1.linkActivated.connect(lambda checked:answer_1_clicked(self,answer))
    # self.answer_2.linkActivated.connect(lambda checked:answer_2_clicked(self,answer))
    # self.answer_3.linkActivated.connect(lambda checked:answer_3_clicked(self,answer))
    # self.answer_4.linkActivated.connect(lambda checked:answer_4_clicked(self,answer))

    

def answer_1_clicked(self):
    if self.answer == 1:
        # 答案正确则按钮变绿
        self.answer_1.setStyleSheet("background-color: rgb(65, 205, 82,150);text-align:left")
        # 记录已答正确题数
        self.correct_num += 1
    else:
        # 答案错误按钮变红，同时正确的答案变成绿色显示出来
        self.answer_1.setStyleSheet("background-color: rgb(223, 76, 76,160);text-align:left")
        self.answer_button.setStyleSheet("background-color: rgb(65, 205, 82,150);text-align:left")

    # 选择完答案之后禁用按钮
    self.answer_1.setEnabled(False)
    self.answer_2.setEnabled(False)
    self.answer_3.setEnabled(False)
    self.answer_4.setEnabled(False)

def answer_2_clicked(self):
    if self.answer == 2:
        self.answer_2.setStyleSheet("background-color: rgb(65, 205, 82,150);text-align:left")
        self.correct_num += 1
    else:
        self.answer_2.setStyleSheet("background-color: rgb(223, 76, 76,160);text-align:left")
        self.answer_button.setStyleSheet("background-color: rgb(65, 205, 82,150);text-align:left")
    # 选择完答案之后禁用按钮
    self.answer_1.setEnabled(False)
    self.answer_2.setEnabled(False)
    self.answer_3.setEnabled(False)
    self.answer_4.setEnabled(False)

def answer_3_clicked(self):
    if self.answer == 3:
        self.answer_3.setStyleSheet("background-color: rgb(65, 205, 82,150);text-align:left")
        self.correct_num += 1
    else:
        self.answer_3.setStyleSheet("background-color: rgb(223, 76, 76,160);text-align:left")
        self.answer_button.setStyleSheet("background-color: rgb(65, 205, 82,150);text-align:left")
    # 选择完答案之后禁用按钮
    self.answer_1.setEnabled(False)
    self.answer_2.setEnabled(False)
    self.answer_3.setEnabled(False)
    self.answer_4.setEnabled(False)
def answer_4_clicked(self):
    if self.answer == 4:
        self.answer_4.setStyleSheet("background-color: rgb(65, 205, 82,150);text-align:left")
        self.correct_num += 1
    else:
        self.answer_4.setStyleSheet("background-color: rgb(223, 76, 76,160);text-align:left")
        self.answer_button.setStyleSheet("background-color: rgb(65, 205, 82,150);text-align:left")#   选择完答案之后禁用按钮
    self.answer_1.setEnabled(False)
    self.answer_2.setEnabled(False)
    self.answer_3.setEnabled(False)
    self.answer_4.setEnabled(False)
# 更新题目
def test_update(self):
    self.now_num += 1
    if(self.test_num == self.now_num):
        self.next_btn.setText("结束测试")
    if(self.test_num == (self.now_num-1)):
        self.stackedWidget.setCurrentIndex(2)
        test_end(self)
    else:
        # 清除按钮颜色
        self.answer_1.setStyleSheet("background-color: rgb(225, 225, 225);text-align:left")
        self.answer_2.setStyleSheet("background-color: rgb(225, 225, 225);text-align:left")
        self.answer_3.setStyleSheet("background-color: rgb(225, 225, 225);text-align:left")
        self.answer_4.setStyleSheet("background-color: rgb(225, 225, 225);text-align:left")
        # 恢复按钮可使用
        self.answer_1.setEnabled(True)
        self.answer_2.setEnabled(True)
        self.answer_3.setEnabled(True)
        self.answer_4.setEnabled(True)
        show_test(self)


# 答题结束
def test_end(self):
    self.label_total_num.setText(str(self.test_num))
    self.label_correct_num.setText(str(self.correct_num))
    self.correct_rate = self.correct_num/self.test_num * 100
    self.label_correct_rate.setText(str(self.correct_rate) + "%")
    add_result(self)

# 在“我的”表格中添加测试结果
def add_result(self):
   num = self.table_result.rowCount()
   self.table_result.setRowCount(num+1)
   self.table_result.setItem(num, 0, QTableWidgetItem(str(self.test_num)))
   self.table_result.setItem(num, 1, QTableWidgetItem(str(self.correct_num)))
   self.table_result.setItem(num, 2, QTableWidgetItem(str(self.correct_rate)+"%"))



