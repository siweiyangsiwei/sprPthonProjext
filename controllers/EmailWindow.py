from PyQt5.QtWidgets import QMainWindow,QLabel
from view.email_window import Ui_emailWindow
import function.email_fn as email_fn

class EmailWindow(QMainWindow, Ui_emailWindow):
    def __init__(self):
        super(EmailWindow, self).__init__()
        self.setupUi(self)
        self.button_addFile.clicked.connect(lambda checked: email_fn.import_data(self))
        self.button_send.clicked.connect(lambda checked: email_fn.send_email(self))

