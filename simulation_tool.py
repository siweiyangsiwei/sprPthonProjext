from PyQt5 import QtWidgets
# 初始化分数记录
record_score_exp = {'第一章':'',
                    '第二章':'',
                    '第三章':'',
                    '第四章':'',
                    '第五章':'',
                    '第六章':'',
                    '第七章':'',
                    '第八章':'',
                    '第九章':''}


# 保存完成步骤的字典
exam_dict3 = dict.fromkeys(range(1,5+1),'')
exam_dict4 = dict.fromkeys(range(1,8+1),'')

# 第一章
# 打开墨水，计分点2
def ban_close_ink1(self):
    self.close_ink_1.setChecked(False)
    # # # self.table_exam1.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
# 关闭墨水，结束实验，计分5
def ban_open_ink1(self):
    self.open_ink_1.setChecked(False)
    # # # self.table_exam1.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
    # 无墨水
    self.laminar_flow.hide()
    self.turbulant_flow.hide()
# 加水，计分点1，观察，计分点34
def show_pattern_1(self):
    # 有水
    self.water_exp11.show()
    self.water_exp12.show()
    self.water_exp13.show()
    self.water_exp14.show()
    self.water_exp15.show()
    self.water_exp16.show()
    self.water_exp17.show()
    self.water_exp18.show()
    # # self.table_exam1.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
    # 水量小层流，水量大湍流
    open_rate_1 = self.pump_c_open_rate_1.value()
    if self.open_ink_1.isChecked():
        if open_rate_1 == 20:
            self.flow_rate_1.setText('40')
            self.reynold.setText('704')
            self.laminar_flow.show()
            # # self.table_exam1.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
        elif open_rate_1 == 40:
            self.flow_rate_1.setText('48')
            self.reynold.setText('844')
            self.laminar_flow.show()
            # # self.table_exam1.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
        elif open_rate_1 == 60:
            self.flow_rate_1.setText('83')
            self.reynold.setText('1460')
            self.laminar_flow.show()
            # # self.table_exam1.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
        elif open_rate_1 == 80:
            self.flow_rate_1.setText('134')
            self.reynold.setText('2356')
            self.turbulant_flow.show()
            # # self.table_exam1.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
        elif open_rate_1 == 100:
            self.flow_rate_1.setText('180')
            self.reynold.setText('3166')
            self.turbulant_flow.show()
            # # self.table_exam1.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
    else:
        # 有水但没有墨水
        if open_rate_1 == 20:
            self.flow_rate_1.setText('40')
        elif open_rate_1 == 40:
            self.flow_rate_1.setText('48')
        elif open_rate_1 == 60:
            self.flow_rate_1.setText('83')
        elif open_rate_1 == 80:
            self.flow_rate_1.setText('134')
        elif open_rate_1 == 100:
            self.flow_rate_1.setText('180')
# 重置实验
def restart_exam1(self):
    # 去掉水
    self.water_exp11.hide()
    self.water_exp12.hide()
    self.water_exp13.hide()
    self.water_exp14.hide()
    self.water_exp15.hide()
    self.water_exp16.hide()
    self.water_exp17.hide()
    self.water_exp18.hide()
    self.laminar_flow.hide()
    self.turbulant_flow.hide()
    # 阀门B set false
    self.open_ink_1.setChecked(False)
    self.close_ink_1.setChecked(False)
    # 流量、雷诺数清零
    self.flow_rate_1.setText('')
    self.reynold.setText('')
    # 阀门C清零
    self.pump_c_open_rate_1.setValue(0)
    # 表格清空
    # # self.table_exam1.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam1.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam1.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam1.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam1.setItem(4, 1, QtWidgets.QTableWidgetItem(''))

# 第二章
# 计分点1，阀门开度0，任意旋转
def whatever_water2(self):
    # 其余false
    self.front2.setChecked(False)
    self.vertical2.setChecked(False)
    # 显示水
    self.whatever_water1_2.show()
    self.whatever_water2_2.show()
    self.whatever_water3_2.show()
    self.whatever_water4_2.show()

    # 阀门开度
    water_rate2 = self.water_flow_rate2.value()
    # if water_rate2 == 0:
        # self.table_exam2.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
    # else:
        # self.table_exam2.setItem(0, 1, QtWidgets.QTableWidgetItem('错误'))
# 计分点23，阀门开度50，100,正对
def front_water2(self):
    # 其余false
    self.whatever2.setChecked(False)
    self.vertical2.setChecked(False)
    # 显示水
    self.whatever_water1_2.hide()
    self.whatever_water2_2.hide()
    self.whatever_water3_2.hide()
    self.whatever_water4_2.hide()
    self.front_water9_2.hide()
    self.front_water10_2.hide()
    self.front_water11_2.hide()
    self.front_water12_2.hide()
    self.vertical_water1_2.hide()
    self.vertical_water2_2.hide()
    self.vertical_water3_2.hide()
    self.vertical_water4_2.hide()
    # 阀门开度
    water_rate2 = self.water_flow_rate2.value()
    if water_rate2 == 50:
        self.front_water1_2.show()
        self.front_water2_2.show()
        self.front_water3_2.show()
        self.front_water4_2.show()
        self.front_water5_2.hide()
        self.front_water6_2.hide()
        self.front_water7_2.hide()
        self.front_water8_2.hide()
        # self.table_exam2.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
    elif water_rate2 == 100:
        self.front_water5_2.show()
        self.front_water6_2.show()
        self.front_water7_2.show()
        self.front_water8_2.show()
        self.front_water1_2.hide()
        self.front_water2_2.hide()
        self.front_water3_2.hide()
        self.front_water4_2.hide()
        # self.table_exam2.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
    # else:
        # self.table_exam2.setItem(1, 1, QtWidgets.QTableWidgetItem('错误'))
        # self.table_exam2.setItem(2, 1, QtWidgets.QTableWidgetItem('错误'))
# 计分点4，阀门开度100，垂直
def vertical_water2(self):
    self.front2.setChecked(False)
    self.whatever2.setChecked(False)
    self.whatever_water1_2.hide()
    self.whatever_water2_2.hide()
    self.whatever_water3_2.hide()
    self.whatever_water4_2.hide()
    self.front_water1_2.hide()
    self.front_water2_2.hide()
    self.front_water3_2.hide()
    self.front_water4_2.hide()
    self.front_water5_2.hide()
    self.front_water6_2.hide()
    self.front_water7_2.hide()
    self.front_water8_2.hide()
    self.front_water9_2.hide()
    self.front_water10_2.hide()
    self.front_water11_2.hide()
    self.front_water12_2.hide()
    # 阀门开度
    water_rate2 = self.water_flow_rate2.value()
    if water_rate2 == 100:
        self.vertical_water1_2.show()
        self.vertical_water2_2.show()
        self.vertical_water3_2.show()
        self.vertical_water4_2.show()
        # self.table_exam2.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
    # else:
        # self.table_exam2.setItem(3, 1, QtWidgets.QTableWidgetItem('错误'))
