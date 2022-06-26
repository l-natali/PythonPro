from flowers import Flowers, f1, f2, f3
from customers import c1, c2, Customers


class Order:
    def __init__(self, customer: Customers):
        self.items = []
        self.am = []
        self.customer = customer

    def __str__(self):
        res = f'{self.customer}:\n'
        for i, item in enumerate(self.items):
            tmp = f'{item} uah * {self.am[i]} = {self.am[i] * item.price} uan\n'
            res += tmp
        res += f'Total price - {self.total_price()} uah'
        return res

    def add_item(self, flowers: Flowers, amount: int):
        if not isinstance(flowers, Flowers):
            raise TypeError
        self.items.append(flowers)
        self.am.append(amount)
        return

    def total_price(self):
        res = 0
        for i, item in enumerate(self.items):
            res += self.am[i] * item.price
        return res


order1 = Order(c1)
order2 = Order(c2)

order1.add_item(f1, 56)
order1.add_item(f2, 12)
order1.add_item(f1, 89)

order2.add_item(f3, 87)

print(order1, order2, sep='\n\n')

