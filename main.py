from PyQt5 import QtWidgets
from controllers.LoginWindow import LoginWindow
import sys
from controllers.MainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # login_window = LoginWindow()
    # login_window.show()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
