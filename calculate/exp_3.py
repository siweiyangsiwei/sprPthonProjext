from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes


# 实验三数据处理
# 光滑管
def calculate_data_3a(self):
    try:
        # 获取基本参数: 管径、管长、流体密度、流体粘度
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
    # try:
        # 获取基本参数: 管径、管长、流体密度、流体粘度
        d = float(self.d3.text())
        rou = float(self.rou3.text())

        Q = []
        dP = []
        k = []

        for i in range(0,5):
            # 获取流量
            Q.append(float(self.exp_data_3c.item(1,i).text()))
            # 获取压差
            dP.append(float(self.exp_data_3c.item(2,i).text()))
            # 计算局部阻力系数
            k_i = round(2 * dP[i] * 1000 / rou / (4*Q[i]/3600/3.1415/(d/1000)**2)**2, 2)
            k.append(k_i)
            # 加载数据
            self.exp_data_3c.setItem(3, i, QtWidgets.QTableWidgetItem(str(k[i])))
    # except:
    #     QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)

# 光滑管作图
def get_pic_3a(self):
    try:
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

        fig = plt.figure(1)
        host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
        host.set_ylabel('ln(λ)')
        host.set_xlabel('ln(Re)')
        fig.add_axes(host)
        p1, = host.plot(logRe, logLd,'s', label="original values")
        # 公式
        # 一次线性方程
        z = np.polyfit(logRe, logLd, 1)
        p = np.poly1d(z)
        # 代公式
        yvals = p(logRe)
        # 拟合曲线
        host.plot(logRe, yvals, 'r', label='polyfit values')
        host.set_title('光滑管ln(Re)-ln(λ)拟合曲线')
        # 相关系数R2
        r2 = round(r2_score(logLd,yvals),4)
        # 完整公式
        text='y='+ str(p).strip() +'\n'+ "R\u00b2=" + str(r2).strip()
        # 显示公式
        plt.text(np.average(logRe)-0.7,(np.average(logLd)),text,size=12,family="Times new roman",color="black",style='italic',weight='light')
        host.legend()
        plt.show()
        plt.savefig('./data/img/exp_3_data_1.png')

    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)

# 粗糙管作图
def get_pic_3b(self):
    try:
        Re = []
        ld = []
        logRe = []
        logLd = []
        for i in range(0, 10):
            # 获取雷诺数
            Re.append(float(self.exp_data_3b.item(i, 2).text()))
            # 获取局部阻力系数
            ld.append(float(self.exp_data_3b.item(i, 3).text()))
            # 取对数
            logRe.append(np.log(Re[i]))
            logLd.append(np.log(ld[i]))

        fig = plt.figure(1)
        host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
        host.set_ylabel('ln(λ)')
        host.set_xlabel('ln(Re)')
        fig.add_axes(host)
        p1, = host.plot(logRe, logLd, 's', label="original values")
        host.set_title('粗糙管ln(Re)-ln(λ)拟合曲线')
        # 公式
        # 一次线性方程
        z = np.polyfit(logRe, logLd, 1)
        p = np.poly1d(z)
        # 代公式
        yvals = p(logRe)
        # 拟合曲线
        host.plot(logRe, yvals, 'r', label='polyfit values')
        # 相关系数R2
        r2 = round(r2_score(logLd, yvals), 4)
        # 完整公式
        text = 'y=' + str(p).strip() + '\n' + "R\u00b2=" + str(r2).strip()
        # 显示公式
        plt.text(np.average(logRe) - 0.7, (np.average(logLd)), text, size=12, family="Times new roman", color="black",
                 style='italic', weight='light')
        host.legend()
        plt.show()

        plt.savefig('./data/img/exp_3_data_2.png')
    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)
        
def reset_pic_3a(self):
    self.exp_data_3a.clearContents()
    
def reset_pic_3b(self):
    self.exp_data_3b.clearContents()
    
def reset_pic_3c(self):
    self.exp_data_3c.clearContents()