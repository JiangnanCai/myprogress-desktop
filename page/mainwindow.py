import PyQt5.QtWidgets
from ui import Ui_MainWindow


class MainWindow(PyQt5.QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
