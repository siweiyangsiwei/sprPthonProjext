from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

# 实验四数据处理
def calculate_data_4(self):
    try:
        # 获取基本参数: 流体密度
        rou = float(self.rou4.text())

        # 压差
        d_P = []
        # 流量
        Q = []
        # 电功率显示值
        P = []
        # 转速
        n = []
        # 扬程
        H = []
        # 轴功率
        N = []
        # 泵效率
        Efficiency = []

        for i in range(0, 10):
            # 获取压差
            d_P.append(float(self.exp_data_4a.item(i, 1).text()) - float(self.exp_data_4a.item(i, 0).text()))
            # 获取流量
            Q.append(float(self.exp_data_4a.item(i, 2).text()))
            # 获取功率
            P.append(float(self.exp_data_4a.item(i, 1).text()))
            # 获取转速
            n.append(float(self.exp_data_4a.item(i, 1).text()))

            # 计算扬程
            H_i = round(0.23 + (d_P[i]*10**6 * (n[0]/n[i])) / rou / 9.81 , 2)
            H.append(H_i)
            # 计算轴功率
            N_i = round(P[i] * 0.95 * (n[0]/n[i]), 2)
            N.append(N_i)
            # 计算泵效率
            Efficiency_i = round(H[i] * (Q[i]/3600) * rou * 9.81 / (N[i]*1000 * (n[0]/n[i])) * 100, 2)
            Efficiency.append(Efficiency_i)
            # 加载数据
            self.exp_data_4b.setItem(i, 0, QtWidgets.QTableWidgetItem(str(Q[i])))
            self.exp_data_4b.setItem(i, 1, QtWidgets.QTableWidgetItem(str(H[i])))
            self.exp_data_4b.setItem(i, 2, QtWidgets.QTableWidgetItem(str(N[i])))
            self.exp_data_4b.setItem(i, 3, QtWidgets.QTableWidgetItem(str(Efficiency[i])))


    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)

# 作图
def get_pic_4(self):
    Q = []
    H = []
    N = []
    Efficiency = []
    for i in range(0, 10):
        # 获取流量
        Q.append(float(self.exp_data_4b.item(i, 0).text()))
        # 获取扬程
        H.append(float(self.exp_data_4b.item(i, 1).text()))
        # 获取轴功率
        N.append(float(self.exp_data_4b.item(i, 2).text()))
        # 获取泵效率
        Efficiency.append(float(self.exp_data_4b.item(i, 3).text()))

    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 中文字体显示
    plt.rcParams.update({"font.size": 10})  # 此处必须添加此句代码方可改变标题字体大小

    # 画布
    figure = plt.figure()
    canvas = FigureCanvas(figure)
    g = QtWidgets.QGraphicsScene()
    g.addWidget(canvas)
    figure.set_tight_layout


    # 画图
    feature_4 = figure.subplots(1, 1)
    feature_4.plot(Q, H, label='扬程-流量(H~Q)')
    feature_4.plot(Q, N, label='功率-流量(N~Q)')
    feature_4.plot(Q, Efficiency, label='效率-流量(η~Q)')
    # feature_4.set_title('%d转下离心泵特性曲线' % n)
    feature_4.set_title('离心泵特性曲线')
    feature_4.set_ylabel('H/N/η', fontsize=10)
    feature_4.set_xlabel('流量Q(m^3/s)', fontsize=10)
    feature_4.legend()
    canvas.draw()
    plt.show()

    # # 公式
    # # 一次线性方程
    # z = np.polyfit(Re, ld, 1)
    # p = np.poly1d(z)
    # # 代公式
    # yvals = p(Re)
    # # 相关系数R2
    # r2 = round(r2_score(Re,yvals),3)
    # # 完整公式，但是没有找到将x、y改成Re、λ的方法
    # text='y='+ str(p).strip() +'\n'+ "R\u00b2=" + str(r2).strip()
    # # 显示公式
    # plt.text(np.average(logRe),(np.average(logLd)),text,size=12,family="Times new roman",color="black",style='italic',weight='light')
    #
    # canvas.draw()
    # plt.show()