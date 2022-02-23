from student import Student, student_1, student_2, student_3, student_4, \
    student_5, student_6, student_7, student_8, student_9, student_10


class Group:
    def __init__(self, student: Student):
        self.student = student
        self.group_st = []

    def __str__(self):
        return f'{self.student.surname}, {self.group_st}'

    def add_student(self, student: Student):
        self.group_st.append(student)
        return

    def get_students(self):
        return self.group_st

    def del_students(self, student: Student):
        self.group_st.remove(student)

    def find_student(self, student: Student):
        if student.surname in self.group_st:
            return 'yes'
        else:
            return 'no'

    def count_students(self):
        if len(self.group_st) > 10:
            return 'error'


group = Group(student_1)
group.add_student(student_2.surname)
group.add_student(student_7.surname)
group.add_student(student_5.surname)
group.add_student(student_8.surname)
group.del_students(student_2.surname)

print(group.get_students(), group.find_student(student_6), group.count_students(), sep='\n')
