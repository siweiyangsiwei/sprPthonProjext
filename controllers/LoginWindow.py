from PyQt5.QtWidgets import QMainWindow
from controllers.MainWindow import MainWindow
from view.login import Ui_MainWindow


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.setWindowTitle("登录")


    def login(self):
        user = self.user_lineedit.text()
        pwd = self.pwd_lineedit.text()
        if user == '123' and pwd == '123':
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