# 计分点5，阀门开度50，23正对
def front23_2(self):
    self.vertical_23_water_2.setChecked(False)
    self.whatever2.setChecked(False)
    self.front2.setChecked(False)
    self.vertical2.setChecked(False)
    # 显示水
    self.whatever_water1_2.hide()
    self.whatever_water2_2.hide()
    self.whatever_water3_2.hide()
    self.whatever_water4_2.hide()
    self.vertical_water1_2.hide()
    self.vertical_water2_2.hide()
    self.vertical_water3_2.hide()
    self.vertical_water4_2.hide()
    self.front_water5_2.hide()
    self.front_water6_2.hide()
    self.front_water7_2.hide()
    self.front_water8_2.hide()
    self.front_water9_2.hide()
    self.front_water10_2.hide()
    self.front_water11_2.hide()
    self.front_water12_2.hide()
    # 阀门开度
    water_rate2 = self.water_flow_rate2.value()
    if water_rate2 == 50:
        self.front_water1_2.show()
        self.front_water2_2.show()
        self.front_water3_2.show()
        self.front_water4_2.show()
        # self.table_exam2.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
    # else:
        # self.table_exam2.setItem(4, 1, QtWidgets.QTableWidgetItem('错误'))
# 计分点6，阀门开度50，23垂直
def vertical23_2(self):
    self.front_23_water_2.setChecked(False)
    self.whatever2.setChecked(False)
    self.front2.setChecked(False)
    self.vertical2.setChecked(False)
    self.whatever_water1_2.hide()
    self.whatever_water2_2.hide()
    self.whatever_water3_2.hide()
    self.whatever_water4_2.hide()
    self.front_water1_2.hide()
    self.front_water2_2.hide()
    self.front_water3_2.hide()
    self.front_water4_2.hide()
    self.front_water5_2.hide()
    self.front_water6_2.hide()
    self.front_water7_2.hide()
    self.front_water8_2.hide()
    self.vertical_water1_2.hide()
    self.vertical_water2_2.hide()
    self.vertical_water3_2.hide()
    self.vertical_water4_2.hide()
    water_rate2 = self.water_flow_rate2.value()
    if water_rate2 == 50:
        self.front_water9_2.show()
        self.front_water10_2.show()
        self.front_water11_2.show()
        self.front_water12_2.show()
        # self.table_exam2.setItem(5, 1, QtWidgets.QTableWidgetItem('完成'))
    # else:
        # self.table_exam2.setItem(5, 1, QtWidgets.QTableWidgetItem('错误'))
# 计分点7，量筒
def get_water_amount_2(self):
    self.get_water2.setEnabled(False)
    # self.table_exam2.setItem(6, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点8，计时
def get_the_time_2(self):
    self.count_time2.setEnabled(False)
    # self.table_exam2.setItem(7, 1, QtWidgets.QTableWidgetItem('完成'))
# 重置
def restart_exam2(self):
    # 水
    self.whatever_water1_2.hide()
    self.whatever_water2_2.hide()
    self.whatever_water3_2.hide()
    self.whatever_water4_2.hide()
    self.front_water1_2.hide()
    self.front_water2_2.hide()
    self.front_water3_2.hide()
    self.front_water4_2.hide()
    self.front_water5_2.hide()
    self.front_water6_2.hide()
    self.front_water7_2.hide()
    self.front_water8_2.hide()
    self.front_water9_2.hide()
    self.front_water10_2.hide()
    self.front_water11_2.hide()
    self.front_water12_2.hide()
    self.vertical_water1_2.hide()
    self.vertical_water2_2.hide()
    self.vertical_water3_2.hide()
    self.vertical_water4_2.hide()
    # 按钮
    self.whatever2.setChecked(False)
    self.front2.setChecked(False)
    self.vertical2.setChecked(False)
    self.vertical_23_water_2.setChecked(False)
    self.front_23_water_2.setChecked(False)
    self.get_water2.setEnabled(True)
    self.count_time2.setEnabled(True)
    # 阀门开度
    self.water_flow_rate2.setValue(0)
    # 表格
    # self.table_exam2.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam2.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam2.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam2.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam2.setItem(4, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam2.setItem(5, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam2.setItem(6, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam2.setItem(7, 1, QtWidgets.QTableWidgetItem(''))

# 第三章
# 1、水槽加水，评分点1
def add_water_box3(self):
    global exam_dict3
    # 加水
    self.water_icon_3.show()
    # 只能加一次水
    self.add_water_b3.setEnabled(False)
    exam_dict3[1] = '完成'
    # self.table_exam3.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
    print(exam_dict3)
# 2、灌泵，评分点2
def add_water_pump3(self):
    global exam_dict3
    # 灌泵
    self.water_icon_4.show()
    # 只能灌一次泵
    self.add_water_p3.setEnabled(False)
    # 如果此时泵打开，0分
    if self.pump_on_3.isChecked():
        exam_dict3[2] = '错误'
        # self.table_exam3.setItem(1, 1, QtWidgets.QTableWidgetItem('错误'))
    # 如果此时关泵，有分
    else:
        exam_dict3[2] = '完成'
        # self.table_exam3.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
    print(exam_dict3)
# 3、开泵（出口阀要关，进口阀要开），评分点3
def open_the_pump3(self):
    global exam_dict3
    self.tube_water_3.show()
    self.tube_water_4.show()
    # 只能开一次泵
    self.pump_on_3.setEnabled(False)
    # 开泵时，进口阀如果打开，判断出口阀
    if self.open_in_3.isChecked():
        # 开泵时，如果出口阀门打开，扣分，关闭则加分
        if self.pump_open_rate_3.value() != 0:
            exam_dict3[3] = '错误'
            # self.table_exam3.setItem(2, 1, QtWidgets.QTableWidgetItem('错误'))
        elif self.pump_open_rate_3.value() == 0:
            exam_dict3[3] = '完成'
            # self.table_exam3.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
    else:
        # 开泵时，进口阀关闭，则零分
        exam_dict3[3] = '错误'
        # self.table_exam3.setItem(2, 1, QtWidgets.QTableWidgetItem('错误'))
    print(exam_dict3)
# 4、开启出口阀，改变两个压差、流量，加分点4
def open_out_valve3(self):
    global exam_dict3
    if self.pump_on_3.isEnabled() == False:
        exam_dict3[4] = '完成'
        # self.table_exam3.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
        self.tube_wt1_2.show()
        self.tube_wt2_2.show()
        self.tube_wt3_2.show()
        self.tube_wt4_2.show()
        self.tube_wt5_2.show()
        self.tube_wt6_2.show()
        open_rate_3 = self.pump_open_rate_3.value()
        if open_rate_3 == 10:
            self.flow_rate_3.setText('4.43')
            self.straight_p3.setText('0.601')
            self.corner_p3.setText('0.466')
        elif open_rate_3 == 20:
            self.flow_rate_3.setText('6.20')
            self.straight_p3.setText('1.134')
            self.corner_p3.setText('0.879')
        elif open_rate_3 == 30:
            self.flow_rate_3.setText('7.63')
            self.straight_p3.setText('1.644')
            self.corner_p3.setText('1.287')
        elif open_rate_3 == 40:
            self.flow_rate_3.setText('8.64')
            self.straight_p3.setText('2.006')
            self.corner_p3.setText('1.634')
        elif open_rate_3 == 50:
            self.flow_rate_3.setText('9.86')
            self.straight_p3.setText('2.639')
            self.corner_p3.setText('2.108')
        elif open_rate_3 == 60:
            self.flow_rate_3.setText('11.05')
            self.straight_p3.setText('3.193')
            self.corner_p3.setText('2.601')
        elif open_rate_3 == 70:
            self.flow_rate_3.setText('12.10')
            self.straight_p3.setText('3.757')
            self.corner_p3.setText('3.105')
        elif open_rate_3 == 80:
            self.flow_rate_3.setText('13.18')
            self.straight_p3.setText('4.453')
            self.corner_p3.setText('3.700')
        elif open_rate_3 == 90:
            self.flow_rate_3.setText('14.04')
            self.straight_p3.setText('5.030')
            self.corner_p3.setText('4.518')
        elif open_rate_3 == 100:
            self.flow_rate_3.setText('15.08')
            self.straight_p3.setText('5.785')
            self.corner_p3.setText('4.947')
    else:
        exam_dict3[4] = '错误'
    print(exam_dict3)
