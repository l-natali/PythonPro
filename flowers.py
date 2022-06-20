class Flowers:
    def __init__(self, name, color, height, price):
        self.name = name
        self.color = color
        self.height = height
        self.price = price

    def __str__(self):
        return f'Name - {self.name}\nColor - {self.color}\nHeight - {self.height} sm' \
               f'\nPrice - {self.price} uah'


f1 = Flowers('Rose', 'white', 51, 25)
f2 = Flowers('Lily', 'orange', 36, 15)
f3 = Flowers('Tulip', 'yellow', 45, 10)
