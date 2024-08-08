from typing import Any
import random

import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore


class ArrowToolButton(PyQt5.QtWidgets.QToolButton):
    def __init__(self,
                 title: str = '',
                 parent: Any = None):
        super(ArrowToolButton, self).__init__(parent)
        self.setCheckable(True)
        self.setStyleSheet("QToolButton { border: none; }")
        self.setToolButtonStyle(PyQt5.QtCore.Qt.ToolButtonTextBesideIcon)
        self.setArrowType(PyQt5.QtCore.Qt.RightArrow)
        self.setText(title)

    def on_pressed(self):
        self.setArrowType(PyQt5.QtCore.Qt.DownArrow
                          if self.isChecked()
                          else PyQt5.QtCore.Qt.RightArrow)


class CollapseArea(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent: Any = None):
        super(CollapseArea, self).__init__(parent)
        self.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Minimum,
                           PyQt5.QtWidgets.QSizePolicy.Minimum)
        self.layout = PyQt5.QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)


class MyCollapseBox(PyQt5.QtWidgets.QWidget):
    def __init__(self,
                 title: str = '',
                 parent: Any = None):
        super(MyCollapseBox, self).__init__(parent)

        self.collapsed = True

        self.button_toggle = ArrowToolButton(parent=self)
        self.button_toggle.setChecked(self.collapsed)
        self.button_toggle.pressed.connect(self.on_pressed)
        self.button_toggle.setText(title)

        self.content_area = CollapseArea(self)
        self.content_area.setVisible(not self.collapsed)

        self.v_layout = PyQt5.QtWidgets.QVBoxLayout(self)
        self.v_layout.addWidget(self.button_toggle, alignment=PyQt5.QtCore.Qt.AlignTop)
        self.v_layout.addWidget(self.content_area, alignment=PyQt5.QtCore.Qt.AlignTop)

    def addWidget(self, widget):
        self.content_area.layout.addWidget(widget)

    def on_pressed(self):
        self.collapsed = self.button_toggle.isChecked()
        self.button_toggle.on_pressed()
        self.content_area.setVisible(self.collapsed)


if __name__ == '__main__':
    import sys
    from widget import MyProgressBar

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    collapsebox = MyCollapseBox('ffff')
    collapsebox.addWidget(MyProgressBar())
    collapsebox.addWidget(MyProgressBar())
    collapsebox.addWidget(MyProgressBar())
    collapsebox.show()
    sys.exit(app.exec_())
