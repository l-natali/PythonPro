import datetime


class MyClass:

    def __init__(self, x):
        self.__x = x

    def __str__(self):
        return self.x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        with open('file.txt', 'a') as f:
            f.write(f'{datetime.datetime.now()} value was changed to {value}\n')
        self.__x = value


a = MyClass(4)
a.x = '3'
print(a.x)
a.x = 78
print(a.x)
