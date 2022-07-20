class MyDescriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError("field is read-only")


class MyClass:

    field = MyDescriptor('Text')

    def __str__(self):
        return self.field


a = MyClass()
print(a.field)
a.field = 'Text2'
