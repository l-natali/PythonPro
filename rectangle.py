class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def square(self):
        return self.x * self.y

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __add__(self, other):
        return Rectangle(1, self.square() + other.square())

    def __mul__(self, other: int):
        return Rectangle(1, self.square() * other)


r1 = Rectangle(int(input('1 high=')), int(input('1 width=')))
r2 = Rectangle(int(input('2 high=')), int(input('2 width=')))
eq = r1 == r2
gt = r1 > r2
lt = r1 < r2
r3 = r1 + r2
sq_r1 = r1 * 2
sq_r2 = r2 * 3


print(' Is rectangles equal? - ', eq, '\n', 'Is rectangle 1 grater than rectangle 2? - ', gt, '\n',
      'Is rectangle 1 les than rectangle 2? - ', lt, '\n', 'Sum of squares =', r3, '\n',
      'Raised square 1 -', sq_r1, '\n', 'Raised square 2 -', sq_r2)

