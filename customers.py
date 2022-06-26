class Customers:
    def __init__(self, name, surname, phone, city):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.city = city

    def __str__(self):
        return f'{self.name} {self.surname}, phone number: {self.phone}, {self.city}'


c1 = Customers('Vitaliy', 'Lysenko', '0974732386', 'Mykolaiv')
c2 = Customers('Eugen', 'Maksymovich', '0508762855', 'Lviv')
