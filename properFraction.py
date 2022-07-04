from math import gcd


class ProperFraction:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} {self.y}'

    def gcd(self):
        gc = gcd(self.x, self.y)
        return gc

    def __mul__(self, other):
        if not self.y or not other.y:
            raise ZeroDivisionError
        elif not isinstance(self.x, int) or not isinstance(self.y, int) \
                or not isinstance(other.x, int) or not isinstance(other.y, int):
            raise TypeError
        else:
            x = self.x * other.x
            y = self.y * other.y
            return f'{x}/{y}'

    def __truediv__(self, other):
        if not self.y or not other.y:
            raise ZeroDivisionError
        elif not isinstance(self.x, int) or not isinstance(self.y, int) \
                or not isinstance(other.x, int) or not isinstance(other.y, int):
            raise TypeError
        else:
            x = self.x * other.y
            y = self.y * other.x
            return f'{x}/{y}'

    def __add__(self, other):
        if not self.y or not other.y:
            raise ZeroDivisionError
        elif not isinstance(self.x, int) or not isinstance(self.y, int) \
                or not isinstance(other.x, int) or not isinstance(other.y, int):
            raise TypeError
        elif self.y == other.y:
            x = self.x + other.x
            y = self.y
            return f'{x}/{y}'
        else:
            y = self.y * other.y
            x = (self.x * other.y) + (self.x * other.y)
            return f'{x}/{y}'

    def __sub__(self, other):
        if not self.y or not other.y:
            raise ZeroDivisionError
        elif not isinstance(self.x, int) or not isinstance(self.y, int) \
                or not isinstance(other.x, int) or not isinstance(other.y, int):
            raise TypeError
        elif self.y == other.y:
            x = self.x - other.x
            y = self.y
            return f'{x}/{y}'
        else:
            x = (self.x * other.y) - (self.x * other.y)
            y = self.y * other.y
            return f'{x}/{y}'


a = ProperFraction(3, 5)
b = ProperFraction(1, 2)
n = a + b
m = a - b
s = a * b
d = a / b

print(n, m, s, d, sep='\n')