# 5、停泵，评分点5
def close_the_pump3(self):
    global exam_dict3
    # 只能关一次泵
    self.pump_off_3.setEnabled(False)
    # 关泵时，出口阀不为0则没分
    if self.pump_open_rate_3.value() != 0:
        exam_dict3[5] = '错误'
        # self.table_exam3.setItem(4, 1, QtWidgets.QTableWidgetItem('错误'))
    # 关了出口阀就加分
    else:
        exam_dict3[5] = '完成'
        # self.table_exam3.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
    print(exam_dict3)
    # 去掉所有水
    self.tube_wt1_2.hide()
    self.tube_wt2_2.hide()
    self.tube_wt3_2.hide()
    self.tube_wt4_2.hide()
    self.tube_wt5_2.hide()
    self.tube_wt6_2.hide()
    self.tube_water_3.hide()
    self.tube_water_4.hide()
    # 去掉显示的值
    self.pump_open_rate_3.setValue(0)
    self.flow_rate_3.clear()
    self.straight_p3.clear()
    self.corner_p3.clear()
# 重置
def restart_exam3(self):
    global exam_dict3
    # 去掉水槽的水，可以再次加水
    self.water_icon_3.hide()
    self.add_water_b3.setEnabled(True)
    # 去掉泵里的水，可以再次加水
    self.water_icon_4.hide()
    self.add_water_p3.setEnabled(True)
    # 出口阀开闭清零
    self.pump_open_rate_3.setValue(0)
    # 流量计数据清零
    self.flow_rate_3.setText('')
    # 分数清零
    exam_dict3 = dict.fromkeys(range(1,5+1),'')
    print(exam_dict3)
    # self.table_exam3.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam3.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam3.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam3.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam3.setItem(4, 1, QtWidgets.QTableWidgetItem(''))
    # 去掉所有水
    self.tube_wt1_2.hide()
    self.tube_wt2_2.hide()
    self.tube_wt3_2.hide()
    self.tube_wt4_2.hide()
    self.tube_wt5_2.hide()
    self.tube_wt6_2.hide()
    self.tube_water_3.hide()
    self.tube_water_4.hide()
    # 泵的开闭清零
    self.pump_on_3.setEnabled(True)
    self.pump_off_3.setEnabled(True)
    # 进口阀开闭清零
    self.close_in_3.setChecked(False)
    self.open_in_3.setChecked(False)
    # 两个压力表数据清零
    self.straight_p3.setText('')
    self.corner_p3.setText('')
# 进口泵按钮设置
def ban_close_in_3(self):
    self.close_in_4.setChecked(False)
def ban_open_in_3(self):
    self.open_in_4.setChecked(False)
# 提交分数
def summit_simu_3(self):
    global exam_dict3
    print(exam_dict3)

# 第四章
# 转速按钮设置，点了一个另一个取消，且点击2700后，可以重新开泵
# 加分点4、6
def ban_2700(self):
    global exam_dict4
    self.pump_2700.setChecked(False)
    exam_dict4[4] = '完成'
    # self.table_exam4.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
    print(exam_dict4)
def ban_2400(self):
    global exam_dict4
    self.pump_2400.setChecked(False)
    exam_dict4[6] = '完成'
    # self.table_exam4.setItem(5, 1, QtWidgets.QTableWidgetItem('完成'))
    print(exam_dict4)
    # 重新开泵
    self.pump_open_rate_4.setValue(0)
    self.flow_rate_4.clear()
    self.pump_work_4.clear()
    self.in_p_4.clear()
    self.out_p_4.clear()
# 进口泵按钮设置
def ban_close_in_4(self):
    self.close_in_4.setChecked(False)
def ban_open_in_4(self):
    self.open_in_4.setChecked(False)
# 1、选择转速
# 2、水槽加水，加分1
def add_water_box4(self):
    global exam_dict4
    # 加水
    self.water_icon.show()
    # 只能加一次水
    self.add_water_b4.setEnabled(False)
    exam_dict4[1] = '完成'
    print(exam_dict4)
    # self.table_exam4.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
# 3、灌泵，加分2
def add_water_pump4(self):
    global exam_dict4
    # 灌泵
    self.water_icon_2.show()
    # 只能灌一次泵
    self.add_water_p4.setEnabled(False)
    exam_dict4[2] = '完成'
    print(exam_dict4)
    # self.table_exam4.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
# 4、开泵（出口阀要关，进口阀要开），加分3
def open_the_pump4(self):
    global exam_dict4
    self.tube_water_1.show()
    self.tube_water_2.show()
    # 只能开一次泵
    self.pump_on_4.setEnabled(False)
    # 开泵时，进口阀如果打开，判断出口阀
    if self.open_in_4.isChecked():
        # 开泵时，如果出口阀门打开，扣分，关闭则加分
        if self.pump_open_rate_4.value() != 0:
            exam_dict4[3] = '错误'
            # self.table_exam4.setItem(2, 1, QtWidgets.QTableWidgetItem('错误'))
        elif self.pump_open_rate_4.value() == 0:
            exam_dict4[3] = '完成'
            # self.table_exam4.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
    else:
        exam_dict4[3] = '错误'
        # self.table_exam4.setItem(2, 1, QtWidgets.QTableWidgetItem('错误'))

    print(exam_dict4)
