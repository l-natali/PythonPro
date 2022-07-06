import logging
from students import Students, st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11
from config import STUDENT_LIMIT_IN_GROUP
from number_of_students import NumberOfStudentsError
from orderIterator import OrderIterator


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(filename)s %(message)s')

fileHandler = logging.FileHandler('group.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)


class Group:
    def __init__(self, course):
        self.course = course
        self.group = []

    def __str__(self):
        return '\n'.join(map(str, self.group))

    def __iadd__(self, other):
        if isinstance(other, Students):
            # Ошибка ниже почему-то не обрабатывается. Можете подсказать что тут неправильно?
            if len(self.group) > STUDENT_LIMIT_IN_GROUP:
                raise NumberOfStudentsError(len(self.group), f'is more then {STUDENT_LIMIT_IN_GROUP} '
                                                             f'you cannot add any students more')
            if other not in self.group:
                self.group.append(other)
        logger.info(f'Student {other.name} {other.surname} added to group')
        return self

    def __isub__(self, other):
        if isinstance(other, Students):
            if other in self.group:
                self.group.remove(other)
        logger.warning(f'Student {other.name} {other.surname} deleted from group')
        return self

    def __len__(self):
        return len(self.group)

    def __getitem__(self, item):
        if isinstance(item, slice):
            res = []
            start = item.start or 0
            stop = item.stop or len(self.group)
            step = item.step or 1

            if start < 0 or stop > len(self.group):
                raise IndexError
            for i in range(start, stop, step):
                res.append(self.group[i])
            return res

        if isinstance(item, int):
            if item < len(self.group):
                return self.group[item]
            raise IndexError
        raise TypeError()

    def __iter__(self):
        return OrderIterator(self.group)

    def find_student(self, surname):
        get_surname = [i for i in self.group if i.surname == surname]
        return get_surname if get_surname else None

    def get_group(self):
        return self.group

    def count_students(self):
        res = len(self.group)
        if res > STUDENT_LIMIT_IN_GROUP:
            return 'error'
        return res


if __name__ == '__main__':
    try:
        group = Group('Python Pro')
        group += st1
        group += st2
        group += st3
        group += st4
        group += st5
        group += st6
        group += st7
        group += st8
        group += st9
        group += st10
        group += st11
        group -= st4
        group -= st1

    except NumberOfStudentsError:
        logger.exception('NumberOfStudentsError')

for i, item in enumerate(group):
    print(i, item)
print('\nCount students - ', group.count_students(), '\n\nFound students:')
for i in group.find_student('Lukiienko'):
    print(i)

print('\nSliced group:')
x = group[3:7]
for item in x:
    print(item)
