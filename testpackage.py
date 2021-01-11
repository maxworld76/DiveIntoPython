from mypackage.utils import mul
import inspect
import this


if __name__ == "__main__":
    print("running directly..")
    print(mul(2,3))
    print(inspect.getfile(this))
    import os
    print(os.listdir('D:\\Programs\\Python39\\lib\\'))
    import requests

    print(inspect.getfile(requests))

