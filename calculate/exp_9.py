import os.path
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from matplotlib import pyplot as plt
import numpy as np
from docx import Document

from function.report_9 import write_9_docx


def data_processing_9_data_calculate_click(self):
    QMessageBox.information(self, '提示', '正在计算中,请稍等~~~', QMessageBox.Ok)
    date = self.data_processing_9_date.text()
    bgtemp = self.data_processing_9_data_bgtemp.text()
    fgtemp = self.data_processing_9_data_fgtemp.text()
    flow = self.data_processing_9_data_flow.text()
    fstemp = self.data_processing_9_data_fstemp.text()
    pressure = self.data_processing_9_data_pressure.text()
    size = self.data_processing_9_data_size.text()
    weight_str = self.data_processing_9_data_weight.text()
    weight = float(weight_str)
    area = 0.0361
    table = self.data_processing_9_table
    av_x_rate = 0.0
    steam = 0.0
    u = 0.0
    # 保存表格中的数据
    data = [[], [], [], [], [], []]
    item = QTableWidgetItem()
    if (date == ''
            or bgtemp == ''
            or fgtemp == ''
            or flow == ''
            or fstemp == ''
            or pressure == ''
            or size == ''
            or weight == ''):
        QMessageBox.information(self, '提示', '请填写所有完整信息~~~', QMessageBox.Ok)

        return
    # 遍历保存表格中的数据到一个二维数组中
    # 并且填写需要计算出来的表格
    for j in range(int(table.rowCount())):
        # 获取湿物料质量数据并且计算湿物料含水量填入表中
        if table.item(j, 0) is not None:
            data[0].append(float(table.item(j, 0).data(0)))
            x_rate = (float(table.item(j, 0).data(0)) - weight) / weight
            data[1].append(x_rate)
            item = QTableWidgetItem()
            item.setText(str(x_rate))
            table.setItem(j, 1, item)
        #  获取时间间隔
        if table.item(j, 4) is not None and table.item(j, 4).data(0) is not None:
            data[4].append(float(table.item(j, 4).data(0)))

    # 计算数据
    data[1].append(data[1][-1])
    data[0].append(data[0][-1])
    for j in range(len(data[4])):
        av_x_rate = (data[1][j] + data[1][j + 1]) / 2
        data[2].append(av_x_rate)
        steam = data[0][j] - data[0][j + 1]
        data[3].append(steam)
        u = data[3][j] / 1000 / 0.0361 / data[4][j]
        data[5].append(u)

    # 将数据填入表格中
    j = 0
    for i in range(table.rowCount()):
        if table.item(i, 4) is not None and table.item(i, 4).data(0) is not None:
            item = QTableWidgetItem()
            item.setText(str(data[2][j]))
            table.setItem(i, 2, item)
            item = QTableWidgetItem()
            item.setText(str(data[3][j]))
            table.setItem(i, 3, item)
            item = QTableWidgetItem()
            item.setText(str(data[5][j]))
            table.setItem(i, 5, item)
            j += 1

    # 做出恒定干燥条件下的干燥曲线
    plt.figure(1)
    plt.plot(data[4], data[1][0:-2], color='r', marker='o')
    plt.xlabel('干燥时间t/h')
    plt.ylabel('X/kg水/kg绝干物料')
    plt.title('X-t curve')
    plt.savefig('./data/img/exp_9_data_1.png')
    img = os.path.abspath('./data/img/exp_9_data_1.png')
    image = QtGui.QPixmap(img).scaled(11182, 1182)
    self.data_processing_9_data_pic_1.setScaledContents(True)
    self.data_processing_9_data_pic_1.setPixmap(image)
    # 斜率
    xt = np.diff(data[1][0:-2]) / np.diff(data[4])
    U = []
    # 计算出干燥速率
    for i in xt:
        U.append(-1 * weight * i / area)
    plt.figure(2)
    plt.plot(data[1][:-3], U, color='r', marker='o')
    plt.xlabel('干基含水率')
    plt.ylabel('干燥速率U/kg/(${m^3}$·h)')
    plt.title('U-X curve')
    plt.savefig('./data/img/exp_9_data_2.png')
    img = os.path.abspath('./data/img/exp_9_data_2.png')
    image = QtGui.QPixmap(img).scaled(11182, 1182)
    self.data_processing_9_data_pic_2.setScaledContents(True)
    self.data_processing_9_data_pic_2.setPixmap(image)

    # 创建一个问答框
    self.box = QMessageBox(QMessageBox.Question, '提示', '计算完成,是否要生成实验报告?')

    # 添加按钮
    yes = self.box.addButton('确定', QMessageBox.YesRole)
    no = self.box.addButton('取消', QMessageBox.NoRole)

    # 显示该问答框
    self.box.exec_()
    if self.box.clickedButton() == yes:
        write_9_docx(self, data, date, bgtemp, fgtemp, flow, fstemp, pressure, size, weight, area)
