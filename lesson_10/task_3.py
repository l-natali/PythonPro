class Box:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = "+str(self.x)+", y = "+str(self.y)+", z = "+str(self.z)+" ]"

    @staticmethod
    def stat(x, y, z):
        return f'{x} x {y} x {z} = {x * y * z}'


a = Box(1, 2, 3)
b = Box(3, 4, 5)
print(a.stat(5, 6, 7))
print(Box.stat(5, 6, 7))
