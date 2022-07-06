from math import gcd


class ProperFraction:

    def __init__(self, x: int, y: int):
        if not y:
            raise ZeroDivisionError('Y must not be zero')
        elif not isinstance(x, int) or not isinstance(y, int):
            raise TypeError('Numbers must be integer')
        self.x = x
        self.y = y

    def __str__(self):
        res = gcd(self.x, self.y)
        self.x //= res
        self.y //= res
        return f'{self.x}/{self.y}'

    def __mul__(self, other):
        return ProperFraction(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return ProperFraction(self.x * other.y, self.y * other.x)

    def __add__(self, other):
        return ProperFraction(self.x * other.y + other.x * self.y, self.y * other.y)

    def __sub__(self, other):
        return ProperFraction(self.x * other.y - other.x * self.y, self.y * other.y)


a = ProperFraction(5, 10)
b = ProperFraction(1, 2)
n = a + b
m = a - b
s = a * b
d = a / b

print(n, m, s, d, sep='\n')
