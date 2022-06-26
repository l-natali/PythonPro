class Person:
    def __init__(self, name: str, surname: str, sex):
        self.name = name.strip().title()
        self.surname = surname.strip().title()
        self.sex = sex

    def __str__(self):
        return f'{self.name} {self.surname}, {self.sex}'