# 5、开出口阀（2400，2700共用），加分5（2400）、7（2700）
def open_out_valve4(self):
    global exam_dict4
    if self.pump_on_4.isEnabled() == False:
        self.tube_wt1.show()
        self.tube_wt2.show()
        self.tube_wt3.show()
        self.tube_wt4.show()
        self.tube_wt5.show()
        self.tube_wt6.show()
        open_rate = self.pump_open_rate_4.value()
        if self.pump_2400.isChecked():
            # self.table_exam4.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
            exam_dict4[5] = '完成'
            print(exam_dict4)
            if open_rate == 5:
                self.flow_rate_4.setText('3.00')
                self.pump_work_4.setText('0.37')
                self.in_p_4.setText('-0.06')
                self.out_p_4.setText('0.127')
            elif open_rate == 10:
                self.flow_rate_4.setText('4.00')
                self.pump_work_4.setText('0.41')
                self.in_p_4.setText('-0.07')
                self.out_p_4.setText('0.125')
            elif open_rate == 20:
                self.flow_rate_4.setText('5.00')
                self.pump_work_4.setText('0.45')
                self.in_p_4.setText('-0.08')
                self.out_p_4.setText('0.121')
            elif open_rate == 30:
                self.flow_rate_4.setText('6.00')
                self.pump_work_4.setText('0.50')
                self.in_p_4.setText('-0.10')
                self.out_p_4.setText('0.116')
            elif open_rate == 40:
                self.flow_rate_4.setText('7.00')
                self.pump_work_4.setText('0.53')
                self.in_p_4.setText('-0.12')
                self.out_p_4.setText('0.109')
            elif open_rate == 50:
                self.flow_rate_4.setText('8.00')
                self.pump_work_4.setText('0.56')
                self.in_p_4.setText('-0.13')
                self.out_p_4.setText('0.101')
            elif open_rate == 60:
                self.flow_rate_4.setText('9.00')
                self.pump_work_4.setText('0.59')
                self.in_p_4.setText('-0.16')
                self.out_p_4.setText('0.091')
            elif open_rate == 70:
                self.flow_rate_4.setText('10.00')
                self.pump_work_4.setText('0.62')
                self.in_p_4.setText('-0.19')
                self.out_p_4.setText('0.080')
            elif open_rate == 80:
                self.flow_rate_4.setText('11.00')
                self.pump_work_4.setText('0.63')
                self.in_p_4.setText('-0.21')
                self.out_p_4.setText('0.070')
            elif open_rate == 90:
                self.flow_rate_4.setText('12.00')
                self.pump_work_4.setText('0.63')
                self.in_p_4.setText('-0.24')
                self.out_p_4.setText('0.055')
            elif open_rate == 95:
                self.flow_rate_4.setText('13.00')
                self.pump_work_4.setText('0.64')
                self.in_p_4.setText('-0.27')
                self.out_p_4.setText('0.039')
            elif open_rate == 100:
                self.flow_rate_4.setText('14.00')
                self.pump_work_4.setText('0.65')
                self.in_p_4.setText('-0.30')
                self.out_p_4.setText('0.026')
        elif self.pump_2700.isChecked():
            # self.table_exam4.setItem(6, 1, QtWidgets.QTableWidgetItem('完成'))
            exam_dict4[7] = '完成'
            print(exam_dict4)
            if open_rate == 5:
                self.flow_rate_4.setText('3.00')
                self.pump_work_4.setText('0.48')
                self.in_p_4.setText('-0.06')
                self.out_p_4.setText('0.156')
            elif open_rate == 10:
                self.flow_rate_4.setText('4.00')
                self.pump_work_4.setText('0.54')
                self.in_p_4.setText('-0.07')
                self.out_p_4.setText('0.154')
            elif open_rate == 20:
                self.flow_rate_4.setText('5.00')
                self.pump_work_4.setText('0.58')
                self.in_p_4.setText('-0.09')
                self.out_p_4.setText('0.150')
            elif open_rate == 30:
                self.flow_rate_4.setText('6.00')
                self.pump_work_4.setText('0.63')
                self.in_p_4.setText('-0.10')
                self.out_p_4.setText('0.154')
            elif open_rate == 40:
                self.flow_rate_4.setText('7.00')
                self.pump_work_4.setText('0.66')
                self.in_p_4.setText('-0.12')
                self.out_p_4.setText('0.139')
            elif open_rate == 50:
                self.flow_rate_4.setText('8.00')
                self.pump_work_4.setText('0.71')
                self.in_p_4.setText('-0.13')
                self.out_p_4.setText('0.131')
            elif open_rate == 60:
                self.flow_rate_4.setText('9.00')
                self.pump_work_4.setText('0.73')
                self.in_p_4.setText('-0.16')
                self.out_p_4.setText('0.122')
            elif open_rate == 70:
                self.flow_rate_4.setText('10.00')
                self.pump_work_4.setText('0.74')
                self.in_p_4.setText('-0.19')
                self.out_p_4.setText('0.113')
            elif open_rate == 80:
                self.flow_rate_4.setText('11.00')
                self.pump_work_4.setText('0.78')
                self.in_p_4.setText('-0.21')
                self.out_p_4.setText('0.100')
            elif open_rate == 90:
                self.flow_rate_4.setText('12.00')
                self.pump_work_4.setText('0.83')
                self.in_p_4.setText('-0.24')
                self.out_p_4.setText('0.087')
            elif open_rate == 95:
                self.flow_rate_4.setText('13.00')
                self.pump_work_4.setText('0.85')
                self.in_p_4.setText('-0.27')
                self.out_p_4.setText('0.074')
            elif open_rate == 100:
                self.flow_rate_4.setText('14.00')
                self.pump_work_4.setText('0.88')
                self.in_p_4.setText('-0.32')
                self.out_p_4.setText('0.055')
# 6、停泵
def close_the_pump4(self):
    global exam_dict4
    # 只能关一次泵
    self.pump_off_4.setEnabled(False)
    # 关泵时，出口阀不为0则没分
    if self.pump_open_rate_4.value() != 0:
        exam_dict4[8] = '错误'
        # self.table_exam4.setItem(7, 1, QtWidgets.QTableWidgetItem('错误'))
    # 关了出口阀就加分
    else:
        exam_dict4[8] = '完成'
        # self.table_exam4.setItem(7, 1, QtWidgets.QTableWidgetItem('完成'))
    print(exam_dict4)
    # 去掉所有水
    self.tube_wt1.hide()
    self.tube_wt2.hide()
    self.tube_wt3.hide()
    self.tube_wt4.hide()
    self.tube_wt5.hide()
    self.tube_wt6.hide()
    self.tube_water_1.hide()
    self.tube_water_2.hide()
    # 去掉显示的值
    self.pump_open_rate_4.setValue(0)
    self.flow_rate_4.clear()
    self.pump_work_4.clear()
    self.in_p_4.clear()
    self.out_p_4.clear()
# 重置实验数据
def restart_exam4(self):
    global exam_dict4
    # 去掉水槽的水，可以再次加水
    self.water_icon.hide()
    self.add_water_b4.setEnabled(True)
    # 去掉泵里的水，可以再次加水
    self.water_icon_2.hide()
    self.add_water_p4.setEnabled(True)
    # 出口阀开闭清零
    self.pump_open_rate_4.setValue(0)
    # 流量计数据清零
    self.flow_rate_4.setText('')
    # 转速清零
    self.pump_2400.setChecked(False)
    self.pump_2700.setChecked(False)
    # 轴功率清零
    self.pump_work_4.setText('')
    # 分数清零
    exam_dict4 = dict.fromkeys(range(1,8+1),'')
    print(exam_dict4)
    # self.table_exam4.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam4.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam4.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam4.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam4.setItem(4, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam4.setItem(5, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam4.setItem(6, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam4.setItem(7, 1, QtWidgets.QTableWidgetItem(''))
    # 去掉所有水
    self.tube_wt1.hide()
    self.tube_wt2.hide()
    self.tube_wt3.hide()
    self.tube_wt4.hide()
    self.tube_wt5.hide()
    self.tube_wt6.hide()
    self.tube_water_1.hide()
    self.tube_water_2.hide()
    # 泵的开闭清零
    self.pump_on_4.setEnabled(True)
    self.pump_off_4.setEnabled(True)
    # 进口阀开闭清零
    self.close_in_4.setChecked(False)
    self.open_in_4.setChecked(False)
    # 两个压力表数据清零
    self.in_p_4.setText('')
    self.out_p_4.setText('')
