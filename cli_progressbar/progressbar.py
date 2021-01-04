# -*- coding: utf-8 -*-
"""
lightweight library to print progress bar in cli
"""
import sys
from typing import Union


class Progress:
    def __init__(self, goal: int = -1):
        self.goal = goal
        self.status = ''
        self.showing_status = ''
        self.longest_status = 0
        self.bar_len = 60
        self.fill = '█'
        self.zfill = '-'
        self.decimals = 1

    def set_status(self, status: str):
        if status == self.status:
            return
        self.status = status
        self.longest_status = max(len(status), self.longest_status)
        self.showing_status = status + ' ' * (self.longest_status - len(status))

    def update(self, count: int, status: str = ''):
        self.set_status(status)

        filled_len = int(round(self.bar_len * count / float(self.goal)))

        percents = round(100.0 * count / float(self.goal), self.decimals)
        bar = self.fill * filled_len + self.zfill * (self.bar_len - filled_len)

        text = '[%s] %s%s | %s/%s' % (bar, percents, '%', count, self.goal)
        if self.showing_status:
            text += ' | %s' % self.showing_status
        sys.stdout.write(text + '\r')
        sys.stdout.flush()

    def start(self, status: str = ''):
        self.update(0, status)

    def stop(self, status: str = ''):
        self.update(self.goal, status)
        print('')

    def iterate(self, _list: Union[list, dict], status: Union[str, callable] = ''):
        if self.goal < 0:
            self.goal = len(_list)

        for i, elem in enumerate(_list):
            status_txt = status(elem) if callable(status) else status
            self.update(i, status_txt)
            yield elem
