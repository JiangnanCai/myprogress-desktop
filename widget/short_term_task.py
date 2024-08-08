from typing import Any

import PyQt5.QtCore
import PyQt5.QtWidgets

from widget.my_input_confirm import MyInputWidget
from widget.my_checkbox_time import TimeCheckBox


class ShortTermTaskWidget(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent: Any = None):
        super(ShortTermTaskWidget, self).__init__(parent)
        self.layout = PyQt5.QtWidgets.QVBoxLayout(self)

        self.scroll_area = PyQt5.QtWidgets.QScrollArea(self)
        self.scroll_area.setStyleSheet("QScrollArea { border: none;}")
        self.scroll_area_widget = PyQt5.QtWidgets.QWidget(self.scroll_area)
        self.scroll_area_layout = PyQt5.QtWidgets.QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_widget.setLayout(self.scroll_area_layout)
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_layout.setSpacing(0)
        self.scroll_area_layout.setAlignment(PyQt5.QtCore.Qt.AlignTop)
        self.scroll_area.setHorizontalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)

        self.input_line = MyInputWidget(self)
        self.input_line.signal_submit_text.connect(self.new_widget)

        self.layout.addWidget(self.scroll_area)
        self.layout.addWidget(self.input_line)

    def new_widget(self, text):
        task_widget = TimeCheckBox(text, self.scroll_area_widget)
        # label = PyQt5.QtWidgets.QLabel('asdad', self.scroll_area_widget)
        self.scroll_area_layout.addWidget(task_widget)
        self.update()


if __name__ == '__main__':
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main_window = ShortTermTaskWidget()
    main_window.show()
    sys.exit(app.exec_())