# 提交成绩
def summit_simu_4(self):
    print(exam_dict4)
    self.get_simu_score4.setEnabled(False)

# 第五章
# 计分点1，浸湿滤布
def soak_the_cloth5(self):
    self.soak_filter5.setEnabled(False)
    # self.table_exam5.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点2，安装机器
def equip_filter5(self):
    self.finish5.show()
    self.equip_5.setEnabled(False)
    # self.table_exam5.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点3，启动搅拌
def stir5(self):
    self.dirty5_2.show()
    self.open_stir5.setEnabled(False)
    # self.table_exam5.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点4，开启滤浆阀门
def start_filter5(self):
    self.open_filter5.setEnabled(False)
    # self.table_exam5.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点5，开启洗液
def start_wash5(self):
    self.open_wash5.setEnabled(False)
    # self.table_exam5.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点6，开启空气
def get_air_5(self):
    self.open_air5.setEnabled(False)
    # if self.open_filter5.isEnabled() or self.open_wash5.isEnabled():
        # self.table_exam5.setItem(5, 1, QtWidgets.QTableWidgetItem('错误'))

    # else:
    #     self.water5.show()
    #     self.dirty5.show()
        # self.table_exam5.setItem(5, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点7，调节压力
def adjust_ap5(self):
    self.adjust_air5.setEnabled(False)
    # if self.open_air5.isEnabled():
        # self.table_exam5.setItem(6, 1, QtWidgets.QTableWidgetItem('错误'))
    # else:
        # self.table_exam5.setItem(6, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点8，量筒
def get_the_water5(self):
    self.get_water5.setEnabled(False)
    # if self.open_air5.isEnabled() == False and self.open_filter5.isEnabled() == False and self.open_wash5.isEnabled() == False:
    #     self.water_cup5.show()
        # self.table_exam5.setItem(7, 1, QtWidgets.QTableWidgetItem('完成'))
    # else:
        # self.table_exam5.setItem(7, 1, QtWidgets.QTableWidgetItem('错误'))
# 计分点9，秒表
def count_the_time5(self):
    self.count_time5.setEnabled(False)
    # self.table_exam5.setItem(8, 1, QtWidgets.QTableWidgetItem('完成'))
# 重置
def restart_exam5(self):
    # 按钮
    self.soak_filter5.setEnabled(True)
    self.equip_5.setEnabled(True)
    self.open_wash5.setEnabled(True)
    self.open_filter5.setEnabled(True)
    self.open_air5.setEnabled(True)
    self.open_stir5.setEnabled(True)
    self.adjust_air5.setEnabled(True)
    self.get_water5.setEnabled(True)
    self.count_time5.setEnabled(True)
    # 标签
    self.finish5.hide()
    self.water5.hide()
    self.dirty5.hide()
    self.dirty5_2.hide()
    self.water_cup5.hide()
    # 表格
    # self.table_exam5.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam5.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam5.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam5.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam5.setItem(4, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam5.setItem(5, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam5.setItem(6, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam5.setItem(7, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam5.setItem(8, 1, QtWidgets.QTableWidgetItem(''))

# 第六章
# 计分点1，点开加热器
def ban_close_heat_6(self):
    self.close_heat_6.setChecked(False)
    # self.table_exam6.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点5，关闭加热器
def ban_open_heat_6(self):
    self.open_heat_6.setChecked(False)
    # 如果先关了鼓风机，则错
    # if self.close_air_6.isChecked():
        # self.table_exam6.setItem(4, 1, QtWidgets.QTableWidgetItem('错误'))
    # else:
        # self.table_exam6.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点3，开蒸汽阀门
def ban_close_gas_6(self):
    self.close_gas_6.setChecked(False)
    # 热空气显示
    self.gas_1.show()
    self.gas_2.show()
    # if self.open_air_6.isChecked() == False:
        # self.table_exam6.setItem(2, 1, QtWidgets.QTableWidgetItem('错误'))
    # else:
        # self.table_exam6.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点6，关蒸汽阀门
def ban_open_gas_6(self):
    self.open_gas_6.setChecked(False)
    # 热空气不显示
    self.gas_1.hide()
    self.gas_2.hide()
    # 如果先关了鼓风机，则错
    # if self.close_air_6.isChecked():
        # self.table_exam6.setItem(5, 1, QtWidgets.QTableWidgetItem('错误'))
    # else:
        # self.table_exam6.setItem(5, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点2，开鼓风机
def ban_close_air_6(self):
    self.close_air_6.setChecked(False)
    # 空气显示
    self.cold_air.show()
    # self.table_exam6.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点7，关鼓风机
def ban_open_air_6(self):
    self.open_air_6.setChecked(False)
    # 空气不显示
    self.cold_air.hide()
    # self.table_exam6.setItem(6, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点4，实验过程
def show_data_6(self):
    # 确保前面三个已经打开
    if self.close_heat_6.isChecked() == False and self.close_gas_6.isChecked()==False and self.close_air_6.isChecked()==False:
        # self.table_exam6.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
        open_rate_6 = self.open_air_rate_6.value()
        if open_rate_6 == 10:
            self.air_pressure_6.setText('1.99')
            self.air_flow_rate_6.setText('19.2')
            self.air_t_in_6.setText('35.0')
            self.air_t_out_6.setText('93.6')
            self.ts_6.setText('115.4')
            self.tw_6.setText('107.9')
            self.gas_pressure_6.setText('59')
        elif open_rate_6 == 20:
            self.air_pressure_6.setText('1.79')
            self.air_flow_rate_6.setText('18.2')
            self.air_t_in_6.setText('34.5')
            self.air_t_out_6.setText('93.5')
            self.ts_6.setText('115.3')
            self.tw_6.setText('108.2')
            self.gas_pressure_6.setText('59')
        elif open_rate_6 == 30:
            self.air_pressure_6.setText('1.57')
            self.air_flow_rate_6.setText('17.1')
            self.air_t_in_6.setText('34.3')
            self.air_t_out_6.setText('93.1')
            self.ts_6.setText('115.5')
            self.tw_6.setText('108.2')
            self.gas_pressure_6.setText('59')
        elif open_rate_6 == 40:
            self.air_pressure_6.setText('1.43')
            self.air_flow_rate_6.setText('16.2')
            self.air_t_in_6.setText('34.0')
            self.air_t_out_6.setText('92.8')
            self.ts_6.setText('115.5')
            self.tw_6.setText('108.2')
            self.gas_pressure_6.setText('59')
        elif open_rate_6 == 50:
            self.air_pressure_6.setText('1.22')
            self.air_flow_rate_6.setText('15.0')
            self.air_t_in_6.setText('33.2')
            self.air_t_out_6.setText('92.3')
            self.ts_6.setText('115.5')
            self.tw_6.setText('108.5')
            self.gas_pressure_6.setText('60')
        elif open_rate_6 == 60:
            self.air_pressure_6.setText('1.11')
            self.air_flow_rate_6.setText('14.3')
            self.air_t_in_6.setText('32.7')
            self.air_t_out_6.setText('91.6')
            self.ts_6.setText('115.3')
            self.tw_6.setText('108.2')
            self.gas_pressure_6.setText('58')
        elif open_rate_6 == 70:
            self.air_pressure_6.setText('0.93')
            self.air_flow_rate_6.setText('13.0')
            self.air_t_in_6.setText('32.2')
            self.air_t_out_6.setText('90.9')
            self.ts_6.setText('115.2')
            self.tw_6.setText('108.3')
            self.gas_pressure_6.setText('58')
        elif open_rate_6 == 80:
            self.air_pressure_6.setText('0.80')
            self.air_flow_rate_6.setText('12.0')
            self.air_t_in_6.setText('31.8')
            self.air_t_out_6.setText('90.4')
            self.ts_6.setText('115.2')
            self.tw_6.setText('108.3')
            self.gas_pressure_6.setText('59')
        elif open_rate_6 == 90:
            self.air_pressure_6.setText('0.69')
            self.air_flow_rate_6.setText('11.2')
            self.air_t_in_6.setText('31.5')
            self.air_t_out_6.setText('90.0')
            self.ts_6.setText('115.5')
            self.tw_6.setText('108.7')
            self.gas_pressure_6.setText('59')
        elif open_rate_6 == 100:
            self.air_pressure_6.setText('0.69')
            self.air_flow_rate_6.setText('11.2')
            self.air_t_in_6.setText('31.5')
            self.air_t_out_6.setText('90.0')
            self.ts_6.setText('115.5')
            self.tw_6.setText('108.7')
            self.gas_pressure_6.setText('59')
    # else:
        # self.table_exam6.setItem(3, 1, QtWidgets.QTableWidgetItem('错误'))
