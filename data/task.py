import os
from collections import defaultdict

import pandas as pd


class Tasks(object):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    task_file = 'tasks.csv'
    task_path = os.path.join(root_dir, task_file)

    def __init__(self):
        self.datas = self._task

    @property
    def _task(self):
        df = pd.read_csv(self.task_path)
        tasks = defaultdict(list)
        for index, row in df.iterrows():
            task = row.to_dict()
            task_name = task.pop('task')
            subtask = SubTask(task)
            tasks[task_name].append(subtask)
        return tasks


class SubTask(object):
    def __init__(self, datas):
        self.datas = datas
        self.unit = datas.get('unit')
        self.name = datas.get('subtask')
        self.min_val = datas.get('min_val')
        self.max_val = datas.get('max_val')
        self.cur_val = datas.get('cur_val')
        self.deadline = datas.get('deadline')


task_datas = Tasks().datas
