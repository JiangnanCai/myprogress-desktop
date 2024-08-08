from typing import Any

import PyQt5.QtWidgets
import PyQt5.QtCore

from widget import MyTaskCollapseWidget
from data import task_datas


class MyScrollArea(PyQt5.QtWidgets.QScrollArea):
    def __init__(self, parent: Any = None):
        super(MyScrollArea, self).__init__(parent)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)

        self.widget = PyQt5.QtWidgets.QWidget(self)
        self.layout = PyQt5.QtWidgets.QVBoxLayout(self.widget)

        self.layout.setSpacing(0)
        self.layout.setAlignment(PyQt5.QtCore.Qt.AlignTop)

        self.setWidget(self.widget)


class Ui_MainWindow(object):
    def __init__(self):
        self.width = 500
        self.height = 300

        self.v_layout = None
        self.scroll_area = None

        self.task = task_datas
        self.num_task = len(self.task)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.setStyleSheet("background-color: white;")
        MainWindow.resize(self.width, self.height)
        MainWindow.setWindowTitle('My Progress')

        self.v_layout = PyQt5.QtWidgets.QVBoxLayout(MainWindow)

        self.scroll_area = MyScrollArea(MainWindow)
        self.scroll_area.resize(self.width, self.height)

        for title, value in self.task.items():
            collapse_box = MyTaskCollapseWidget(task_datas=value, title=title, parent=MainWindow)
            self.scroll_area.layout.addWidget(collapse_box, alignment=PyQt5.QtCore.Qt.AlignTop)

        self.v_layout.addWidget(self.scroll_area, alignment=PyQt5.QtCore.Qt.AlignCenter)



