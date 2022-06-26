class NumberOfStudentsError(Exception):

    def __init__(self, num, desc):
        self.num = num
        self.desc = desc

    def __str__(self):
        return f'{self.num} {self.desc}'

