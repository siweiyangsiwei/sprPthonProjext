from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

# 实验三
# 光滑管
def calculate_data_3a(self):
    try:
        # 获取基本参数: 管径、管长、转速、温度、流体密度、流体粘度
        d = float(self.d3.text())
        l = float(self.l3.text())
        rou = float(self.rou3.text())
        miu = float(self.miu3.text())

        # 流量
        Q = []
        # 压差
        dP = []
        # 雷诺数
        Re = []
        # 摩擦系数
        ld = []

        for i in range(0,10):
            # 获取流量
            Q.append(float(self.exp_data_3a.item(i,0).text()))
            # 获取压差
            dP.append(float(self.exp_data_3a.item(i,1).text()))
            # 计算雷诺数
            Re_i = round(4 * Q[i] * rou / 3600 / 3.1415 / (d/1000) / miu, 2)
            Re.append(Re_i)
            # 计算摩擦系数
            ld_i = round(2 * (d/1000) * (dP[i]*1000) / rou / l / (4*Q[i]/3600/3.1415/(d/1000)**2) , 4)
            ld.append(ld_i)
            # 加载数据
            self.exp_data_3a.setItem(i, 2, QtWidgets.QTableWidgetItem(str(Re[i])))
            self.exp_data_3a.setItem(i, 3, QtWidgets.QTableWidgetItem(str(ld[i])))
    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)

# 粗糙管
def calculate_data_3b(self):
    try:
        # 获取基本参数: 管径、管长、转速、温度、流体密度、流体粘度
        d = float(self.d3.text())
        l = float(self.l3.text())
        rou = float(self.rou3.text())
        miu = float(self.miu3.text())

        Q = []
        dP = []
        Re = []
        ld = []

        for i in range(0,10):
            # 获取流量
            Q.append(float(self.exp_data_3b.item(i, 0).text()))
            # 获取压差
            dP.append(float(self.exp_data_3b.item(i, 1).text()))
            # 计算雷诺数
            Re_i = round(4 * Q[i] * rou / 3600 / 3.1415 / (d / 1000) / miu, 2)
            Re.append(Re_i)
            # 计算摩擦系数
            ld_i = round(2 * (d / 1000) * (dP[i] * 1000) / rou / l / (4 * Q[i] / 3600 / 3.1415 / (d / 1000) ** 2), 4)
            ld.append(ld_i)
            # 加载数据
            self.exp_data_3b.setItem(i, 2, QtWidgets.QTableWidgetItem(str(Re[i])))
            self.exp_data_3b.setItem(i, 3, QtWidgets.QTableWidgetItem(str(ld[i])))
    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)

# 阀门局部阻力系数
def calculate_data_3c(self):
    try:
        # 获取基本参数: 管径、管长、转速、温度、流体密度、流体粘度
        d = float(self.d3.text())
        rou = float(self.rou3.text())

        Q = []
        dP = []
        k = []

        for i in range(0,10):
            # 获取流量
            Q.append(float(self.exp_data_3b.item(2,i).text()))
            # 获取压差
            dP.append(float(self.exp_data_3b.item(3,i).text()))
            # 计算局部阻力系数
            k_i = round(2 * dP[i] / rou / (4*Q[i]/3600/3.1415/(d/1000)**2), 2)
            k.append(k_i)
            # 加载数据
            self.exp_data_3c.setItem(4, i, QtWidgets.QTableWidgetItem(str(k[i])))
    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)

# 作图
def get_pic_3a(self):
    Re = []
    ld = []
    logRe = []
    logLd = []
    for i in range(0, 10):
        # 获取雷诺数
        Re.append(float(self.exp_data_3a.item(i, 2).text()))
        # 获取局部阻力系数
        ld.append(float(self.exp_data_3a.item(i, 3).text()))
        # 取对数
        logRe.append(np.log(Re[i]))
        logLd.append(np.log(ld[i]))

    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 中文字体显示
    plt.rcParams.update({"font.size": 10})  # 此处必须添加此句代码方可改变标题字体大小
    # plt.tick_params(labelsize=10)

    # 画布
    figure = plt.figure()
    canvas = FigureCanvas(figure)
    g = QtWidgets.QGraphicsScene()
    g.addWidget(canvas)
    figure.set_tight_layout

    # self.lumbda_re = self.figure3.subplots(1, 1)
    # self.lumbda_re.plot(logRe, logLd)
    # self.lumbda_re.set_title('λ-Re', fontsize=10)
    # self.lumbda_re.set_ylabel('ln(λ)', fontsize=10)
    # self.lumbda_re.set_xlabel('ln(Re)', fontsize=10)
    # canvas = FigureCanvasQTAgg(self.figure3)
    # canvas.draw()
    # g = QtWidgets.QGraphicsScene()
    # g.addWidget(canvas)
    # self.gr.show()

    # 字体刻度设置

    # 画图
    lumbda_re = figure.subplots(1, 1)
    lumbda_re.plot(logRe, logLd)
    lumbda_re.set_title('λ-Re', fontsize=10)
    lumbda_re.set_ylabel('ln(λ)', fontsize=10)
    lumbda_re.set_xlabel('ln(Re)', fontsize=10)
    canvas.draw()
    plt.show()
        # self.figure3.savefig('image/实验3.png')


        
def reset_pic_3a(self):
    self.exp_data_3a.clearContents()
    
def reset_pic_3b(self):
    self.exp_data_3b.clearContents()
    
def reset_pic_3c(self):
    self.exp_data_3c.clearContents()