from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

# 实验二数据处理
def calculate_data2(self):
    try:
        # 获取基本数据：
        # 管内径
        d = float(self.d2.text())
        # 变截面管喉径
        d2 = float(self.d_2.text())
        # 水温
        t = float(self.t2.text())
        # 水密度
        rou = float(self.rou2.text())
        # 水粘度
        miu = float(self.miu2.text())
        # 获取流量
        Q = []
        for i in range(0,8):
            Q.append(float(self.exp_data_1a.item(i,0).text()))
        # 获取高度
        H1 = []
        H2 = []
        H3 = []
        H4 = []
        H5 = []
        H6 = []
        H7 = []
        H8 = []
        for i in range(0,8):
            H1.append(float(self.exp_data_2a.item(i,1).text()))
            H2.append(float(self.exp_data_2a.item(i,2).text()))
            H3.append(float(self.exp_data_2a.item(i,3).text()))
            H4.append(float(self.exp_data_2a.item(i,4).text()))
            H5.append(float(self.exp_data_2a.item(i,5).text()))
            H6.append(float(self.exp_data_2a.item(i,6).text()))
            H7.append(float(self.exp_data_2a.item(i,7).text()))
            H8.append(float(self.exp_data_2a.item(i,8).text()))
        # 主体管路平均流速u(m/s)
        u = []
        # 2截面平均流速(m / s)
        u_2 = []
        # 通过节流件阻力损失（mmH2O）
        hf = []
        # 5截面中心点速度u5(m / s)
        u5 = []
        # 7截面中心点速度u7(m / s)
        u7 = []
        u_d_u5 = []
        u_d_u7 = []
        for i in range(0,8):
            ui = round((Q[i]/1000) * 4 / 3600 / 3.1415 / (d/1000)**2 , 2)
            u.append(ui)

            ui_2 = round((Q[i]/1000) * 4 / 3600 / 3.1415 / d2 ** 2, 2)
            u_2.append(ui_2)

            hfi = round(H1[i] - H3[i] , 1)
            hf.append(hfi)

            u5i = round((2 * 9.81 * (H5[i] - H4[i]) / 100)**0.5 , 4)
            u5.append(u5i)

            u7i= round((2 * 9.81 * (H7[i] - H6[i]) / 100) ** 0.5, 4)
            u7.append(u7i)

            u_d_u5.append(round(u[i] / u5[i], 3))

            u_d_u7.append(round(u[i] / u7[i], 3))

        # 在表2加载数据
        for i in range(0,8):
            self.exp_data_2b.setItem(i, 0, QtWidgets.QTableWidgetItem(str(Q[i])))
            self.exp_data_2b.setItem(i, 1, QtWidgets.QTableWidgetItem(str(u[i])))
            self.exp_data_2b.setItem(i, 2, QtWidgets.QTableWidgetItem(str(u_2[i])))
            self.exp_data_2b.setItem(i, 3, QtWidgets.QTableWidgetItem(str(hf[i])))
            self.exp_data_2b.setItem(i, 4, QtWidgets.QTableWidgetItem(str(u5[i])))
            self.exp_data_2b.setItem(i, 5, QtWidgets.QTableWidgetItem(str(u7[i])))
            self.exp_data_2b.setItem(i, 6, QtWidgets.QTableWidgetItem(str(u_d_u5[i])))
            self.exp_data_2b.setItem(i, 7, QtWidgets.QTableWidgetItem(str(u_d_u7[i])))

    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)

def reset_pic(self):
    self.exp_data_2a.clearContents()
    self.exp_data_2b.clearContents()