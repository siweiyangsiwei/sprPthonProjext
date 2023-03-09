from PyQt5.QtWidgets import QFileDialog, QMessageBox
from win32com import client
from docx import Document


def import_data(self):
    file_path = QFileDialog.getExistingDirectory()
    return file_path


# 转换docx为pdf
def docx2pdf(fn):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    # for file in files:
    doc = word.Documents.Open(fn)  # 打开word文件
    doc.SaveAs("{}.pdf".format(fn[:-5]), 17)  # 另存为后缀为".pdf"的文件，其中参数17表示为pdf
    doc.Close()  # 关闭原来word文件
    word.Quit()


def write_9_docx(self,data, date, bgtemp, fgtemp, flow, fstemp, pressure, size, weight, area):
    # 完成实验报告
    document = Document('./resources/report/实验九 洞道干燥实验.docx')

    document.add_paragraph('实验日期' + date + "\t干燥介质:热空气\t物料尺寸" + size +
                           "\t物料的绝干质量" + weight +
                           "\t干燥室截面积" + area + "\t室前干球温度" + fgtemp +
                           "\t室前湿球温度" + fstemp + " \t室后干球温度" + bgtemp +
                           "\t孔板流量计空气流量" + flow + "\t风机出口压力" + pressure
                           )

    document.add_paragraph("                表1 数据记录表")
    table1 = document.add_table(len(data[0]), len(data), style='Table Grid')
    heading_cells = table1.rows[0].cells
    heading_cells[0].text = "湿物料质量Gi(g)"
    heading_cells[1].text = "湿物料含水量Xi(kg水/kg绝干料)"
    heading_cells[2].text = "湿物料平均含水量(kg水/kg绝干料)"
    heading_cells[3].text = "汽化水分量△W(g)"
    heading_cells[4].text = "时间间隔△t(m,s)"
    heading_cells[5].text = "干燥速率U(kg/m²,s"

    for i in range(len(data)):
        for j in range(len(data[0]) - 1):
            if i > 1 and j > len(data[0]) - 3:
                continue
            table1.rows[j + 1].cells[i].text = str(data[i][j])

    document.add_picture('./data/img/exp_9_data_1.png')
    document.add_picture('./data/img/exp_9_data_2.png')

    # 保存文件
    pre_path = import_data(self)
    file_path = pre_path + '/' + '实验九 洞道干燥实验.docx'
    document.save(file_path)

    # 创建一个问答框
    self.box = QMessageBox(QMessageBox.Question, '提示', 'docx文件已保存，是否转换成pdf文件？')

    # 添加按钮
    yes = self.box.addButton('确定', QMessageBox.YesRole)
    no = self.box.addButton('取消', QMessageBox.NoRole)

    # 显示该问答框
    self.box.exec_()

    if self.box.clickedButton() == yes:
        try:
            print(1)
            # docx转pdf
            docx2pdf(file_path)
            QMessageBox.information(self, '提示', '成功生成pdf文件！', QMessageBox.Ok)
        except:
            QMessageBox.information(self, '提示', '生成pdf文件出错！', QMessageBox.Ok)
    else:
        print(2)