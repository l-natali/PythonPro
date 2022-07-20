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
        if not isinstance(value, int):
            raise AttributeError('Value must be integer')
        self.__x = value


a = MyClass(3)
print(a.x)
a.x = 5
print(a.x)
a.x = 'f'
print(a.x)
