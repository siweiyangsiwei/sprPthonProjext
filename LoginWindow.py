from PyQt5.QtWidgets import QMainWindow
from MainWindow import MainWindow
from login import Ui_MainWindow


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        user = self.user_lineedit.text()
        pwd = self.pwd_lineedit.text()
        if user == '123' and pwd == '123':
            main_window = MainWindow()
            main_window.show()
            self.close()
