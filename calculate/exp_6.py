from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

# 实验六数据处理
def calculate_data_6(self):
    try:
        # 获取基本参数:
        # 大气压
        P_0 = float(self.p6.text())
        # 管内径
        d = float(self.d6.text())
        # 管长
        l = float(self.l6.text())
        # # 密度
        # rou = float(self.rou6.text())
        # 空气粘度
        miu = float(self.miu6.text())
        # 比热容
        C = float(self.C6.text())
        # 空气传热系数
        l_d = float(self.lambda_6.text())

        # 流量
        Q = []
        # 空气计前表压
        P_f = []
        # 空气进口温度
        t1 = []
        # 空气出口温度
        t2 = []
        # 蒸汽温度
        T = []
        # 空气密度
        rou = []
        # 传热平均温差
        delta_tm = []
        # 总传热系数
        K = []
        # 雷诺数
        Re = []
        # 努塞尔准数
        Nu = []

        for i in range(0, 7):
            # 获取流量
            Q.append(float(self.exp_data_6a.item(i, 0).text()))
            # 获取空气计前表压
            P_f.append(float(self.exp_data_6a.item(i, 1).text()))
            # 获取空气进口温度
            t1.append(float(self.exp_data_6a.item(i, 2).text()))
            # 获取空气出口温度
            t2.append(float(self.exp_data_6a.item(i, 3).text()))
            # 获取蒸汽温度
            T.append(float(self.exp_data_6a.item(i, 4).text()))

            # 计算空气密度
            rou_i = round(1.293 * (P_0+P_f[i])/101.33 * 273/(273+t1[i]), 2)
            rou.append(rou_i)
            # 计算delta_tm
            delta_tm_i = round(np.divide( (T[i]-t2[i]) - (T[i]-t1[i]) , np.log((T[i]-t2[i])/(T[i]-t1[i]))) , 2)
            delta_tm.append(delta_tm_i)
            # 计算K
            K_i = round(Q[i]/3600*rou[i]*C*(t2[i]-t1[i])/(np.pi*d/1000*l)/delta_tm[i], 2)
            K.append(K_i)
            # 计算Re
            Re_i = round(d/1000 * (Q[i] * 4 / 3600 / np.pi / (d/1000)**2) * rou[i] / miu , 2)
            Re.append(Re_i)
            # 计算Nu
            Nu_i = round(K[i] * d/1000 / l_d, 2)
            Nu.append(Nu_i)
            # 加载数据
            self.exp_data_6b.setItem(i, 0, QtWidgets.QTableWidgetItem(str(Q[i])))
            self.exp_data_6b.setItem(i, 1, QtWidgets.QTableWidgetItem(str(K[i])))
            self.exp_data_6b.setItem(i, 2, QtWidgets.QTableWidgetItem(str(Re[i])))
            self.exp_data_6b.setItem(i, 3, QtWidgets.QTableWidgetItem(str(Nu[i])))


    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)

# 作图Nu~Re
def get_pic_6(self):
    Q = []
    Re = []
    Nu = []
    for i in range(0, 7):
        # # 获取流量
        # Q.append(float(self.exp_data_6b.item(i, 0).text()))
        # 获取Re
        Re.append(float(self.exp_data_6b.item(i, 2).text()))
        # 获取Nu
        Nu.append(float(self.exp_data_6b.item(i, 3).text()))

    # 取对数
    logRe = np.log(Re)
    logNu = np.log(Nu)

    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 中文字体显示
    plt.rcParams.update({"font.size": 10})  # 此处必须添加此句代码方可改变标题字体大小

    # 画布
    figure = plt.figure()
    canvas = FigureCanvas(figure)
    g = QtWidgets.QGraphicsScene()
    g.addWidget(canvas)
    figure.set_tight_layout

    # 公式
    # 一次线性方程
    z = np.polyfit(logRe, logNu, 1)
    p = np.poly1d(z)
    # 代公式
    yvals = p(logRe)
    # 相关系数R2
    r2 = round(r2_score(logNu, yvals), 4)
    # 完整公式
    text = 'y=' + str(p).strip() + '\n' + "R\u00b2=" + str(r2).strip()
    # 显示公式
    plt.text(np.average(logRe), (np.average(logNu)), text, size=12, family="Times new roman", color="black",
             style='italic', weight='light')

    # 画图
    feature_6 = figure.subplots(1, 1)
    feature_6.plot(logRe, logNu, 's', label="original values")
    feature_6.set_title('Nu~Re曲线')
    feature_6.set_ylabel('logNu', fontsize=10)
    feature_6.set_xlabel('logRe', fontsize=10)
    feature_6.plot(logRe, yvals, 'r', label="polyfit values")
    feature_6.legend()

    canvas.draw()
    plt.show()