from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

from tools import simulation_tool
from view.simulation import Ui_Form

class Simulation(QMainWindow, Ui_Form):
    def __init__(self):
        super(Simulation, self).__init__()
        self.setupUi(self)

        # 实验1
        # 原始无水流
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
        # 阀B按钮
        self.open_ink_1.setCheckable(True)
        self.close_ink_1.setCheckable(True)
        # 只能同时按一个
        self.open_ink_1.clicked[bool].connect(lambda checked: simulation_tool.ban_close_ink1(self))
        self.close_ink_1.clicked[bool].connect(lambda checked: simulation_tool.ban_open_ink1(self))
        # 打开阀门C，有水
        self.pump_c_open_rate_1.valueChanged.connect(lambda checked: simulation_tool.show_pattern_1(self))
        # 重置按钮
        self.restart_1.clicked.connect(lambda checked: simulation_tool.restart_exam1(self))

        # 实验2
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
        # 朝向按钮设置
        self.whatever2.setCheckable(True)
        self.front2.setCheckable(True)
        self.vertical2.setCheckable(True)
        self.whatever2.clicked[bool].connect(lambda checked: simulation_tool.whatever_water2(self))
        self.front2.clicked[bool].connect(lambda checked: simulation_tool.front_water2(self))
        self.vertical2.clicked[bool].connect(lambda checked: simulation_tool.vertical_water2(self))
        # 2、3点朝向
        self.front_23_water_2.setCheckable(True)
        self.vertical_23_water_2.setCheckable(True)
        self.front_23_water_2.clicked[bool].connect(lambda checked: simulation_tool.front23_2(self))
        self.vertical_23_water_2.clicked[bool].connect(lambda checked: simulation_tool.vertical23_2(self))
        # 量筒
        self.get_water2.clicked.connect(lambda checked: simulation_tool.get_water_amount_2(self))
        # 计时
        self.count_time2.clicked.connect(lambda checked: simulation_tool.get_the_time_2(self))
        # 重置
        self.restart_2.clicked.connect(lambda checked: simulation_tool.restart_exam2(self))

        # 实验3
        # 进口阀按钮
        self.open_in_3.setCheckable(True)
        self.close_in_3.setCheckable(True)
        # 进口阀只能选择一个
        self.open_in_3.clicked[bool].connect(lambda checked: simulation_tool.ban_close_in_3(self))
        self.close_in_3.clicked[bool].connect(lambda checked: simulation_tool.ban_open_in_3(self))
        # 重置按钮
        self.restart_3.clicked.connect(lambda checked: simulation_tool.restart_exam3(self))
        # 1、加水
        self.water_icon_3.hide()
        self.add_water_b3.clicked.connect(lambda checked: simulation_tool.add_water_box3(self))
        # 2、灌泵
        self.water_icon_4.hide()
        self.add_water_p3.clicked.connect(lambda checked: simulation_tool.add_water_pump3(self))
        # 3、开启离心泵前，关闭出口阀，打开进口阀,灌泵，开泵
        # 管路中没有水
        self.tube_wt1_2.hide()
        self.tube_wt2_2.hide()
        self.tube_wt3_2.hide()
        self.tube_wt4_2.hide()
        self.tube_wt5_2.hide()
        self.tube_wt6_2.hide()
        self.tube_water_3.hide()
        self.tube_water_4.hide()
        # 开泵
        self.pump_on_3.clicked.connect(lambda checked: simulation_tool.open_the_pump3(self))
        # 4、开启出口阀
        self.pump_open_rate_3.valueChanged.connect(lambda checked: simulation_tool.open_out_valve3(self))
        # 5、停泵，停泵前需要关闭出口阀
        self.pump_off_3.clicked.connect(lambda checked: simulation_tool.close_the_pump3(self))

        # 实验4
        # 按钮设置
        # 泵的转速，初始化
        self.pump_2400.setCheckable(True)
        self.pump_2700.setCheckable(True)
        # 泵的转速只能选择一个
        self.pump_2700.clicked[bool].connect(lambda checked: simulation_tool.ban_2400(self))
        self.pump_2400.clicked[bool].connect(lambda checked: simulation_tool.ban_2700(self))
        # 进口阀按钮
        self.open_in_4.setCheckable(True)
        self.close_in_4.setCheckable(True)
        # 进口阀只能选择一个
        self.open_in_4.clicked[bool].connect(lambda checked: simulation_tool.ban_close_in_4(self))
        self.close_in_4.clicked[bool].connect(lambda checked: simulation_tool.ban_open_in_4(self))

        # 1、选择转速
        # 2、加水
        self.water_icon.hide()
        self.add_water_b4.clicked.connect(lambda checked: simulation_tool.add_water_box4(self))
        # 3、灌泵
        self.water_icon_2.hide()
        self.add_water_p4.clicked.connect(lambda checked: simulation_tool.add_water_pump4(self))
        # 4、开启离心泵前，关闭出口阀，打开进口阀,灌泵，开泵
        # 管路中没有水
        self.tube_wt1.hide()
        self.tube_wt2.hide()
        self.tube_wt3.hide()
        self.tube_wt4.hide()
        self.tube_wt5.hide()
        self.tube_wt6.hide()
        self.tube_water_1.hide()
        self.tube_water_2.hide()
        # 开泵
        self.pump_on_4.clicked.connect(lambda checked: simulation_tool.open_the_pump4(self))
        # 5、开启出口阀
        self.pump_open_rate_4.valueChanged.connect(lambda checked: simulation_tool.open_out_valve4(self))
        # 6、停泵，停泵前需要关闭出口阀
        self.pump_off_4.clicked.connect(lambda checked: simulation_tool.close_the_pump4(self))
        # 重置按钮
        self.restart_4.clicked.connect(lambda checked: simulation_tool.restart_exam4(self))

        # 实验5
        # 滤布
        self.soak_filter5.clicked.connect(lambda checked: simulation_tool.soak_the_cloth5(self))
        # 安装
        self.finish5.hide()
        self.equip_5.clicked.connect(lambda checked: simulation_tool.equip_filter5(self))
        # 启动搅拌
        self.dirty5_2.hide()
        self.open_stir5.clicked.connect(lambda checked: simulation_tool.stir5(self))
        # 阀门
        self.dirty5.hide()
        self.open_filter5.clicked.connect(lambda checked: simulation_tool.start_filter5(self))
        # 洗液
        self.water5.hide()
        self.open_wash5.clicked.connect(lambda checked: simulation_tool.start_wash5(self))
        # 空气
        self.open_air5.clicked.connect(lambda checked: simulation_tool.get_air_5(self))
        # 压力
        self.adjust_air5.clicked.connect(lambda checked: simulation_tool.adjust_ap5(self))
        # 量筒
        self.water_cup5.hide()
        self.get_water5.clicked.connect(lambda checked: simulation_tool.get_the_water5(self))
        # 计时
        self.count_time5.clicked.connect(lambda checked: simulation_tool.count_the_time5(self))
        # 重置
        self.restart_5.clicked.connect(lambda checked: simulation_tool.restart_exam5(self))

        # 实验6
        self.cold_air.hide()
        self.gas_1.hide()
        self.gas_2.hide()
        # 加热器按钮设置
        self.open_heat_6.setCheckable(True)
        self.close_heat_6.setCheckable(True)
        self.open_heat_6.clicked[bool].connect(lambda checked: simulation_tool.ban_close_heat_6(self))
        self.close_heat_6.clicked[bool].connect(lambda checked: simulation_tool.ban_open_heat_6(self))

        # 加热蒸汽阀门按钮设置
        self.open_gas_6.setCheckable(True)
        self.close_gas_6.setCheckable(True)
        self.open_gas_6.clicked[bool].connect(lambda checked: simulation_tool.ban_close_gas_6(self))
        self.close_gas_6.clicked[bool].connect(lambda checked: simulation_tool.ban_open_gas_6(self))

        # 鼓风机按钮设置
        self.open_air_6.setCheckable(True)
        self.close_air_6.setCheckable(True)
        self.open_air_6.clicked[bool].connect(lambda checked: simulation_tool.ban_close_air_6(self))
        self.close_air_6.clicked[bool].connect(lambda checked: simulation_tool.ban_open_air_6(self))
        # 调节阀门
        self.open_air_rate_6.valueChanged.connect(lambda checked: simulation_tool.show_data_6(self))
        # 重置按钮
        self.restart_6.clicked.connect(lambda checked: simulation_tool.restart_exam6(self))

        # 实验7
        # 按钮设置
        # 电源
        self.open_e_7.setCheckable(True)
        self.close_e_7.setCheckable(True)
        self.open_e_7.clicked[bool].connect(lambda checked: simulation_tool.ban_closee7(self))
        self.close_e_7.clicked[bool].connect(lambda checked: simulation_tool.ban_opene7(self))
        # 进料泵
        self.open_in_pump_7.setCheckable(True)
        self.close_in_pump_7.setCheckable(True)
        self.open_in_pump_7.clicked[bool].connect(lambda checked: simulation_tool.ban_close_inpump7(self))
        self.close_in_pump_7.clicked[bool].connect(lambda checked: simulation_tool.ban_open_inpump7(self))
        # 电加热器
        self.open_heat7.setCheckable(True)
        self.close_heat7.setCheckable(True)
        self.open_heat7.clicked[bool].connect(lambda checked: simulation_tool.ban_close_heat7(self))
        self.close_heat7.clicked[bool].connect(lambda checked: simulation_tool.ban_open_heat7(self))
        # 产品阀
        self.open_d_7.setCheckable(True)
        self.close_d_7.setCheckable(True)
        self.close_d_7.clicked[bool].connect(lambda checked: simulation_tool.ban_open_d7(self))
        self.open_d_7.clicked[bool].connect(lambda checked: simulation_tool.ban_close_d7(self))
        # 冷却水阀
        self.open_cold_water7.setCheckable(True)
        self.close_cold_water7.setCheckable(True)
        self.open_cold_water7.clicked[bool].connect(lambda checked: simulation_tool.ban_close_cold7(self))
        self.close_cold_water7.clicked[bool].connect(lambda checked: simulation_tool.ban_open_cold7(self))
        # 釜液阀
        self.adjust_w7.clicked.connect(lambda checked: simulation_tool.adjust_the_w7(self))
        # 两个取样
        self.get_d7.clicked.connect(lambda checked: simulation_tool.get_d_7(self))
        self.get_w7.clicked.connect(lambda checked: simulation_tool.get_w_7(self))
        # 重置按钮
        self.restart_7.clicked.connect(lambda checked: simulation_tool.restart_exam7(self))

        # 实验8
        # 水泵
        self.open_pump8.clicked.connect(lambda checked: simulation_tool.open_water8(self))
        # 水流量
        self.adjust_water8big.setCheckable(True)
        self.adjust_water8small.setCheckable(True)
        self.adjust_water8big.clicked[bool].connect(lambda checked: simulation_tool.big_water8(self))
        self.adjust_water8small.clicked[bool].connect(lambda checked: simulation_tool.small_water8(self))
        # 打开风机
        self.open_air8.clicked.connect(lambda checked: simulation_tool.open_the_air8(self))
        # 空气阀门
        self.adjust_air8.clicked.connect(lambda checked: simulation_tool.adjust_the_air8(self))
        # co2阀门
        self.adjust_co28.clicked.connect(lambda checked: simulation_tool.adjust_the_co28(self))
        # 记录数据
        self.note8.clicked.connect(lambda checked: simulation_tool.note_down8(self))
        # 打开尾气阀/进气阀
        self.open_rest8.setCheckable(True)
        self.open_in8.setCheckable(True)
        self.open_rest8.clicked[bool].connect(lambda checked: simulation_tool.check_rest8(self))
        self.open_in8.clicked[bool].connect(lambda checked: simulation_tool.check_in8(self))
        # 重置
        self.restart_8.clicked.connect(lambda checked: simulation_tool.restart_exam8(self))

        # 实验9
        # 按钮设置
        # 总电源
        self.open_e9.setCheckable(True)
        self.close_e9.setCheckable(True)
        self.open_e9.clicked[bool].connect(lambda checked: simulation_tool.ban_close_e9(self))
        self.close_e9.clicked[bool].connect(lambda checked: simulation_tool.ban_open_e9(self))
        # 加热器
        self.heat19.setCheckable(True)
        self.heat29.setCheckable(True)
        self.heat39.setCheckable(True)
        self.heat39.clicked[bool].connect(lambda checked: simulation_tool.check_heat9(self))
        # 鼓风机
        self.open_air9.setCheckable(True)
        self.close_air9.setCheckable(True)
        self.open_air9.clicked[bool].connect(lambda checked: simulation_tool.ban_close_air9(self))
        self.close_air9.clicked[bool].connect(lambda checked: simulation_tool.ban_open_air9(self))
        # 测量物料尺寸
        self.measure_size9.clicked.connect(lambda checked: simulation_tool.measure_dry9(self))
        # 称量物料
        self.get_gc9.clicked.connect(lambda checked: simulation_tool.get_the_gc9(self))
        # 检查天平
        self.check_weight9.clicked.connect(lambda checked: simulation_tool.check_the_weight9(self))
        # 加水
        self.water_wet_ball9.hide()
        self.add_water9.clicked.connect(lambda checked: simulation_tool.add_water_wet_ball9(self))
        # 放入物料
        self.wet_thing9.hide()
        self.put_in9.clicked.connect(lambda checked: simulation_tool.show_thing9(self))
        # 记录时间
        self.count_time9.clicked.connect(lambda checked: simulation_tool.count_the_time9(self))
        # 停止加热2
        self.stop_heat92.clicked.connect(lambda checked: simulation_tool.stop_heat_92(self))
        # 停止加热
        self.stop_heat9.clicked.connect(lambda checked: simulation_tool.stop_the_heat9(self))
        # 重置
        self.restart_9.clicked.connect(lambda checked: simulation_tool.restart_exam9(self))

        # 实验10
        # 背景图片
        self.bg104.setPixmap(QtGui.QPixmap('素材/实验图模拟用/10s.png'))
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
        # 压缩机按钮设置
        self.open_air10.setCheckable(True)
        self.close_air10.setCheckable(True)
        self.open_air10.clicked[bool].connect(lambda checked: simulation_tool.ban_close_air10(self))
        self.close_air10.clicked[bool].connect(lambda checked: simulation_tool.ban_open_air10(self))
        # 进气阀设置
        self.open_airin10.setCheckable(True)
        self.close_airin10.setCheckable(True)
        self.open_airin10.clicked[bool].connect(lambda checked: simulation_tool.ban_close_airin10(self))
        self.close_airin10.clicked[bool].connect(lambda checked: simulation_tool.ban_open_airin10(self))
        # 放空阀设置
        self.air_pressure_control10.valueChanged.connect(lambda checked: simulation_tool.ap_change10(self))
        # 测氧仪
        self.calibration_10.clicked.connect(lambda checked: simulation_tool.get_cali(self))
        # n2阀门
        self.n2_open_rate10.valueChanged.connect(lambda checked: simulation_tool.n2_v_change(self))
        # 测C1/C2
        self.get_c1_10.clicked.connect(lambda checked: simulation_tool.ban_c2_10(self))
        self.get_c2_10.clicked.connect(lambda checked: simulation_tool.ban_c1_10(self))
        # 重置
        self.restart_10.clicked.connect(lambda checked: simulation_tool.restart_exam10(self))

