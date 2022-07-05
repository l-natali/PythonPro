from math import gcd


class ProperFraction:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} {self.y}'

    def __mul__(self, other):
        if not self.y or not other.y:
            raise ZeroDivisionError
        elif not isinstance(self.x, int) or not isinstance(self.y, int) \
                or not isinstance(other.x, int) or not isinstance(other.y, int):
            raise TypeError
        else:
            x = self.x * other.x
            y = self.y * other.y
            y1 = y // gcd(x, y)
            x1 = x // gcd(x, y)
            return f'{x1}/{y1}'

    def __truediv__(self, other):
        if not self.y or not other.y:
            raise ZeroDivisionError
        elif not isinstance(self.x, int) or not isinstance(self.y, int) \
                or not isinstance(other.x, int) or not isinstance(other.y, int):
            raise TypeError
        else:
            x = self.x * other.y
            y = self.y * other.x
            x1 = x // gcd(x, y)
            y1 = y // gcd(x, y)
            return f'{x1}/{y1}'

    def __add__(self, other):
        if not self.y or not other.y:
            raise ZeroDivisionError
        elif not isinstance(self.x, int) or not isinstance(self.y, int) \
                or not isinstance(other.x, int) or not isinstance(other.y, int):
            raise TypeError
        elif self.y == other.y:
            x = self.x + other.x
            y = self.y
            x1 = x // gcd(x, y)
            y1 = y // gcd(x, y)
            return f'{x1}/{y1}'
        else:
            y = self.y * other.y
            x = (self.x * other.y) + (self.x * other.y)
            x1 = x // gcd(x, y)
            y1 = y // gcd(x, y)
            return f'{x1}/{y1}'

    def __sub__(self, other):
        if not self.y or not other.y:
            raise ZeroDivisionError
        elif not isinstance(self.x, int) or not isinstance(self.y, int) \
                or not isinstance(other.x, int) or not isinstance(other.y, int):
            raise TypeError
        elif self.y == other.y:
            x = self.x - other.x
            y = self.y
            x1 = x // gcd(x, y)
            y1 = y // gcd(x, y)
            return f'{x1}/{y1}'
        else:
            x = (self.x * other.y) - (self.x * other.y)
            y = self.y * other.y
            x1 = x // gcd(x, y)
            y1 = y // gcd(x, y)
            return f'{x1}/{y1}'


a = ProperFraction(12, 2)
b = ProperFraction(3, 6)
n = a + b
m = a - b
s = a * b
d = a / b

print(n, m, s, d, sep='\n')
