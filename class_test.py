class A:
    def __init__(self, name):
        self.name = name

class B(A):
    def __init__(self, name, value):
        self.value = value
        super(B, self).__init__(name)

b = B("Name", "Value")
print(b.name, b.value)
print(issubclass(A, object))
a = A("fff")

print(isinstance(A(""), A))