# 重置按钮
def restart_exam6(self):
    # 所有按钮重置
    self.close_air_6.setChecked(False)
    self.open_air_6.setChecked(False)
    self.close_gas_6.setChecked(False)
    self.open_gas_6.setChecked(False)
    self.close_heat_6.setChecked(False)
    self.open_heat_6.setChecked(False)
    # 仪表示数清空
    self.air_pressure_6.setText('')
    self.air_flow_rate_6.setText('')
    self.air_t_in_6.setText('')
    self.air_t_out_6.setText('')
    self.ts_6.setText('')
    self.tw_6.setText('')
    self.gas_pressure_6.setText('')
    self.open_air_rate_6.setValue(0)
    # 表格清空
    # self.table_exam6.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam6.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam6.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam6.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam6.setItem(4, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam6.setItem(5, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam6.setItem(6, 1, QtWidgets.QTableWidgetItem(''))
    # 气体
    self.cold_air.hide()
    self.gas_1.hide()
    self.gas_2.hide()

# 第七章
# 加分点1，开电源
def ban_closee7(self):
    self.close_e_7.setChecked(False)
    # self.table_exam7.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点2，开进料泵
def ban_close_inpump7(self):
    self.close_in_pump_7.setChecked(False)
    # self.table_exam7.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点3，开电加热器
def ban_close_heat7(self):
    self.close_heat7.setChecked(False)
    # self.table_exam7.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点4，开冷却水阀
def ban_close_cold7(self):
    self.close_cold_water7.setChecked(False)
    # self.table_exam7.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点5，关闭产品阀
def ban_open_d7(self):
    self.open_d_7.setChecked(False)
    # self.table_exam7.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点7，调节釜液阀门
def adjust_the_w7(self):
    self.adjust_w7.setEnabled(False)
    # self.table_exam7.setItem(6, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点6，打开产品阀
def ban_close_d7(self):
    self.close_d_7.setChecked(False)
    # if self.open_cold_water7.isChecked() == False:
        # self.table_exam7.setItem(5, 1, QtWidgets.QTableWidgetItem('错误'))
    # else:
        # self.table_exam7.setItem(5, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点8，取釜液
def get_w_7(self):
    self.get_w7.setEnabled(False)
    # self.table_exam7.setItem(7, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点9，取产品
def get_d_7(self):
    self.get_d7.setEnabled(False)
    # self.table_exam7.setItem(8, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点10，关闭电加热器
def ban_open_heat7(self):
    self.open_heat7.setChecked(False)
    # self.table_exam7.setItem(9, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点11，关闭冷却水
def ban_open_cold7(self):
    self.open_cold_water7.setChecked(False)
    # if self.open_heat7.isChecked():
        # self.table_exam7.setItem(10, 1, QtWidgets.QTableWidgetItem('错误'))
    # else:
        # self.table_exam7.setItem(10, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点12，关泵
def ban_open_inpump7(self):
    self.open_in_pump_7.setChecked(False)
    # self.table_exam7.setItem(11, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点13，关闭电源
def ban_opene7(self):
    self.open_e_7.setChecked(False)
    # self.table_exam7.setItem(12, 1, QtWidgets.QTableWidgetItem('完成'))
# 重置
def restart_exam7(self):
    self.open_e_7.setChecked(False)
    self.close_e_7.setChecked(False)
    self.open_cold_water7.setChecked(False)
    self.close_cold_water7.setChecked(False)
    self.open_in_pump_7.setChecked(False)
    self.close_in_pump_7.setChecked(False)
    self.open_heat7.setChecked(False)
    self.close_heat7.setChecked(False)
    self.open_d_7.setChecked(False)
    self.close_d_7.setChecked(False)
    self.get_w7.setEnabled(True)
    self.get_d7.setEnabled(True)
    self.adjust_w7.setEnabled(True)
    # 清除表格
    # self.table_exam7.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(4, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(5, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(6, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(7, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(8, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(9, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(10, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(11, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam7.setItem(12, 1, QtWidgets.QTableWidgetItem(''))

# 第八章
# 计分点1，打开水泵
def open_water8(self):
    self.open_pump8.setEnabled(False)
    # self.table_exam8.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点23，调节水流量
def big_water8(self):
    self.adjust_water8small.setChecked(False)
    self.water_flow_rate8.setText('200')
    # self.table_exam8.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
def small_water8(self):
    self.adjust_water8big.setChecked(False)
    self.water_flow_rate8.setText('150')
    # self.table_exam8.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点4，打开风机
def open_the_air8(self):
    self.open_air8.setEnabled(False)
    # self.table_exam8.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点5，调节空气
def adjust_the_air8(self):
    self.adjust_air8.setEnabled(False)
    if self.open_air8.isEnabled() == False:
        self.air_flow_rate8.setText('0.3')
        # self.table_exam8.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
    else:
        self.air_flow_rate8.setText('')
        # self.table_exam8.setItem(4, 1, QtWidgets.QTableWidgetItem('错误'))
# 计分点6，调节co2
def adjust_the_co28(self):
    self.adjust_co28.setEnabled(False)
    self.co2_flow_rate8.setText('0.4')
    # self.table_exam8.setItem(5, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点7，记录数据
def note_down8(self):
    self.note8.setEnabled(False)
    # self.table_exam8.setItem(6, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点8，打开尾气检测阀
def check_rest8(self):
    self.open_in8.setChecked(False)
    # self.table_exam8.setItem(7, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点9，打开进气检测阀
