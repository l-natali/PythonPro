from person import Person


class Students(Person):
    def __init__(self, name, surname, sex, age: int,):
        super().__init__(name, surname, sex)
        self.age = age

    def __str__(self):
        return f'{super().__str__()}, age - {self.age}'


st1 = Students('Ihor', 'Petrenko', 'male', 20)
st2 = Students('Victoriia', 'Goncharenko', 'female', 24)
st3 = Students('Olena', 'Kondratiuk', 'female', 27)
st4 = Students('Oleg', 'Grekalov', 'male', 19)
st5 = Students('Maryna', 'Frolova', 'female', 24)
st6 = Students('Nataliia', 'Lukiienko', 'female', 29)
st7 = Students('Sergiy', 'Maksymenko', 'male', 33)
st8 = Students('Denis', 'Moskaev', 'male', 30)
st9 = Students('Victor', 'Grinevich', 'male', 20)
st10 = Students('Anatoliy', 'Shylin', 'male', 32)
st11 = Students('Sergiy', 'Lukiienko', 'male', 32)
