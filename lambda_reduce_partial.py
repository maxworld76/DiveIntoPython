from functools import partial, reduce


def test(a, b):
    return f"{a}:{b}"


def my_sum(c):
    return reduce(lambda x, y: x + y, c)


print(test(1, 2))
t1 = partial(test, b=10)
print(t1(1))

print(my_sum([1, 3, 4]))

print(list(filter(bool, [0, 1, 2])))
