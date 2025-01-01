import time
from contextlib import contextmanager

# Контекстный менеджер, замеряющий время работы блока кода


class cm_timer_1:

    def __init__(self):
        self.exec_start = 0
        self.exec_end = 0

    def __enter__(self):
        self.exec_start = time.time()

    def __exit__(self, type, value, traceback):
        self.exec_end = time.time()
        print(f"time: {self.exec_end - self.exec_start}")


@contextmanager
def cm_timer_2():
    exec_start = time.time()
    try:
        yield exec_start
    finally:
        print(f"time: {time.time() - exec_start}")


if __name__ == "__main__":
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(5.5)
