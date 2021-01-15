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

        pos = getattr(self, 'pos', 0)
        self.move_to(pos)
        sys.stdout.write(text + '\r')
        sys.stdout.flush()
        self.move_to(-pos)

    def move_to(self, line_count):
        if line_count:
            sys.stdout.write('\n' * line_count + '\x1b[A' * -line_count)
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


class MultiProgressManager:
    def __init__(self, progress_count: int = 0, progress_prefix: str = 'progress_'):
        self.progresses = []
        self.stopped_progresses = 0

        for index in range(progress_count):
            progress = Progress()
            self.append(progress, progress_prefix + str(index + 1))

    def append(self, progress: Progress, name: str = None):
        if progress not in self.progresses:
            self.progresses.append(progress)
            progress.pos = self.get_next_position()

            def finish(status):
                progress.update(progress.goal, status)
                self.stopped_progresses += 1
                if self.stopped_progresses == len(self.progresses):
                    print('\n' * (len(self.progresses) - 1))

            progress.stop = finish

            if name:
                setattr(self, name, progress)

    def get_next_position(self):
        return len(self.progresses) - 1
