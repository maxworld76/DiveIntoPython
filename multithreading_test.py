from threading import Thread
import time


class myThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print("hello kitty")
        time.sleep(2)


p = myThread("meow")
p.start()
p.join()
print("exiting")
