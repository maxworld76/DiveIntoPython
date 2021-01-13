from multiprocessing import Process
import time
import os


def f(name):
    print(name)
    time.sleep(3)


print("pid = {}".format(os.getpid()))
p = Process(target=f, args=("test",))

print("starting new process")
p.start()
print("started")
print("waiting for chils proce to finish..")
p.join()
print("exiting program")
