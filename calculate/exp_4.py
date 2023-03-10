from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes

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
            P.append(float(self.exp_data_4a.item(i, 3).text()))
            # 获取转速
            n.append(float(self.exp_data_4a.item(i, 4).text()))

            # 计算扬程
            H_i = round((0.23 + (d_P[i]*10**3 ) / rou / 9.81) * (n[0]/n[i]), 2)
            H.append(H_i)
            # 计算轴功率
            N_i = round(P[i] * 0.95 * (n[0]/n[i]), 2)
            N.append(N_i)
            # 计算泵效率
            Efficiency_i = round(H[i] * (Q[i]/3600) * rou * 9.81 / N[i] * 100, 2)
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
    try:
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

        fig = plt.figure(1)

        host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
        par1 = ParasiteAxes(host, sharex=host)
        par2 = ParasiteAxes(host, sharex=host)
        host.parasites.append(par1)
        host.parasites.append(par2)

        host.set_ylabel('H(m)')
        host.set_xlabel('Q(m3/h)')

        host.axis['right'].set_visible(False)
        par1.axis['right'].set_visible(True)
        par1.set_ylabel('N(W)')

        par1.axis['right'].major_ticklabels.set_visible(True)
        par1.axis['right'].label.set_visible(True)

        par2.set_ylabel('η(%)')
        offset = (60, 0)
        new_axisline = par2._grid_helper.new_fixed_axis  # "_grid_helper"与"get_grid_helper()"等价，可以代替
        par2.axis['right2'] = new_axisline(loc='right', axes=par2, offset=offset)

        fig.add_axes(host)

        p1, = host.plot(Q, H, label="H~Q")
        p2, = par1.plot(Q, N, label="N~Q")
        p3, = par2.plot(Q,Efficiency, label="η~Q")
        host.set_title('离心泵特性曲线')
        host.legend()
        # 轴名称，刻度值的颜色
        host.axis['left'].label.set_color(p1.get_color())
        par1.axis['right'].label.set_color(p2.get_color())
        par2.axis['right2'].label.set_color(p3.get_color())
        par2.axis['right2'].major_ticklabels.set_color(p3.get_color())  # 刻度值颜色
        par2.axis['right2'].set_axisline_style('-|>', size=1.5)  # 轴的形状色
        par2.axis['right2'].line.set_color(p3.get_color())  # 轴的颜色

        plt.show()
        plt.savefig('./data/img/exp_4_data.png')
    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)
