from multiprocessing import Process
import time


class MyProc(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print("hello kitty")
        time.sleep(2)


p = MyProc("meow")
p.start()
p.join()
print("exiting")
