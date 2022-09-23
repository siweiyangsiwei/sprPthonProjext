import smtplib
import os
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from PyQt5.QtWidgets import QMessageBox,QFileDialog


# 添加附件
def import_data(self):
    self.file_path, file_type = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;Text Files (*.txt)")
    (path, file_name) = os.path.split(self.file_path)
    self.label_fileName.setText(file_name)

# 发送邮件
def send_email(self):
    host_sever = 'smtp.163.com'  # qq邮箱smtp服务器
    pwd = 'ANXQRDSTOGGAAMFA' # 授权码
    sender = 'yuebeix588441@163.com'

    # 获取输入框内容
    receiver = self.text_recevier.text()
    mail_title = self.text_title.text()
    mail_content = self.text_content.toPlainText()

    # 定义一个可以添加正文和附件的邮件消息对象
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender
    msg["To"] = Header("测试邮箱", 'utf-8')

    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

    # 添加附件
    try:
        attachment = MIMEApplication(open(self.file_path,'rb').read())
        attachment.add_header('Content-Disposition', 'attachment', filename='1.pdf')
        msg.attach(attachment)
    except:
        pass

    try:
        smtp = SMTP_SSL(host_sever)
        smtp.set_debuglevel(0)
        smtp.ehlo(host_sever)
        smtp.login(sender, pwd)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        QMessageBox.information(self, '提示', '发送邮件成功！', QMessageBox.Ok)

    except smtplib.SMTPException:
        QMessageBox.critical(self, '错误', '无法发送邮件！', QMessageBox.Ok)