def check_in8(self):
    if self.open_rest8.isChecked() == False:
        self.open_rest8.setChecked(False)
        # self.table_exam8.setItem(8, 1, QtWidgets.QTableWidgetItem('错误'))
    else:
        self.open_rest8.setChecked(False)
        # self.table_exam8.setItem(8, 1, QtWidgets.QTableWidgetItem('完成'))
# 重置
def restart_exam8(self):
    self.open_pump8.setEnabled(True)
    self.adjust_water8big.setChecked(False)
    self.adjust_water8small.setChecked(False)
    self.water_flow_rate8.setText('')
    self.open_air8.setEnabled(True)
    self.adjust_air8.setEnabled(True)
    self.adjust_co28.setEnabled(True)
    self.air_flow_rate8.setText('')
    self.co2_flow_rate8.setText('')
    self.note8.setEnabled(True)
    self.open_rest8.setChecked(False)
    self.open_in8.setChecked(False)
    # self.table_exam8.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam8.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam8.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam8.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam8.setItem(4, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam8.setItem(5, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam8.setItem(6, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam8.setItem(7, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam8.setItem(8, 1, QtWidgets.QTableWidgetItem(''))

# 第九章
# 加分点1，测量物料
def measure_dry9(self):
    self.measure_size9.setEnabled(False)
    # self.table_exam9.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点2，称量物料
def get_the_gc9(self):
    self.get_gc9.setEnabled(False)
    # self.table_exam9.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点3，检查天平
def check_the_weight9(self):
    self.check_weight9.setEnabled(False)
    # self.table_exam9.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点4，温度计加水
def add_water_wet_ball9(self):
    self.water_wet_ball9.show()
    self.add_water9.setEnabled(False)
    # self.table_exam9.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点5，打开总开关
def ban_close_e9(self):
    self.close_e9.setChecked(False)
    # self.table_exam9.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点6，打开风机
def ban_close_air9(self):
    self.close_air9.setChecked(False)
    # if self.heat19.isChecked() or self.heat29.isChecked() or self.heat39.isChecked():
        # self.table_exam9.setItem(5, 1, QtWidgets.QTableWidgetItem('错误'))
    # else:
        # self.table_exam9.setItem(5, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点7，打开三个加热
def check_heat9(self):
    print("..")
    # if self.heat19.isChecked() and self.heat29.isChecked() and self.heat39.isChecked():
        # self.table_exam9.setItem(6, 1, QtWidgets.QTableWidgetItem('完成'))
    # else:
        # self.table_exam9.setItem(6, 1, QtWidgets.QTableWidgetItem('错误'))
# 加分点8，关闭加热2
def stop_heat_92(self):
    self.stop_heat92.setEnabled(False)
    self.heat29.setChecked(False)
    # self.table_exam9.setItem(7, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点9，放入物料
def show_thing9(self):
    self.wet_thing9.show()
    self.put_in9.setEnabled(False)
    # self.table_exam9.setItem(8, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点10，记录时间
def count_the_time9(self):
    self.count_time9.setEnabled(False)
    # self.table_exam9.setItem(9, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点11，关闭加热
def stop_the_heat9(self):
    self.stop_heat9.setEnabled(False)
    self.heat19.setChecked(False)
    self.heat29.setChecked(False)
    self.heat39.setChecked(False)
    # if self.close_air9.isChecked():
        # self.table_exam9.setItem(10, 1, QtWidgets.QTableWidgetItem('错误'))
    # else:
        # self.table_exam9.setItem(10, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点12，关闭风机
def ban_open_air9(self):
    self.open_air9.setChecked(False)
    # self.table_exam9.setItem(11, 1, QtWidgets.QTableWidgetItem('完成'))
# 加分点13，关闭总电源
def ban_open_e9(self):
    self.open_e9.setChecked(False)
    # self.table_exam9.setItem(12, 1, QtWidgets.QTableWidgetItem('完成'))
# 重置
def restart_exam9(self):
    self.open_e9.setChecked(False)
    self.close_e9.setChecked(False)
    self.open_air9.setChecked(False)
    self.close_air9.setChecked(False)
    self.heat19.setChecked(False)
    self.heat29.setChecked(False)
    self.heat39.setChecked(False)
    self.measure_size9.setEnabled(True)
    self.get_gc9.setEnabled(True)
    self.check_weight9.setEnabled(True)
    self.add_water9.setEnabled(True)
    self.put_in9.setEnabled(True)
    self.count_time9.setEnabled(True)
    self.stop_heat9.setEnabled(True)
    self.stop_heat92.setEnabled(True)
    self.wet_thing9.hide()
    self.water_wet_ball9.hide()
    # self.table_exam9.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(4, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(5, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(6, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(7, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(8, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(9, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(10, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(11, 1, QtWidgets.QTableWidgetItem(''))
    # self.table_exam9.setItem(12, 1, QtWidgets.QTableWidgetItem(''))

# 第十章
# 计分点1，启动压缩机
def ban_close_air10(self):
    # 另一个键false
    self.close_air10.setChecked(False)
    # 空气显示
    self.air_1_10.show()
    # # self.table_exam10.setItem(0, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点2，打开进气阀
def ban_close_airin10(self):
    # 另一个键false
    self.close_airin10.setChecked(False)
    # 空气显示
    self.air_2_10.show()
    self.air_3_10.show()
    self.n2_1_10.show()
    self.n2_2_10.show()
    self.o2_1_10.show()
    # 排空阀要关
    # if self.air_pressure_control10.value() != 0:
        # # self.table_exam10.setItem(1, 1, QtWidgets.QTableWidgetItem('错误'))
    # else:
        # # self.table_exam10.setItem(1, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点3，调节放空阀开度，压力示数变化
def ap_change10(self):
    air_open_rate_10 = self.air_pressure_control10.value()
    if air_open_rate_10 == 25:
        self.air_pressure10.setText('0.4')
        # # self.table_exam10.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
    elif air_open_rate_10 == 50:
        self.air_pressure10.setText('0.5')
        # # self.table_exam10.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
    elif air_open_rate_10 == 75:
        self.air_pressure10.setText('0.6')
        # # self.table_exam10.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
    elif air_open_rate_10 == 100:
        self.air_pressure10.setText('MAX')
        # # self.table_exam10.setItem(2, 1, QtWidgets.QTableWidgetItem('完成'))
    else:
        pass
# 计分点4，校正测氧仪
def get_cali(self):
    # 按钮不可用
    self.calibration_10.setEnabled(False)
    # # self.table_exam10.setItem(3, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点5，调节阀12，流量示数变化
