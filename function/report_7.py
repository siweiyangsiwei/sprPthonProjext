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

def write_7_docx(self, data1, data2, data3, HETP, R1, R2, R3, q1, q2, q3, date, num_of_pic, num_of_shai_ban,
             height_of_tian_liao,tower_type):
    # 实验报告
    document = Document('./resources/report/实验七 精馏实验.docx')
    document.add_paragraph('实验日期' + date + "\t板式塔实际塔板数" + num_of_shai_ban +
                           "\t填料塔填料层高度" + height_of_tian_liao +
                           "\t图解法计算所得理论板数" + num_of_pic)
    document.add_paragraph("                表1 数据记录表")
    table1 = document.add_table(len(data1) + 1, 4, style='Table Grid')
    table1.rows[0].cells[1].text = '1'
    table1.rows[0].cells[2].text = '2'
    table1.rows[0].cells[3].text = '3'
    if not tower_type:
        for i in range(len(data1)):
            table1.rows[i + 1].cells[0].text = self.data_processing_7_table_1.verticalHeaderItem(i).data(0)

    else:
        for i in range(len(data1)):
            table1.rows[i + 1].cells[0].text = self.data_processing_7_table_2.verticalHeaderItem(i).data(0)

    for j in range(len(data1)):
        table1.rows[j + 1].cells[1].text = str(data1[j])
        table1.rows[j + 1].cells[2].text = str(data2[j])
        table1.rows[j + 1].cells[3].text = str(data3[j])
    document.add_paragraph("\n")

    document.add_paragraph("                表2 计算结果")
    table2 = document.add_table(4, 4, style='Table Grid')
    table2.rows[0].cells[1].text = '1'
    table2.rows[0].cells[2].text = '2'
    table2.rows[0].cells[3].text = '3'
    for i in range(3):
        table2.rows[i + 1].cells[0].text = self.data_processing_7_table_3.verticalHeaderItem(i).data(0)
        table2.rows[1].cells[1].text = str(HETP)
        table2.rows[1].cells[2].text = str(HETP)
        table2.rows[1].cells[3].text = str(HETP)
        table2.rows[2].cells[1].text = str(R1)
        table2.rows[2].cells[2].text = str(R2)
        table2.rows[2].cells[3].text = str(R3)
        table2.rows[3].cells[1].text = str(q1)
        table2.rows[3].cells[2].text = str(q2)
        table2.rows[3].cells[3].text = str(q3)

    # 保存文件
    pre_path = import_data(self)
    file_path = pre_path + '/' + '实验七 精馏实验.docx'
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
        pass