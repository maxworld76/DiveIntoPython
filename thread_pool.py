from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random


def f(name):
    print(f"name: {name} is running")
    time.sleep(random.randint(0, 4))
    return name


# shutdown() on exit
with ThreadPoolExecutor(max_workers=3, thread_name_prefix='my_th_') as pool:
    results = [pool.submit(f, i) for i in range(5)]

    for future in as_completed(results):
        print(f"completed: {future.result()}")
