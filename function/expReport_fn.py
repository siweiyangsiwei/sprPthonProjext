import docx
from PyQt5.QtWidgets import QMessageBox,QFileDialog
from win32com import client

# 获取实验数据
def get_data(self):
    self.weather = self.edit_weather.text()
    self.length = self.edit_length.text()
    if self.weather == '' or self.length == '':
        QMessageBox.critical(self,'错误','实验数据不完整',QMessageBox.Ok)
    else:
        write_docx(self)

# 选择文件要保存的位置
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

# 生成docx文件
def write_docx(self):
    try:
        pre_path = import_data(self)
        if pre_path == '':
            pass
        else:
            # 获取模板
            doc = docx.Document('resources/report/实验一.docx')

            # 写入实验数据
            doc.add_paragraph("温度：" + self.weather + '℃' + '\t' + '测压段管长：' + self.length + 'm')

            # 获取保存路径
            file_path = pre_path + '/' + '实验一.docx'
            doc.save(file_path)

            # 创建一个问答框，注意是Question
            self.box = QMessageBox(QMessageBox.Question, '提示', 'docx文件已保存，是否转换成pdf文件？')

            # 添加按钮，可用中文
            yes = self.box.addButton('确定', QMessageBox.YesRole)
            no = self.box.addButton('取消', QMessageBox.NoRole)

            # 设置消息框中内容前面的图标
            self.box.setIcon(1)

            # 显示该问答框
            self.box.exec_()

            if self.box.clickedButton() == yes:
                print(1)
                # docx转pdf
                docx2pdf(file_path)
                QMessageBox.information(self, '提示', '成功生成pdf文件！', QMessageBox.Ok)
            else:
                print(2)
                pass


    except:
        QMessageBox.critical(self, '错误', '保存失败', QMessageBox.Ok)








