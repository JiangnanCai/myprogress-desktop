from typing import Any

import PyQt5.QtWidgets
import PyQt5.QtCore


class TimeCheckBox(PyQt5.QtWidgets.QWidget):
    def __init__(self,
                 text: str = '',
                 parent: Any = None):
        super(TimeCheckBox, self).__init__(parent)

        layout = PyQt5.QtWidgets.QHBoxLayout(self)

        self.checkbox = PyQt5.QtWidgets.QCheckBox(self)
        self.checkbox.setText(text)
        self.checkbox.stateChanged.connect(self.check)
        self.checkbox.stateChanged.connect(self.toggleTimer)
        self.checkbox.setStyleSheet("QCheckBox: { text-decoration: line-through; } ")

        self.button_timer = PyQt5.QtWidgets.QPushButton(self)
        self.button_timer.clicked.connect(self.toggleTimer)
        self.button_timer.setText('start')

        self.button_delete = PyQt5.QtWidgets.QPushButton(self)
        self.button_delete.setText('delete')

        layout.addWidget(self.checkbox)
        layout.addWidget(self.button_timer)
        layout.addWidget(self.button_delete)

        self.timer = PyQt5.QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timeElapsed = 0  # 以秒为单位

        self.isTimerRunning = False

    def toggleTimer(self):
        formatted_time = TimeCheckBox.get_formatted_time(self.timeElapsed)
        if self.isTimerRunning:
            self.timer.stop()
            self.button_timer.setText(f"{formatted_time}")
        else:
            if self.timeElapsed != 0:
                self.checkbox.setChecked(not self.checkbox.isChecked())
            self.timer.start(1000)  # 每秒更新一次时间
            self.button_timer.setText(f"{formatted_time}")
        self.isTimerRunning = not self.isTimerRunning

    def updateTime(self):
        self.timeElapsed += 1
        formatted_time = TimeCheckBox.get_formatted_time(self.timeElapsed)
        self.button_timer.setText(f"{formatted_time}")

    @staticmethod
    def get_formatted_time(time_elapsed):
        minutes, seconds = divmod(time_elapsed, 60)
        formatted_time = f"{int(minutes)}:{seconds:02d}"
        return formatted_time

    def check(self):
        if self.checkbox.isChecked():
            self.isTimerRunning = True
        else:
            self.timeElapsed = 0
            self.isTimerRunning = True


if __name__ == '__main__':
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    main_window = TimeCheckBox()
    main_window.show()
    sys.exit(app.exec_())
