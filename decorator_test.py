import functools
log_name = 'log.txt'


def logger(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, ** kwargs):
            result = func(*args, **kwargs)
            with(open(filename, 'a')) as f1:
                f1.write(str(result) + '\n')
            return result
        return wrapped
    return decorator


@logger(log_name)
def summator(a):
    return sum(a)


print(summator([1, 2, 5]))
print(summator.__name__)
with(open(log_name, 'r')) as f:
    print("".join(f.readlines()))
