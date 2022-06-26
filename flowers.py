from price_error import NegativeNumberError


class Flowers:
    def __init__(self, name, color, height, price: int | float):
        if not isinstance(price, int | float):
            raise ValueError
        if price < 0:
            raise NegativeNumberError(price)
        self.name = name
        self.color = color
        self.height = height
        self.price = price

    def __str__(self):
        return f'Name - {self.name}, color - {self.color}, height - {self.height} sm, price - {self.price} uah'


try:
    f1 = Flowers('Rose', 'white', 51, 6)
    f2 = Flowers('Lily', 'orange', 36, '15')
    f3 = Flowers('Tulip', 'yellow', 45, 10)
except ValueError as error:
    print('Price must be integer', error, sep='\n')
except NegativeNumberError as error:
    print('Price must be positive', error, sep='\n')
