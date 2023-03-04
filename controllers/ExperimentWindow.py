import os.path
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from view.experiment import Ui_ExperimentWindow
from controllers.EmailWindow import EmailWindow
from controllers.Simulation import Simulation
from tools import SqlTools
from function import data_processing
import function.report_1
import calculate.exp_1
import calculate.exp_2
import calculate.exp_3

class ExperimentWindow(QMainWindow, Ui_ExperimentWindow):
    # 记录当前正在学习的章节
    nowChapter = 1

    # 记录是否已经开始当前章节的学习
    startLearnOrNot = False

    # 记录当前显示的实验目的的图片
    nowPurposeImg = 1
    # 记录当前显示的实验任务的图片
    nowTaskImg = 1
    # 记录当前显示的实验原理的图片
    nowPrincipleImg = 1
    # 记录当前显示的实验装置的图片
    nowEquipmentImg = 1
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
        super(ExperimentWindow, self).__init__()
        self.setupUi(self)

        # 根据分辨率设置窗口大小
        desktop = QApplication.desktop()
        width = desktop.width()
        # 屏幕比不同而采用固定的窗口比例，窗口宽高之比会变化，看起来不美观
        # 所以得知道窗口宽高比例、窗口宽高占屏幕宽高比例
        # 先设置窗口占据屏幕的大小，求出宽，高用窗口比例得出
        # 窗口宽高比，这里设置 1.3（适应图片）
        window_ratio = 1.3
        # 窗口宽占据屏幕的多少
        window_cover = 0.6
        # 求出窗口宽高
        resize_width = width * window_cover
        resize_height = resize_width / window_ratio
        # 设置窗口大小
        self.resize(resize_width, resize_height)
        # 表格设置
        self.table_style()

        self.pre_test_question.setEnabled(False)
        self.pre_purpose_page.setEnabled(False)
        self.pre_tasks_page.setEnabled(False)
        self.pre_steps_page.setEnabled(False)
        self.pre_principle_page.setEnabled(False)
        self.pre_equipment_page.setEnabled(False)

        # 将所有test模块中的label设置为自动换行
        self.question.setWordWrap(True)
        self.section_A.setWordWrap(True)
        self.section_B.setWordWrap(True)
        self.section_C.setWordWrap(True)
        self.section_D.setWordWrap(True)

        # 点击实验目的下一页按钮触发next_purpose_page_click事件
        self.next_purpose_page.clicked.connect(self.next_purpose_page_click)

        # 点击实验目的上一页按钮触发pre_purpose_page_click事件
        self.pre_purpose_page.clicked.connect(self.pre_purpose_page_click)

        # 点击实验任务下一页按钮触发next_tasks_page_click事件
        self.next_tasks_page.clicked.connect(self.next_tasks_page_click)

        # 点击实验任务上一页按钮触发pre_tasks_page_click事件
        self.pre_tasks_page.clicked.connect(self.pre_tasks_page_click)

        # 点击实验原理下一页按钮触发next_principle_page_click事件
        self.next_principle_page.clicked.connect(self.next_principle_page_click)

        # 点击实验原理上一页按钮触发pre_principle_page_click事件
        self.pre_principle_page.clicked.connect(self.pre_principle_page_click)

        # 点击实验装置下一页按钮触发next_equipment_page_click事件
        self.next_equipment_page.clicked.connect(self.next_equipment_page_click)

        # 点击实验装置上一页按钮触发pre_equipment_page_click事件
        self.pre_equipment_page.clicked.connect(self.pre_equipment_page_click)

        # 点击实验步骤下一页按钮触发next_steps_page_click事件
        self.next_steps_page.clicked.connect(self.next_steps_page_click)

        # 点击实验步骤上一页按钮触发pre_steps_page_click事件
        self.pre_steps_page.clicked.connect(self.pre_steps_page_click)

        # 点击test部分下一题触发next_test_question_click事件
        self.next_test_question.clicked.connect(self.next_test_question_click)

        # 点击test部分上一题触发pre_test_question_click事件
        self.pre_test_question.clicked.connect(self.pre_test_question_click)

        self.amination_in.clicked.connect(self.amination_in_click)


        self.shutdown.clicked.connect(lambda: self.close())
        self.mini.clicked.connect(lambda: self.showMinimized())
        self.back.clicked.connect(self.back_main)
        self.send_email.clicked.connect(self.open_emailWindow)

        # 生成所在章节的实验报告
        self.exp_report.clicked.connect(self.select_report)

        # 计算按键触发事件
        self.calculate_1.clicked.connect(lambda: calculate.exp_1.calculate_data1(self))
        self.calculate_2.clicked.connect(lambda: calculate.exp_2.calculate_data2(self))
        self.calculate_3a.clicked.connect(lambda: calculate.exp_3.calculate_data_3a(self))
        self.calculate_3b.clicked.connect(lambda: calculate.exp_3.calculate_data_3b(self))
        self.calculate_3c.clicked.connect(lambda: calculate.exp_3.calculate_data_3c(self))

        # 作图按键触发事件
        self.get_pic_3a.clicked.connect(lambda: calculate.exp_3.get_pic_3a(self))

        # 重置数据
        self.reset_1.clicked.connect(lambda: calculate.exp_1.reset_pic(self))
        self.reset_2.clicked.connect(lambda: calculate.exp_2.reset_pic(self))
        self.reset_3a.clicked.connect(lambda: calculate.exp_3.reset_pic_3a(self))
        self.reset_3b.clicked.connect(lambda: calculate.exp_3.reset_pic_3b(self))
        self.reset_3c.clicked.connect(lambda: calculate.exp_3.reset_pic_3c(self))

        # 第五章数据处理第一个表格的设计
        self.data_processing_5_table_1.setSpan(0, 0, 10, 1)
        self.data_processing_5_table_1.setSpan(10, 0, 10, 1)
        self.data_processing_5_table_1.setSpan(20, 0, 10, 1)

        # 第五章数据处理第二个表格设计
        self.data_processing_5_table_2.setSpan(0, 0, 10, 1)
        self.data_processing_5_table_2.setSpan(10, 0, 10, 1)
        self.data_processing_5_table_2.setSpan(20, 0, 10, 1)
        self.data_processing_5_table_2.setSpan(0, 4, 10, 1)
        self.data_processing_5_table_2.setSpan(10, 4, 10, 1)
        self.data_processing_5_table_2.setSpan(20, 4, 10, 1)
        self.data_processing_5_table_2.setSpan(0, 5, 10, 1)
        self.data_processing_5_table_2.setSpan(10, 5, 10, 1)
        self.data_processing_5_table_2.setSpan(20, 5, 10, 1)
        self.data_processing_5_table_2.setSpan(0, 6, 10, 1)
        self.data_processing_5_table_2.setSpan(10, 6, 10, 1)
        self.data_processing_5_table_2.setSpan(20, 6, 10, 1)
        self.data_processing_5_table_2.setSpan(0, 7, 10, 1)
        self.data_processing_5_table_2.setSpan(10, 7, 10, 1)
        self.data_processing_5_table_2.setSpan(20, 7, 10, 1)

        # 第五章实验数据开始处理触发的事件
        self.data_processing_5_date_calculate.clicked.connect(self.data_processing_5_date_calculate_click)

        # 第七章实验数据开始处理触发的事件
        self.data_processing_7_data_calculate.clicked.connect(self.data_processing_7_data_calculate_click)

    # 章节改变的事件
    def chapter_click(self, num):

        self.nowChapter = num
        print(self.nowChapter)
        # 设置窗口的Title为当前章节名
        self.setWindowTitle(self.chapterNameList[num - 1])

        # 章节改变将各个部分的图片恢复为1
        self.nowPurposeImg = 1
        self.nowTaskImg = 1
        self.nowPrincipleImg = 1
        self.nowEquipmentImg = 1
        self.nowStepImg = 1

        # 显示当前章节的实验目的(默认只显示当前章节的第一张)
        self.set_purpose_img(1)
        # 显示当前章节的实验任务(默认只显示当前章节的第一张)
        self.set_tasks_img(1)
        # 显示当前章节的实验原理(默认只显示当前章节的第一张)
        self.set_principle_img(1)
        # 显示当前章节的实验装置(默认只显示当前章节的第一张)
        self.set_equipment_img(1)
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

        # 初始化章节对应的数据处理页面
        self.calculate_stackWiget.setCurrentIndex(self.nowChapter-1)



        # 将实验数据处理的页面调整到当前的实验页面
        # self.stackedWidget_2.setCurrentIndex(self.nowChapter - 1)

    # 开始学习按钮的点击触发事件
    def start_learn(self):
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

    # 设置实目的图片的函数
    def set_purpose_img(self, index):
        self.principle_img.setText("")
        img = os.path.abspath(
            ('resources/Image/purpose/chapter' + str(self.nowChapter) + '/purpose' + str(index) + '.png'))
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        self.purpose_img.setScaledContents(True)
        self.purpose_img.setPixmap(image)
        # 页数为1时禁用下一页
        total_img_num = len(os.listdir('resources/Image/purpose/chapter' + str(self.nowChapter)))
        if total_img_num == 1:
            self.next_purpose_page.setEnabled(False)

    # 设置实验任务图片的函数
    def set_tasks_img(self, index):
        self.tasks_img.setText("")
        img = os.path.abspath(
            ('resources/Image/tasks/chapter' + str(self.nowChapter) + '/task' + str(index) + '.png'))
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        image = QtGui.QPixmap(img)
        self.tasks_img.setScaledContents(True)
        self.tasks_img.setPixmap(image)
        # 总页数为1时禁用下一页
        total_img_num = len(os.listdir('resources/Image/tasks/chapter' + str(self.nowChapter)))
        if total_img_num == 1:
            self.next_tasks_page.setEnabled(False)

    # 设置实验原理图片的函数
    def set_principle_img(self, index):
        self.principle_img.setText("")
        img = os.path.abspath(
            ('resources/Image/principle/chapter' + str(self.nowChapter) + '/principle' + str(index) + '.png'))
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        self.principle_img.setScaledContents(True)
        self.principle_img.setPixmap(image)
        # 总页数为1时禁用下一页
        total_img_num = len(os.listdir('resources/Image/principle/chapter' + str(self.nowChapter)))
        if total_img_num == 1:
            self.next_principle_page.setEnabled(False)

    # 设置实验装置图片的函数
    def set_equipment_img(self, index):
        self.equipment_img.setText("")
        img = os.path.abspath(
            ('resources/Image/equipment/chapter' + str(self.nowChapter) + '/equipment' + str(index) + '.png'))
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        self.equipment_img.setScaledContents(True)
        self.equipment_img.setPixmap(image)
        # 总页数为1时禁用下一页
        total_img_num = len(os.listdir('resources/Image/equipment/chapter' + str(self.nowChapter)))
        if total_img_num == 1:
            self.next_equipment_page.setEnabled(False)

    # 设置实验步骤的函数
    def set_steps_img(self, index):
        self.steps_img.setText("")
        img = os.path.abspath(
            ('resources/Image/steps/chapter' + str(self.nowChapter) + '/step' + str(index) + '.png'))
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        self.steps_img.setScaledContents(True)
        self.steps_img.setPixmap(image)
        # 总页数为1时禁用下一页
        total_img_num = len(os.listdir('resources/Image/steps/chapter' + str(self.nowChapter)))
        if total_img_num == 1:
            self.next_steps_page.setEnabled(False)

    # 点击实验目的的下一页触发的事件
    def next_purpose_page_click(self):
        # 当前页+1
        self.nowPurposeImg += 1
        # 上一页按钮可用
        self.pre_purpose_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_purpose_img(self.nowPurposeImg)
        # 判断是否为最后一页
        purpose_img_num = os.listdir('resources/Image/purpose/chapter' + str(self.nowChapter))
        if self.nowPurposeImg >= len(purpose_img_num):
            self.next_purpose_page.setEnabled(False)

    # 点击实验目的的上一页触发的事件
    def pre_purpose_page_click(self):
        # 当前页-1
        self.nowPurposeImg -= 1
        # 下一页按钮可用
        self.next_purpose_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_purpose_img(self.nowPurposeImg)
        # 判断是否为第一页
        if self.nowPurposeImg <= 1:
            self.pre_purpose_page.setEnabled(False)

    # 点击实验任务的下一页触发的事件
    def next_tasks_page_click(self):
        # 当前页+1
        self.nowTaskImg += 1
        # 上一页按钮可用
        self.pre_tasks_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_tasks_img(self.nowTaskImg)
        # 判断是否为最后一页
        tasks_img_num = os.listdir('resources/Image/tasks/chapter' + str(self.nowChapter))
        if self.nowTaskImg >= len(tasks_img_num):
            self.next_tasks_page.setEnabled(False)

    # 点击实验任务的上一页触发的事件
    def pre_tasks_page_click(self):
        # 当前页-1
        self.nowTaskImg -= 1
        # 下一页按钮可用
        self.next_tasks_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_tasks_img(self.nowTaskImg)
        # 判断是否为第一页
        if self.nowTaskImg <= 1:
            self.pre_tasks_page.setEnabled(False)

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

    # 点击实验装置的下一页触发的事件
    def next_equipment_page_click(self):
        # 当前页+1
        self.nowEquipmentImg += 1
        # 上一页按钮可用
        self.pre_equipment_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_equipment_img(self.nowEquipmentImg)
        # 判断是否为最后一页
        equipment_img_num = os.listdir('resources/Image/equipment/chapter' + str(self.nowChapter))
        if self.nowEquipmentImg >= len(equipment_img_num):
            self.next_equipment_page.setEnabled(False)

    # 点击实验装置的上一页触发的事件
    def pre_equipment_page_click(self):
        # 当前页-1
        self.nowEquipmentImg -= 1
        # 下一页按钮可用
        self.next_equipment_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_equipment_img(self.nowEquipmentImg)
        # 判断是否为第一页
        if self.nowEquipmentImg <= 1:
            self.pre_equipment_page.setEnabled(False)

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

    # 实验动画开始按钮点击
    def amination_in_click(self):
        # TODO 这里要进入实验动画,可以做一个判断
        print("进入实验动画")
        simulation = Simulation()
        simulation.verticalStackedWidget.setCurrentIndex(self.nowChapter - 1)
        simulation.show()
        print("实验动画页面被关闭")

    # 第五章数据处理的开始计算按钮绑定函数
    def data_processing_5_date_calculate_click(self):
        data_processing.data_processing_5_date_calculate_click(self)

    def data_processing_7_data_calculate_click(self):
        data_processing.data_processing_7_data_calculate_click(self)

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
        self.question.setText(question[1])
        self.section_A.setText(section_a)
        self.section_B.setText(section_b)
        self.section_C.setText(section_c)
        self.section_D.setText(section_d)

    # 答题结束的函数
    def finish_test(self):
        print("你的答案是: " + str(self.answerList))
        print("正确答案是: " + str(
            SqlTools.get_correct_answer_by_chapter(self.chapterBtnNameList[self.nowChapter - 1])))
        print("答题结束")

    # 接收主窗口，下面用于返回主窗口
    def receive_main(self, mainWindow):
        self.mainWindow = mainWindow

    # 返回主窗口
    def back_main(self):
        self.mainWindow.show()
        self.close()

    # 打开邮箱窗口
    def open_emailWindow(self):
        email_window = EmailWindow()
        email_window.show()

    # 手动改变窗口大小时，触发方法：
    def resizeEvent(self, event):
        # 获取窗口大小
        window_width = event.size().width()
        # tab栏宽度大概占窗口宽度1/9
        tab_width = str(window_width * 1 / 9)
        self.tabWidget_2.setStyleSheet("::tab{width: " + tab_width + ";\n"
                                                                   "    height:50;\n"
                                                                   "    background-color: rgb(128, 177, 198,100);\n"
                                                                   "    border-right: 1px solid  rgb(200, 200, 200);\n"
                                                                   "    font-size:20px;}\n"
                                                                   "::tab:last {\n"
                                                                   "    border:none;}\n"
                                                                   "::tab:hover {\n"
                                                                   "    background-color: rgb(128, 177, 198,150);\n"
                                                                   "}\n"
                                                                   "::tab:selected {\n"
                                                                   "    background-color: rgb(128, 177, 198);\n"
                                                                   "}")
    # 表格均分
    def table_style(self):
        # 实验一表格
        self.exp_data_1a.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_1a.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_1b.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_1b.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 实验二表格
        self.exp_data_2a.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_2a.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_2b.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_2b.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 实验三表格
        self.exp_data_3a.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_3a.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_3b.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_3b.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_3c.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.exp_data_3c.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    # 导出实验报告
    def select_report(self):
        if (self.nowChapter == 1):
            function.report_1.get_data(self)

