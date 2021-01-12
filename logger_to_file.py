class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.items = {}

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            with open(self.filename, 'a') as f:
                f.write(f'Called function {func}')
            return func(*args, *kwargs)

        return wrapped

    def __getitem__(self, item):
        return self.items.get(item)

    def __setitem__(self, key, value):
        self.items[key] = value


logger = Logger('test.log')

@logger
def some_func(a):
    print(a)


#logger = Logger('test.log')
#logger(some_func)

some_func('w')
some_func('g')

logger[4] = 42
print(logger[4])


class MyIter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return (self.current - 1)**2


for i in MyIter(0, 5):
    print(i)
d = MyIter(1,4)
d.start = 4
print(next(d))
print(d.start)
if 'start' in d.__dict__:
    print(f'start already defined: {d.start}')
del d.start
if 'start' in d.__dict__:
    print(f'start already defined: {d.start}')


