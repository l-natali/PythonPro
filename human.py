class Human:
    def __init__(self, name, surname, sex):
        self.name = name
        self.surname = surname
        self.sex = sex

    def __str__(self):
        return f'{self.name} {self.surname}, {self.sex}'

    def say(self):
        return 'Hello'
