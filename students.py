from person import Person


class Students(Person):
    def __init__(self, name, surname, sex, age: int, course):
        super().__init__(name, surname, sex)
        self.age = age
        self.course = course

    def __str__(self):
        return f'{super().__str__()}, age - {self.age}, course - {self.course}'


st1 = Students('Ihor', 'Petrenko', 'male', 20, 'Python Pro')
st2 = Students('Victoriia', 'Goncharenko', 'female', 24, 'Python Pro')
st3 = Students('Olena', 'Kondratiuk', 'female', 27, 'Python Start')
st4 = Students('Oleg', 'Grekalov', 'male', 19, 'Python Pro')
st5 = Students('Maryna', 'Frolova', 'female', 24, 'Python Pro')
st6 = Students('Nataliia', 'Lukiienko', 'female', 29, 'Python Pro')
st7 = Students('Sergiy', 'Maksymenko', 'male', 33, 'Python Start')
st8 = Students('Denis', 'Moskaev', 'male', 30, 'Python Start')
st9 = Students('Victor', 'Grinevich', 'male', 20, 'Python Pro')
st10 = Students('Anatoliy', 'Shylin', 'male', 32, 'Python Start')
