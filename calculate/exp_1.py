from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

# 实验一数据处理
# 雷诺数计算
def calculate_data1(self):
    try:
        # 获取参数
        tube_d_1 = float(self.d1.text())
        tem_1 = float(self.t1.text())
        density_1 = float(self.rou1.text())
        acousity_1 = float(self.miu1.text())
        # 获取流量
        Q1 = float(self.exp_data_1a.item(0, 0).text())
        Q2 = float(self.exp_data_1a.item(1, 0).text())
        Q3 = float(self.exp_data_1a.item(2, 0).text())
        Q4 = float(self.exp_data_1a.item(3, 0).text())
        Q5 = float(self.exp_data_1a.item(4, 0).text())
        Q6 = float(self.exp_data_1a.item(5, 0).text())
        Q7 = float(self.exp_data_1a.item(6, 0).text())
        Q8 = float(self.exp_data_1a.item(7, 0).text())
        Q9 = float(self.exp_data_1a.item(7, 0).text())
        Q10 = float(self.exp_data_1a.item(7, 0).text())
        Q_1 =[Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10]
        u_1 = []
        Rey_1 = []
        flow = []

        # 写入流型
        for i in range(0,10):
            flow.append(str(self.exp_data_1a.item(i, 1).text()))

        # 计算u
        for waterQ1 in Q_1:
            u1 = waterQ1 /  (3600 * 0.25 * 3.1415 * (tube_d_1/1000)**2)
            u_1.append(u1)
        # 计算Re
        for wateru_1 in u_1:
            Reynold1 = tube_d_1*wateru_1*density_1/acousity_1
            Reynold1round = round(Reynold1,1)
            Rey_1.append(Reynold1round)

        # 加载表2数据
        for i in range(0, 10):
            # 加载流量
            self.exp_data_1b.setItem(i, 0, QtWidgets.QTableWidgetItem(str(Q_1[i])))
            # 加载流速u
            self.exp_data_1b.setItem(i, 1, QtWidgets.QTableWidgetItem(str(round(u_1[i],2))))
            # 加载Re
            self.exp_data_1b.setItem(i, 2, QtWidgets.QTableWidgetItem(str(Rey_1[i])))
            # 观察到的流型
            self.exp_data_1b.setItem(i, 3, QtWidgets.QTableWidgetItem(str(flow[i])))
            # 判断理论流动形态
            if Rey_1[i] <= 2000:
                self.exp_data_1b.setItem(i, 4, QtWidgets.QTableWidgetItem('层流'))
            elif Rey_1[i] <= 4000:
                self.exp_data_1b.setItem(i, 4, QtWidgets.QTableWidgetItem('过渡态'))
            else:
                self.exp_data_1b.setItem(i, 4, QtWidgets.QTableWidgetItem('湍流'))
    except:
        QMessageBox.critical(self, '错误', '数据错误！', QMessageBox.Ok)


def reset_pic(self):
    self.exp_data_1a.clearContents()
    self.exp_data_1b.clearContents()
