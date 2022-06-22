from students import Students, st1, st2, st3, st4, st5, st6, st7, st8, st9, st10


class Group:
    def __init__(self, student: Students):
        self.student = student
        self.group = []

    def __str__(self):
        res = f'{self.student}'
        for i in self.group:
            tmp = f'{i}\n'
            res += tmp
        return res

    def add_student(self, student: Students):
        self.group.append(student)
        return

    def del_student(self, student: Students):
        self.group.remove(student)
        return

    def find_student(self, student: Students):
        if student.surname in self.group:
            return 'Yes'
        else:
            return 'No'

    def get_group(self):
        return self.group

    def count_students(self):
        res = 0
        for i in self.group:
            res += 1
        if res > 10:
            return 'error'
        return res

# student_find =
group = Group(st1)
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
group.del_student(st8)
group.del_student(st4)


print(group, 'Count students - ', group.count_students(), '\n', group.find_student(st2))
