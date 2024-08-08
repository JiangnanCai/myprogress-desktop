from matplotlib.figure import Figure
import matplotlib.backends.backend_qt5agg as plt_qt5


def get_canvas():
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    canvas = plt_qt5.FigureCanvasQTAgg(fig)
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
    canvas.draw()
    return canvas
