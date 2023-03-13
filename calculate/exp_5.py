import math
import os

from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5 import QtGui
import matplotlib.pyplot as plt

from report.report_5 import write_5_docx


# 第五章的数据处理部分
def data_processing_5_date_calculate_click(self):
    QMessageBox.information(self, '提示', '正在计算中,请稍等~~~', QMessageBox.Ok)
    # 滤渣压缩系数
    s = self.data_processing_5_date_s.text()
    # 滤渣比阻
    r = self.data_processing_5_date_r.text()
    # 单位滤液的滤渣体积
    V = self.data_processing_5_date_v.text()
    # 滤液的粘度
    u = self.data_processing_5_date_u.text()
    # 日期
    date = self.data_processing_5_date.text()
    # 过滤面积
    area = self.data_processing_5_date_area.text()
    # 温度
    temp = self.data_processing_5_date_temp.text()
    if (self.data_processing_5_date_s.text() == ''
            or self.data_processing_5_date_r.text() == ''
            or self.data_processing_5_date_u.text() == ''
            or self.data_processing_5_date_v.text() == ''
            or self.data_processing_5_date.text() == ''
            or self.data_processing_5_date_area.text() == ''
            or self.data_processing_5_date_temp.text() == ''):
        QMessageBox.information(self, '提示', '请填写所有完整信息！', QMessageBox.Ok)
        return

    else:
        # 分别对应表中填写的三个压强差
        p1 = int(self.data_processing_5_table_1.item(0, 0).data(0))
        p2 = int(self.data_processing_5_table_1.item(10, 0).data(0))
        p3 = int(self.data_processing_5_table_1.item(20, 0).data(0))

        # 分别对应表中填写的三列时间
        t1 = []
        t2 = []
        t3 = []
        # 分别对应表中填写的三个质量
        g1 = []
        g2 = []
        g3 = []
        # 由质量计算出来的体积
        v1 = []
        v2 = []
        v3 = []
        # 相对滤液体积
        q1 = []
        q2 = []
        q3 = []
        # q/t
        qt1 = []
        qt2 = []
        qt3 = []

        Ve1 = 0
        Ve2 = 0
        Ve3 = 0

        # 获取表1中的时间和质量保存到列表中,
        # 1. 将时间填写在表2中
        # 2. 计算出质量对应的体积保存在列表中
        # 3. 计算相对滤液体积填入表2
        # 4. 计算t/q填入表2
        for i in range(10):
            if (self.data_processing_5_table_1.item(i, 1) is not None
                    and self.data_processing_5_table_1.item(i, 2) is not None):
                t = self.data_processing_5_table_1.item(i, 1).data(0)
                g = self.data_processing_5_table_1.item(i, 2).data(0)

                t1.append(int(t))
                g1.append(int(g))
                v = int(g) * 0.997537
                v1.append(int(v))
                item = QTableWidgetItem()
                item.setText(t)
                self.data_processing_5_table_2.setItem(i, 1, item)
                q = v / int(area)
                item = QTableWidgetItem()
                item.setText(str(q))
                q1.append(q)
                self.data_processing_5_table_2.setItem(i, 2, item)
                tq = int(t) / q
                qt1.append(tq)
                item = QTableWidgetItem()
                item.setText(str(tq))
                self.data_processing_5_table_2.setItem(i, 3, item)
        for i in range(10):
            if (self.data_processing_5_table_1.item(i + 10, 1) is not None
                    and self.data_processing_5_table_1.item(i + 10, 2) is not None):
                t = self.data_processing_5_table_1.item(i + 10, 1).data(0)
                g = self.data_processing_5_table_1.item(i + 10, 2).data(0)

                t2.append(int(t))
                g2.append(int(g))
                v = int(g) * 0.997537
                v2.append(int(v))
                item = QTableWidgetItem()
                item.setText(t)
                self.data_processing_5_table_2.setItem(i + 10, 1, item)
                q = v / int(area)
                item = QTableWidgetItem()
                item.setText(str(q))
                q2.append(q)
                self.data_processing_5_table_2.setItem(i + 10, 2, item)
                tq = int(t) / q
                qt2.append(tq)
                item = QTableWidgetItem()
                item.setText(str(tq))
                self.data_processing_5_table_2.setItem(i + 10, 3, item)

        for i in range(10):
            if (self.data_processing_5_table_1.item(i + 20, 1) is not None
                    and self.data_processing_5_table_1.item(i + 20, 2) is not None):
                t = self.data_processing_5_table_1.item(i + 20, 1).data(0)
                g = self.data_processing_5_table_1.item(i + 20, 2).data(0)

                # 保存时间
                t3.append(int(t))
                # 保存质量
                g3.append(int(g))
                # 计算体积
                v = int(g) * 0.997537
                # 保存体积
                v3.append(int(v))
                item = QTableWidgetItem()
                item.setText(t)
                # 时间填入表2
                self.data_processing_5_table_2.setItem(i + 20, 1, item)
                # 相对滤液体积填入表2
                q = v / int(area)
                item = QTableWidgetItem()
                item.setText(str(q))
                q3.append(q)
                self.data_processing_5_table_2.setItem(i + 20, 2, item)
                # 计算t/q填入表2
                tq = int(t) / q
                qt3.append(tq)
                item = QTableWidgetItem()
                item.setText(str(tq))
                self.data_processing_5_table_2.setItem(i + 20, 3, item)

        # 填写表2的压力跟表1的一样
        item = QTableWidgetItem()
        item.setText(str(p1))
        self.data_processing_5_table_2.setItem(0, 0, item)
        item = QTableWidgetItem()
        item.setText(str(p2))
        self.data_processing_5_table_2.setItem(10, 0, item)
        item = QTableWidgetItem()
        item.setText(str(p3))
        self.data_processing_5_table_2.setItem(20, 0, item)

        # # 计算K
        K1 = (2 * p1 ^ (1 - int(s))) / (int(u) * int(r) * int(V))
        K2 = (2 * p2 ^ (1 - int(s))) / (int(u) * int(r) * int(V))
        K3 = (2 * p3 ^ (1 - int(s))) / (int(u) * int(r) * int(V))
        # 将K填入表2
        item = QTableWidgetItem()
        item.setText(str(K1))
        self.data_processing_5_table_2.setItem(0, 4, item)
        item = QTableWidgetItem()
        item.setText(str(K2))
        self.data_processing_5_table_2.setItem(10, 4, item)
        item = QTableWidgetItem()
        item.setText(str(K3))
        self.data_processing_5_table_2.setItem(20, 4, item)

        # 计算Ve过滤介质的当量滤液体积
        Ve1 = (K1 * (int(area) ^ 2) * t1[-1] - (v1[-1] ^ 2)) / (2 * v1[-1])

        Ve2 = (K2 * (int(area) ^ 2) * t2[-1] - (v2[-1] ^ 2)) / (2 * v2[-1])
        Ve3 = (K3 * (int(area) ^ 2) * t3[-1] - (v3[-1] ^ 2)) / (2 * v3[-1])

        # 计算得出te
        te1 = Ve1.__pow__(2) / K1 / (int(area) ^ 2)
        te2 = Ve2.__pow__(2) / K2 / (int(area) ^ 2)
        te3 = Ve3.__pow__(2) / K3 / (int(area) ^ 2)

        # te填入表2
        item = QTableWidgetItem()
        item.setText(str(te1))
        self.data_processing_5_table_2.setItem(0, 6, item)
        item = QTableWidgetItem()
        item.setText(str(te2))
        self.data_processing_5_table_2.setItem(10, 6, item)
        item = QTableWidgetItem()
        item.setText(str(te3))
        self.data_processing_5_table_2.setItem(20, 6, item)

        # 计算得出qe
        qe1 = math.sqrt(K1 * te1)
        qe2 = math.sqrt(K2 * te2)
        qe3 = math.sqrt(K3 * te3)

        # qe填入表2
        item = QTableWidgetItem()
        item.setText(str(qe1))
        self.data_processing_5_table_2.setItem(0, 5, item)
        item = QTableWidgetItem()
        item.setText(str(qe2))
        self.data_processing_5_table_2.setItem(10, 5, item)
        item = QTableWidgetItem()
        item.setText(str(qe3))
        self.data_processing_5_table_2.setItem(20, 5, item)

        # 绘图
        plt.plot(q1, qt1, color='r')
        plt.plot(q2, qt2, color='b')
        plt.plot(q3, qt3, color='g')

        plt.legend(['first', 'second', 'third'])

        plt.xlabel('q')
        plt.ylabel('q/t')
        plt.savefig('./data/img/exp_5_data_1.png')

        img = os.path.abspath("./data/img/exp_5_data_1.png")
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        self.data_processing_5_img.setScaledContents(True)
        self.data_processing_5_img.setPixmap(image)

        # 创建一个问答框
        self.box = QMessageBox(QMessageBox.Question, '提示', '计算完成,是否要生成实验报告?')

        # 添加按钮
        yes = self.box.addButton('确定', QMessageBox.YesRole)
        no = self.box.addButton('取消', QMessageBox.NoRole)

        # 显示该问答框
        self.box.exec_()
        if self.box.clickedButton() == yes:
            # 实验报告
            write_5_docx(self, p1, p2, p3, t1, t2, t3, g1, g2, g3, K1, K2, K3, qe1, qe2, qe3, te1, te2, te3, qt1, qt2,
                         qt3, s, r, V, u, date, area, temp, q1, q2, q3)
