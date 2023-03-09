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

def write_5_docx(self,param):
    # 实验报告
    document = Document('./resources/report/实验五 恒压过滤实验.docx')
    document.add_paragraph('实验日期' + param.data + "\t室温" + param.temp +"\t过滤面积" + param.area +
                           "\t滤渣压缩系数" + param.s + "\t滤液的粘度" + param.u +
                           "\t滤渣比阻" + param.r + "\t单位滤液体积的滤渣体积" + param.V)
    document.add_paragraph("                表1 数据记录表")
    table1 = document.add_table(30 + 1, 3, style='Table Grid')

    # 设置表格样式
    for i in range(3):
        table1.rows[0].cells[i].text = self.data_processing_5_table_1.horizontalHeaderItem(i).data(0)

    table1.cell(1, 0).merge(table1.cell(10, 0))
    table1.cell(11, 0).merge(table1.cell(20, 0))
    table1.cell(21, 0).merge(table1.cell(30, 0))

    # 填入数据

    table1.cell(1, 0).text = str(param.p1)
    table1.cell(11, 0).text = str(param.p2)
    table1.cell(21, 0).text = str(param.p3)

    for j in range(len(param.t1)):
        table1.cell(j + 1, 1).text = str(param.t1[j])
        table1.cell(11 + j, 1).text = str(param.t2[j])
        table1.cell(21 + j, 1).text = str(param.t3[j])

        table1.cell(j + 1, 2).text = str(param.g1[j])
        table1.cell(11 + j, 2).text = str(param.g2[j])
        table1.cell(21 + j, 2).text = str(param.g3[j])

    document.add_paragraph("\n")

    document.add_paragraph("                表2 数据处理表")
    table2 = document.add_table(31, 7, style='Table Grid')
    for i in range(7):
        table2.rows[0].cells[i].text = self.data_processing_5_table_2.horizontalHeaderItem(i).data(0)

    for i in [0, 4, 5, 6]:
        table2.cell(1, i).merge(table2.cell(10, i))
        table2.cell(11, i).merge(table2.cell(20, i))
        table2.cell(21, i).merge(table2.cell(30, i))

    table2.cell(1, 0).text = str(param.p1)
    table2.cell(11, 0).text = str(param.p2)
    table2.cell(21, 0).text = str(param.p3)
    table2.cell(1, 4).text = str(param.K1)
    table2.cell(11, 4).text = str(param.K2)
    table2.cell(21, 4).text = str(param.K3)
    table2.cell(1, 5).text = str(param.qe1)
    table2.cell(11, 5).text = str(param.qe2)
    table2.cell(21, 5).text = str(param.qe3)
    table2.cell(1, 6).text = str(param.te1)
    table2.cell(11, 6).text = str(param.te2)
    table2.cell(21, 6).text = str(param.te3)

    for i in range(10):
        table2.cell(i + 1, 1).text = str(param.t1[i])
        table2.cell(11 + i, 1).text = str(param.t2[i])
        table2.cell(21 + i, 1).text = str(param.t3[i])
        table2.cell(i + 1, 2).text = str(param.q1[i])
        table2.cell(11 + i, 2).text = str(param.q2[i])
        table2.cell(21 + i, 2).text = str(param.q3[i])
        table2.cell(i + 1, 3).text = str(param.qt1[i])
        table2.cell(11 + i, 3).text = str(param.qt2[i])
        table2.cell(21 + i, 3).text = str(param.qt3[i])
    document.add_paragraph("\n")

    document.add_picture('./data/img/exp_5_data_1.png')

    # 保存文件
    pre_path = import_data(param.self)
    file_path = pre_path + '/' + '实验五 恒压过滤实验.docx'
    document.save(file_path)

    # 创建一个问答框
    param.self.box = QMessageBox(QMessageBox.Question, '提示', 'docx文件已保存，是否转换成pdf文件？')

    # 添加按钮
    yes = param.self.box.addButton('确定', QMessageBox.YesRole)
    no = param.self.box.addButton('取消', QMessageBox.NoRole)

    # 显示该问答框
    param.self.box.exec_()

    if param.self.box.clickedButton() == yes:
        print(1)
        # docx转pdf
        docx2pdf(file_path)
        QMessageBox.information(param.self, '提示', '成功生成pdf文件！', QMessageBox.Ok)
    else:
        print(2)
        pass