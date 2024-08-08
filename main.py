import sys

import PyQt5.QtWidgets

from page import MainWindow

if __name__ == '__main__':

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
