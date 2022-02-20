from books import book1, book2
from customer import customer1, customer2


class Order:
    def __init__(self, cust, product, kol1, kol2):
        self.cust = cust
        self.product = product
        self.kol1 = kol1
        self.kol2 = kol2

    def __str__(self):
        return f'{self.cust} ordered:\n {self.product}\n amount - {self.kol1} amount - {self.kol2}'

    def summa(self):
        return (self.kol1 * book1.price) + (self.kol2 * book2.price)


order1 = Order(f'{customer1.name} {customer1.surname}', f'{book1.author}, {book1.book_name}', 1, 0)
order2 = Order(f'{customer2.name} {customer2.surname}', f'{book2.author}, {book2.book_name}', 0, 2)
order3 = Order(f'{customer1.name} {customer1.surname}', f'{book1.author}, {book1.book_name}\n {book2.author}, {book2.book_name}', 2, 1)

print(order1, '\n', 'summa - ', order1.summa(), '\n')
print(order2, '\n', 'summa - ', order2.summa(), '\n')
print(order3, '\n', 'summa - ', order3.summa())
