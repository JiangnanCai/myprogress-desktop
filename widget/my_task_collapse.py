from typing import Any, Dict

import PyQt5.QtWidgets

from widget.my_collapsebox import MyCollapseBox
from widget.my_progressbar import MyProgressBar
from utilis.diagram import get_canvas


class MyTaskCollapseWidget(MyCollapseBox):

    def __init__(self,
                 task_datas: Dict,
                 title: str = '',
                 parent: Any = None):
        super(MyTaskCollapseWidget, self).__init__(title, parent)

        progressbars = []

        for subtask in task_datas:
            progress_bar = MyProgressBar(title=subtask.name)
            progress_bar.canvas = get_canvas()
            progress_bar.setObjectName(subtask.name)
            progress_bar.setRange(subtask.min_val, subtask.max_val)
            progress_bar.setValue(subtask.cur_val)
            progressbars.append(progress_bar)
            self.addWidget(progress_bar)


if __name__ == '__main__':
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    collapsebox = MyTaskCollapseWidget('ffff')
    collapsebox.show()
    sys.exit(app.exec_())

