from flowers import Flowers, f1, f2, f3
from customers import c1, c2


class Order:
    def __init__(self, flowers: Flowers):
        self.flowers = flowers
        self.items = []

    def __str__(self):
        return f'{self.flowers.name}, {self.items}'

    def add_item(self, flowers: Flowers):
        self.items.append(flowers)
        return

    def get_order(self):
        return self.items


order1 = Order(f1)
order1.add_item(f2.name)
order1.add_item(f1.name)
f1_num = 67
f2_num = 101
total_price1 = f1.price * f1_num + f2.price * f2_num

order2 = Order(f1)
order2.add_item(f3.name)
f3_num = 11
total_price2 = f3.price * f3_num

print('Customer', c1.name, c1.surname, 'basket:', '\n', order1.get_order()[0], '-', f2_num, '\n',
      order1.get_order()[1], '-', f1_num, '\n', 'Total price - ', total_price1, 'uah', 2 * '\n',
      'Customer', c2.name, c2.surname, 'basket:', '\n', order2.get_order()[0], '-', f3_num, '\n',
      'Total price - ', total_price2, 'uah')