def n2_v_change(self):
    n2_open_rate = self.n2_open_rate10.value()
    if self.calibration_10.isEnabled() == False:
        # # self.table_exam10.setItem(4, 1, QtWidgets.QTableWidgetItem('完成'))
        if n2_open_rate == 20:
            self.n2_air_rate10.setText('200')
        elif n2_open_rate == 40:
            self.n2_air_rate10.setText('400')
        elif n2_open_rate == 60:
            self.n2_air_rate10.setText('600')
        elif n2_open_rate == 80:
            self.n2_air_rate10.setText('800')
        elif n2_open_rate == 100:
            self.n2_air_rate10.setText('1000')
        else:
            pass
    else:
        if n2_open_rate == 20:
            self.n2_air_rate10.setText('未校正')
            # # self.table_exam10.setItem(4, 1, QtWidgets.QTableWidgetItem('错误'))
        elif n2_open_rate == 40:
            self.n2_air_rate10.setText('未校正')
            # # self.table_exam10.setItem(4, 1, QtWidgets.QTableWidgetItem('错误'))
        elif n2_open_rate == 60:
            self.n2_air_rate10.setText('未校正')
            # # self.table_exam10.setItem(4, 1, QtWidgets.QTableWidgetItem('错误'))
        elif n2_open_rate == 80:
            self.n2_air_rate10.setText('未校正')
            # # self.table_exam10.setItem(4, 1, QtWidgets.QTableWidgetItem('错误'))
        elif n2_open_rate == 100:
            self.n2_air_rate10.setText('未校正')
            # # self.table_exam10.setItem(4, 1, QtWidgets.QTableWidgetItem('错误'))
        else:
            pass

# 计分点6，测c1，显示c1，c2不显示
def ban_c2_10(self):
    # # self.table_exam10.setItem(5, 1, QtWidgets.QTableWidgetItem('完成'))
    # 气体
    self.n2_3_10.show()
    self.o2_2_10.hide()
    self.o2_3_10.hide()
    # 显示
    # 压力为0.4
    if self.air_pressure10.text() == '0.4':
        if self.n2_air_rate10.text() == '0':
            self.o2contain10.setText('0')
        elif self.n2_air_rate10.text() == '200':
            self.o2contain10.setText('11.6')
        elif self.n2_air_rate10.text() == '400':
            self.o2contain10.setText('12.9')
        elif self.n2_air_rate10.text() == '600':
            self.o2contain10.setText('13.9')
        elif self.n2_air_rate10.text() == '800':
            self.o2contain10.setText('14.4')
        elif self.n2_air_rate10.text() == '1000':
            self.o2contain10.setText('15.0')
    # 压力为0.5
    elif self.air_pressure10.text() == '0.5':
        if self.n2_air_rate10.text() == '0':
            self.o2contain10.setText('0')
        elif self.n2_air_rate10.text() == '200':
            self.o2contain10.setText('10.7')
        elif self.n2_air_rate10.text() == '400':
            self.o2contain10.setText('12.3')
        elif self.n2_air_rate10.text() == '600':
            self.o2contain10.setText('13.3')
        elif self.n2_air_rate10.text() == '800':
            self.o2contain10.setText('13.7')
        elif self.n2_air_rate10.text() == '1000':
            self.o2contain10.setText('14.4')
    # 压力为0.6
    elif self.air_pressure10.text() == '0.6':
        if self.n2_air_rate10.text() == '0':
            self.o2contain10.setText('0')
        elif self.n2_air_rate10.text() == '200':
            self.o2contain10.setText('10.0')
        elif self.n2_air_rate10.text() == '400':
            self.o2contain10.setText('11.6')
        elif self.n2_air_rate10.text() == '600':
            self.o2contain10.setText('12.4')
        elif self.n2_air_rate10.text() == '800':
            self.o2contain10.setText('13.3')
        elif self.n2_air_rate10.text() == '1000':
            self.o2contain10.setText('13.7')
    else:
        pass
# 计分点7，测c2，显示c2，c1不显示
def ban_c1_10(self):
    # # self.table_exam10.setItem(6, 1, QtWidgets.QTableWidgetItem('完成'))
    # 气体
    self.n2_3_10.hide()
    self.o2_2_10.show()
    self.o2_3_10.show()
    # 显示
    # 压力为0.4
    if self.air_pressure10.text() == '0.4':
        if self.n2_air_rate10.text() == '0':
            self.o2contain10.setText('0')
        elif self.n2_air_rate10.text() == '200':
            self.o2contain10.setText('31.7')
        elif self.n2_air_rate10.text() == '400':
            self.o2contain10.setText('32.9')
        elif self.n2_air_rate10.text() == '600':
            self.o2contain10.setText('33.8')
        elif self.n2_air_rate10.text() == '800':
            self.o2contain10.setText('34.2')
        elif self.n2_air_rate10.text() == '1000':
            self.o2contain10.setText('34.7')
    # 压力为0.5
    elif self.air_pressure10.text() == '0.5':
        if self.n2_air_rate10.text() == '0':
            self.o2contain10.setText('0')
        elif self.n2_air_rate10.text() == '200':
            self.o2contain10.setText('31.9')
        elif self.n2_air_rate10.text() == '400':
            self.o2contain10.setText('33.4')
        elif self.n2_air_rate10.text() == '600':
            self.o2contain10.setText('34.2')
        elif self.n2_air_rate10.text() == '800':
            self.o2contain10.setText('34.6')
        elif self.n2_air_rate10.text() == '1000':
            self.o2contain10.setText('35.1')
    # 压力为0.6
    elif self.air_pressure10.text() == '0.6':
        if self.n2_air_rate10.text() == '0':
            self.o2contain10.setText('0')
        elif self.n2_air_rate10.text() == '200':
            self.o2contain10.setText('31.8')
        elif self.n2_air_rate10.text() == '400':
            self.o2contain10.setText('33.4')
        elif self.n2_air_rate10.text() == '600':
            self.o2contain10.setText('34.3')
        elif self.n2_air_rate10.text() == '800':
            self.o2contain10.setText('34.8')
        elif self.n2_air_rate10.text() == '1000':
            self.o2contain10.setText('35.5')
    else:
        pass
# 计分点8，关闭无油空气压缩机
def ban_open_air10(self):
    self.open_air10.setChecked(False)
    # # self.table_exam10.setItem(7, 1, QtWidgets.QTableWidgetItem('完成'))
# 计分点9，全开排空阀，关闭进口阀门
def ban_open_airin10(self):
    self.open_airin10.setChecked(False)
    # if self.air_pressure_control10.value() == 100:
        # # self.table_exam10.setItem(8, 1, QtWidgets.QTableWidgetItem('完成'))
    # else:
        # # self.table_exam10.setItem(8, 1, QtWidgets.QTableWidgetItem('错误'))
# 重置按钮
def restart_exam10(self):
    # # self.table_exam10.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam10.setItem(1, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam10.setItem(2, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam10.setItem(3, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam10.setItem(4, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam10.setItem(5, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam10.setItem(6, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam10.setItem(7, 1, QtWidgets.QTableWidgetItem(''))
    # # self.table_exam10.setItem(8, 1, QtWidgets.QTableWidgetItem(''))
    # 图案不显示
    self.air_1_10.hide()
    self.air_2_10.hide()
    self.air_3_10.hide()
    self.o2_1_10.hide()
    self.o2_2_10.hide()
    self.o2_3_10.hide()
    self.n2_1_10.hide()
    self.n2_2_10.hide()
    self.n2_3_10.hide()
    # 按钮
    self.open_air10.setChecked(False)
    self.close_air10.setChecked(False)
    self.open_airin10.setChecked(False)
    self.close_airin10.setChecked(False)
    self.calibration_10.setEnabled(True)
    self.air_pressure_control10.setValue(0)
    self.air_pressure10.setText('')
    self.n2_air_rate10.setText('')
    self.n2_open_rate10.setValue(0)
    self.o2contain10.setText('')