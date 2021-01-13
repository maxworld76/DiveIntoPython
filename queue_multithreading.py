from queue import Queue
from threading import Thread


def run(q: Queue, name):
    print(f"[thread-{name}] starting")
    while True:
        task = q.get()
        if not task:
            break
        print(f"[thread-{name}] executing {task}")
    print(f"[thread-{name}] exiting")


q = Queue(5)
th1 = Thread(target=run, args=(q, 1))
th2 = Thread(target=run, args=(q, 2))
th1.start()
th2.start()

# put tasks
for i in range(1,50):
    q.put(i)

# need this to terminate threads
for t in range(2):
    q.put(None)

# wait for threads to finish
th1.join()
th2.join()

print("exit program")


