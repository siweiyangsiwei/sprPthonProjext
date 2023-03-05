import math
import os

from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtGui
import matplotlib.pyplot as plt


def data_processing_8_data_calculate_click(self):
    if (self.data_processing_8_date == ''
            or self.data_processing_8_data_height == ''
            or self.data_processing_8_data_diameter == ''
            or self.data_processing_8_data_specification == ''
            or self.data_processing_8_data_pressure == ''
            or self.data_processing_8_data_temp == ''
            or self.data_processing_8_data_T == ''
            or self.data_processing_8_data_P == ''):
        print("请填写完整的信息")
        return
    # 实验日期
    date = self.data_processing_8_date.text()
    # 填料层高度
    height_str = self.data_processing_8_data_height.text()
    height = float(self.data_processing_8_data_height.text())
    # 塔内径
    diameter_str = self.data_processing_8_data_diameter.text()
    diameter = float(self.data_processing_8_data_diameter.text())
    # 填料规格
    specification = self.data_processing_8_data_specification.text()
    # 大气压
    pressure_str = self.data_processing_8_data_pressure.text()
    pressure = float(self.data_processing_8_data_pressure.text())
    # 室温
    temp_str = self.data_processing_8_data_temp.text()
    temp = float(self.data_processing_8_data_temp.text())
    # 流量计标定状态
    T = self.data_processing_8_data_T.text()
    P = self.data_processing_8_data_P.text()
    # 记录填料塔流体力学性能
    data = []
    table = None
    # 没有选择,填料为干料
    if not self.data_processing_8_data_type.isChecked():
        table = self.data_processing_8_table_1
        for i in range(table.rowCount()):
            data.append([])
            for j in range(table.columnCount()):
                if table.item(i, j) is None:
                    if j == 1:
                        item = QTableWidgetItem()
                        item.setText(str(data[i][0] / height))
                        table.setItem(i, j, item)
                        data[i].append(float(table.item(i, j).data(0)))
                    else:
                        print("请先填写好表中的数据")
                        return
                else:
                    data[i].append(float(table.item(i, j).data(0)))
    # 填料为湿料
    else:
        table = self.data_processing_8_table_2
        for i in range(table.rowCount()):
            for j in range(table.columnCount() - 1):
                if table.item(i, j) is None:
                    if j == 1:
                        item = QTableWidgetItem()
                        item.setText(str(data[i][0] / height))
                        table.setItem(i, j, item)
                        data[i].append(float(table.item(i, j).data(0)))
                    else:
                        print("请先填写好表中的数据")
                        return
                else:
                    data[i].append(float(table.item(i, j).data(0)))
    # 获取到数据了,开始进行塔的流体力学性能计算
    # 计算V0标准状态下空气流量的计算 以及 空塔气速的计算
    V0 = []
    u = []
    # 获得一个压强降数组
    deter_pressure = []
    for i in range(table.rowCount()):
        V = data[i][2] * 273.15 / 101.32 * math.sqrt(101.32 * data[i][3] / (273.15 + 20) / (273.15 + data[i][4]))
        u1 = 4 * V / math.pi / height.__pow__(2)
        V0.append(V)
        u.append(u1)
        deter_pressure.append(data[i][1])

    # 绘制不同喷淋量下填料层的压强降与气速的关系
    plt.plot(u, deter_pressure, color='r')
    plt.xlabel('u')
    plt.ylabel('△p')
    plt.title('△P/Z-u curve')
    plt.savefig('./data/img/exp_8_data_1.png')
    img = os.path.abspath('./data/img/exp_8_data_1.png')
    image = QtGui.QPixmap(img).scaled(11182, 1182)
    self.data_processing_8_data_pic_1.setScaledContents(True)
    self.data_processing_8_data_pic_1.setPixmap(image)

    table = self.data_processing_8_table_3
    # 用于保存表3的数据
    data3 = [[], []]
    # 进行CO2传质性能测试数据计算
    for i in range(table.rowCount()):
        for j in range(2):
            if table.item(i, j) is None:
                print("请填写好数据再进行计算")
                return
            else:
                data3[j].append(float(table.item(i, j).data(0)))

    # 对于表2进行表3的数据计算
    # 用于保存表4的计算数据(浮点数类型)
    data4 = [[], []]
    for i in range(2):
        data4[i].append(data3[i][0])
        # CO2体积流量
        Vco2 = data3[i][1] * data3[i][7]
        # 计算标准状态下CO2的体积流量
        Vco20 = Vco2 * 273.15 / 101.32 * math.sqrt(
            1.293 / 1.977 * 101.32 * data3[i][3] / (273.15 + 20) / (data3[i][2] + 273.15))
        data4[i].append(Vco20)
        # 空气体积流量
        Vspace = data3[i][1] * (1 - data3[i][7])
        # 标准状态下空气的体积流量
        Vspace0 = Vspace * 273.15 / 101.32 * math.sqrt(
            101.32 * data3[i][3] / (273.15 + 20) / (273.15 + data3[i][2]))
        data4[i].append(Vspace0)
        # 计算空气摩尔流量
        Vmol = Vspace / 22.4 / 1000 / diameter.__pow__(2)
        data4[i].append(Vmol)
        # 计算水摩尔流量
        Lmol = data3[i][0] / 1000 * 1 / diameter.__pow__(2)
        data4[i].append(Lmol)
        # 计算相平衡常数
        m = data3[i][6] / data3[i][3]
        data4[i].append(m)
        # 计算吸收因数
        A = Lmol / m / Vmol
        # 计算X2
        X2 = Vmol * (data3[i][7] - data3[i][8]) / Lmol
        # 计算N(OL)
        NOL = 1 / (1 - A) * math.log(((1 - A) * (data3[i][7] - m * X2 / data3[i][7])), math.e)
        data4[i].append(NOL)
        # 计算H(OL)
        HOL = height / NOL
        data4[i].append(HOL)
        # 计算Kxa
        Kxa = Lmol / HOL / (0.25 * diameter.__pow__(2) * math.pi)
        data4[i].append(Kxa)
        # 计算吸收率
        rate = (data3[i][7] - data3[i][8]) / data3[i][7]
        data4[i].append(rate)
    # 转换为字符串后填入到表4中
    table = self.data_processing_8_table_4
    for i in range(table.rowCount()):
        for j in range(table.columnCount()):
            item = QTableWidgetItem()
            item.setText(str(data4[j][i]))
            table.setItem(i, j, item)
