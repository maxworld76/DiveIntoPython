import threading


class Point:
    def __init__(self, x, y):
        self._mutex = threading.RLock()
        self._x = x
        self._y = y

    def get(self):
        with self._mutex:
            return self._x, self._y

    def put(self, x, y):
        with self._mutex:
            self._x = x
            self._y = y


# OR

a = threading.RLock()
b = threading.RLock()


def foo():
    try:
        a.acquire()
        b.acquire()
    finally:
        a.release()
        b.release()
