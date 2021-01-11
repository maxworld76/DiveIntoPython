def fibonachi(n):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a+b


for i in fibonachi(10):
    print(i)
