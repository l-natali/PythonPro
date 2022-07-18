class_list = []


def register(cls):
    class_list.append(cls)
    return cls


@register
class MyClass:

    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'x * y = {self.x}'

    def __mul__(self, other):
        return MyClass(self.x * other.x)


@register
class MyOtherClass:

    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'x - y = {self.x}'

    def __sub__(self, other):
        return MyOtherClass(self.x - other.x)


a = MyClass(5)
b = MyClass(3)
c = MyOtherClass(7)
d = MyOtherClass(12)
print(a * b)
print(c - d)
print(class_list)
