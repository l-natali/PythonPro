from students import Students, st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11
from config import STUDENT_LIMIT_IN_GROUP
from number_of_students import NumberOfStudentsError


class Group:
    def __init__(self, course):
        self.course = course
        self.group = []

    def __str__(self):
        return '\n'.join(map(str, self.group))

    def add_student(self, student: Students):
        if len(self.group) > STUDENT_LIMIT_IN_GROUP:
            raise NumberOfStudentsError(len(self.group), 'is more then 10, you cannot add any students more')
        elif student not in self.group:
            self.group.append(student)
        return

    def del_student(self, student: Students):
        if student in self.group:
            self.group.remove(student)
        return

    def find_student(self, surname):
        get_surname = [i for i in self.group if i.surname == surname]
        return get_surname if get_surname else None

    def get_group(self):
        return self.group

    def count_students(self):
        res = 0
        for i in self.group:
            res += 1
        if res > 10:
            return 'error'
        return res


group = Group('Python Pro')
group.add_student(st1)
group.add_student(st2)
group.add_student(st3)
group.add_student(st4)
group.add_student(st5)
group.add_student(st6)
group.add_student(st7)
group.add_student(st8)
group.add_student(st9)
group.add_student(st10)
group.add_student(st11)
group.add_student(st1)
group.del_student(st8)
group.del_student(st4)
group.add_student(st11)


print(group, '\nCount students - ', group.count_students(), '\n\nFound students:')
for i in group.find_student('Lukiienko'):
    print(i)
