from human import Human


class Student(Human):
    def __init__(self, name, surname, sex, group):
        super().__init__(name, surname, sex)
        self.group = group

    def __str__(self):
        return f'{super().__str__()}, group {self.group}'

    def say(self):
        return f'{super().say()}, world'


student_1 = Student('Ivan', 'Ivanov', 'male', '319BIT')
student_2 = Student('Oleh', 'Galtsov', 'male', '319BIT')
student_3 = Student('Veronika', 'Leonova', 'female', '319BIT')
student_4 = Student('Maryna', 'Frolova', 'female', '319BIT')
student_5 = Student('Serhiy', 'Maksymenko', 'male', '319BIT')
student_6 = Student('Ivan', 'Stiopochkin', 'male', '319BIT')
student_7 = Student('Nataliia', 'Lukiienko', 'female', '319BIT')
student_8 = Student('Anastasiia', 'Koval', 'female', '319BIT')
student_9 = Student('Ihor', 'Ivanchenko', 'male', '319BIT')
student_10 = Student('Lubov', 'Frolova', 'female', '319BIT')
