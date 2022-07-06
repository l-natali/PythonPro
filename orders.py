import logging
from flowers import Flowers, f1, f2, f3
from customers import c1, c2, Customers
from orderIterator import OrderIterator

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(filename)s %(message)s')

fileHandler = logging.FileHandler('order.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)


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
        logger.info(f'{self.customer.name} {self.customer.surname} add {amount} {flowers.color} {flowers.name}')

    def __iadd__(self, other: Flowers, amount: int):
        if not isinstance(other, Flowers):
            raise TypeError
        self.items.append(other)
        self.am.append(amount)
        logger.info(f'{self.customer.name} {self.customer.surname} add {amount} {other.color} {other.name}')
        return self, amount

    def __isub__(self, other: Flowers):
        if not isinstance(other, Flowers):
            raise TypeError
        if other in self.items:
            self.items.remove(other)
        logger.info(f'{self.customer.name} {self.customer.surname} remove {other.color} {other.name}')
        return self

    def __len__(self):
        return len(self.items)

    # def __getitem__(self, item):
    #     if isinstance(item, slice):
    #         res = []
    #         start = item.start or 0
    #         stop = item.stop or len(self.items)
    #         step = item.step or 1
    #
    #         if start < 0 or stop > len(self.items):
    #             raise IndexError
    #         for i in range(start, stop, step):
    #             res.append(self.items[i])
    #         return res
    #
    #     if isinstance(item, int):
    #         if item < len(self.items):
    #             return self.items[item]
    #         raise IndexError
    #     raise TypeError()

    def __iter__(self):
        return OrderIterator(self.items)

    def total_price(self):
        res = 0
        for i, item in enumerate(self.items):
            res += self.am[i] * item.price
        return res


if __name__ == '__main__':
    order1 = Order(c1)
    order2 = Order(c2)

    order1.add_item(f1, 56)
    order1.add_item(f2, 12)
    order1.add_item(f1, 89)
    order1.__iadd__(f1, 6)
    order1 -= f1

    order2.add_item(f3, 87)

# print(order1, order2, sep='\n\n')
print(c1)
for i in order1:
    print(i)

print(c2)
for i in order2:
    print(i)
# x = order1[1:]
#
# print('Slice order 1:')
# for i in x:
#     print(i)

