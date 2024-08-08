import PyQt5.QtWidgets
from matplotlib.figure import Figure
import matplotlib.backends.backend_qt5agg as plt_qt5


class MyDiagramDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, window_name: str, canvas):
        super(MyDiagramDialog, self).__init__()
        #
        # self.fig = Figure(figsize=(5, 4), dpi=100)
        # self.ax = self.fig.add_subplot(111)
        # self.canvas = plt_qt5.FigureCanvasQTAgg(self.fig)
        # self.ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
        # self.canvas.draw()

        layout = PyQt5.QtWidgets.QVBoxLayout(self)
        layout.addWidget(canvas)

        self.resize(600, 400)
        self.setWindowTitle(window_name)


if __name__ == '__main__':
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = MyDiagramDialog('diagram')
    window.show()
    sys.exit(app.exec_())
