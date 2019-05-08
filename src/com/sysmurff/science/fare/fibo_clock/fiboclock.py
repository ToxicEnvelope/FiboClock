import os
import time
import logging

class Stack(object):
    __len: int
    __stk: list

    def __init__(self) -> None:
        self.__len = 0
        self.__stk = []

    def peek(self) -> int:
        return self.__stk[-1]

    def push(self, itm: int) -> None:
        self.__stk.append(itm)

    def pop(self, idx: int) -> None:
        self.__stk.pop(idx)

    def reverse(self) -> list:
        self.__stk.reverse()
        return self.__stk

    def len(self) -> int:
        self.__len = self.__stk.__len__()
        return self.__len

    def print(self) -> str:
        return self.__dict__.__str__()

def fibo(idx: int) -> int:
    return idx if idx < 2 else fibo(idx=idx-2)+fibo(idx=idx-1)

def tick() -> int:
    st = int(time.time().__str__()[:10])
    stk.push(fibo(idx=ticks))
    et = int(time.time().__str__()[:10])
    return et-st

def log_tick() -> None:
    log.debug('-{}-{}-{}'.format(tick(), stk.len(), stk.peek()))


stk = Stack()
logging.basicConfig(filename='{0}/fibo-clock.log'.format(os.path.expanduser('~/Desktop/Git/FiboClock/logs')),
                    filemode='w',
                    level=logging.DEBUG)
log = logging.getLogger('fibo_clock')
ticks = 0
while True:
    log_tick()
    ticks += 1
