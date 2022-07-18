def decor(cls):
    def param(*args):
        n = input('Text - ')
        return f'{n} {cls(*args)}'
    return param


@decor
class MyClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x * y = {self.mul()}'

    def mul(self):
        return self.x * self.y


a = MyClass(3, 5)
print(a)
