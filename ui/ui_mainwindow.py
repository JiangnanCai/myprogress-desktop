from typing import Any

import PyQt5.QtWidgets
import PyQt5.QtCore

from widget import MyTaskCollapseWidget
from data import task_datas


class MyScrollArea(PyQt5.QtWidgets.QScrollArea):
    def __init__(self, parent: Any = None):
        super(MyScrollArea, self).__init__(parent)

        self.setStyleSheet("QScrollArea { border: none; }")

        self.widget = PyQt5.QtWidgets.QWidget(self)
        self.layout = PyQt5.QtWidgets.QVBoxLayout(self.widget)
        self.widget.setLayout(self.layout)
        self.setWidget(self.widget)
        self.setWidgetResizable(True)

        self.layout.setSpacing(0)
        self.layout.setAlignment(PyQt5.QtCore.Qt.AlignTop)

        self.setHorizontalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)

        self.setWidget(self.widget)


class Ui_MainWindow(object):
    def __init__(self):
        self.widget = None
        self.layout = None
        self.scroll_area = None

        self.task = task_datas
        self.num_task = len(self.task)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.setStyleSheet("background-color: white;")
        MainWindow.setWindowTitle('My Progress')

        self.widget = PyQt5.QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.widget)
        self.layout = PyQt5.QtWidgets.QVBoxLayout(self.widget)
        self.widget.setLayout(self.layout)

        self.scroll_area = MyScrollArea(self.widget)

        self.layout.addWidget(self.scroll_area)

        for title, value in self.task.items():
            collapse_box = MyTaskCollapseWidget(task_datas=value, title=title, parent=MainWindow)
            self.scroll_area.layout.addWidget(collapse_box, alignment=PyQt5.QtCore.Qt.AlignTop)




