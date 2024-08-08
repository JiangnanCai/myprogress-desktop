from typing import Any

import PyQt5.QtCore
import PyQt5.QtWidgets


class MyInputWidget(PyQt5.QtWidgets.QWidget):
    signal_submit_text = PyQt5.QtCore.pyqtSignal(str)

    def __init__(self, parent: Any = None):
        super(MyInputWidget, self).__init__(parent)

        layout = PyQt5.QtWidgets.QHBoxLayout(self)

        self.label_text = PyQt5.QtWidgets.QLabel(self)
        self.label_text.setText('new: ')

        self.text_line = PyQt5.QtWidgets.QLineEdit(self)

        self.button_confirm = PyQt5.QtWidgets.QPushButton(self)
        self.button_confirm.setText('add')
        self.button_confirm.clicked.connect(self.button_clicked)

        layout.addWidget(self.label_text)
        layout.addWidget(self.text_line)
        layout.addWidget(self.button_confirm)

        self.text = None

    def button_clicked(self):
        self.text = self.text_line.text()
        if self.text != "":
            self.signal_submit_text.emit(self.text)
        self.text_line.clear()


if __name__ == '__main__':
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main_window = MyInputWidget()
    main_window.show()
    sys.exit(app.exec_())