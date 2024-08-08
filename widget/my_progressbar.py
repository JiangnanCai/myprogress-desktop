from typing import Any

import PyQt5.QtWidgets
import PyQt5.QtCore

from widget.my_diagram import MyDiagramDialog


class MyProgressBar(PyQt5.QtWidgets.QWidget):
    def __init__(self,
                 title: str = '',
                 parent: Any = None):
        super(MyProgressBar, self).__init__(parent)

        self.diagram_title = 'diagram'
        self.canvas = None

        self.resize(300, 50)
        self.h_layout = PyQt5.QtWidgets.QHBoxLayout(self)

        self.label = PyQt5.QtWidgets.QLabel(self)
        self.label.setFixedWidth(85)
        self.label.setText(title)

        self.progressbar = PyQt5.QtWidgets.QProgressBar(self)
        self.progressbar.setFormat('%p%')

        self.button_add = PyQt5.QtWidgets.QPushButton('+', self)
        self.button_add.setFixedSize(20, 20)
        self.button_add.clicked.connect(self.on_button_clicked)

        self.h_layout.addWidget(self.label, alignment=PyQt5.QtCore.Qt.AlignRight)
        self.h_layout.addWidget(self.progressbar, alignment=PyQt5.QtCore.Qt.AlignVCenter)
        self.h_layout.addWidget(self.button_add, alignment=PyQt5.QtCore.Qt.AlignCenter)

    def setValue(self, cur_value: int):
        self.progressbar.setValue(cur_value)

    def setRange(self, min_value: int, max_value: int):
        self.progressbar.setRange(min_value, max_value)

    def setText(self, text: str):
        self.label.setText(text)

    def on_button_clicked(self):
        dialog = MyDiagramDialog(self.diagram_title, self.canvas)
        dialog.exec_()


if __name__ == '__main__':
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main_window = MyProgressBar()
    main_window.show()
    sys.exit(app.exec_())



