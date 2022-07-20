import abc


class AbstractValidator(abc.ABC):

    @abc.abstractmethod
    def validate(self, value):
        """Validate if number is simple"""


class NumberValidator(AbstractValidator):

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def validate(self, value):
        if value > 1:
            for i in range(2, int(value / 2) + 1):
                if (value % i) == 0:
                    return False
            else:
                return True
        else:
            return False


class NonInherit:

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def validate(self, value):
        if value > 1:
            for i in range(2, int(value / 2) + 1):
                if (value % i) == 0:
                    return False
            else:
                return True
        else:
            return False


AbstractValidator.register(NonInherit)

number = NumberValidator(5)
print(number.validate(6))

number2 = NonInherit(6)
print(number2.validate(7))
