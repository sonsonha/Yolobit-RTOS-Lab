"""
Lab 3 - Semaphore and task communication.
Producer: nut A phat su kien (give semaphore).
Consumer: nhan semaphore de doi trang thai indicator.
"""

from yolobit import *
import _thread


class BinarySemaphore:
    def __init__(self):
        self._lock = _thread.allocate_lock()
        self._flag = 0

    def give(self):
        self._lock.acquire()
        self._flag = 1
        self._lock.release()

    def take(self):
        got = 0
        self._lock.acquire()
        if self._flag == 1:
            self._flag = 0
            got = 1
        self._lock.release()
        return got


sem = BinarySemaphore()
_last_a = 0
indicator = 0


def task_init():
    global _last_a, indicator
    _last_a = 0
    indicator = 0
    display.show(Image.SQUARE_SMALL)


def task_producer_run():
    global _last_a
    current = 1 if button_a.is_pressed() else 0
    if current == 1 and _last_a == 0:
        sem.give()
        print("[LAB3][SEM] give from button A")
    _last_a = current


def task_consumer_run():
    global indicator
    if sem.take():
        indicator = 1 - indicator
        if indicator:
            display.show(Image.YES)
        else:
            display.show(Image.NO)
        print("[LAB3][SEM] take -> indicator =", indicator)
