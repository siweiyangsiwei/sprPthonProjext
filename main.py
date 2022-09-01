import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

from MainForm2 import Ui_MainForm2
from ChildForm2 import Ui_ChildForm2


class MainForm2(QMainWindow, Ui_MainForm2):
    def __init__(self):
        super(MainForm2, self).__init__()
        self.setupUi(self)
        self.child = ChildrenForm()
        self.fileActionOpen.triggered.connect(self.operMsg)
        self.addWinAction.triggered.connect(self.childShow)

    def childShow(self):
        self.MiangridLayout.addWidget(self.child)
        self.child.show()

    def operMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "open", "C:/", "All Files (*);;Text Files (*.txt)")
        self.statusBar().showMessage(file, 1000)

    def display(self):
        username = self.username.text()
        password = self.password.text()
        self.textBrowser.setText(username + " " + password)


class ChildrenForm(QWidget, Ui_ChildForm2):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainForm2()
    myWin.show()
    sys.exit(app.exec_())