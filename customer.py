class Customer:
    def __init__(self, name, surname, phone_number, city):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.city = city

    def __str__(self):
        return f'{self.name} {self.surname}, {self.city}, phone number - {self.phone_number}'


customer1 = Customer('Ivan', 'Ivanov', 380937426846, 'Kyiv')
customer2 = Customer('Petr', 'Petrov', 380973583106, 'Odessa')
