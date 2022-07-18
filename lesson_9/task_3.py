def save_to_file(str_func):
    def save(*args):
        name = f'{MyClass.__name__}.txt'
        with open(name, 'a') as f:
            f.write(str_func(*args))
        return str_func(*args)
    return save


class MyClass:

    def __init__(self, text: str):
        self.text = text

    @save_to_file
    def __str__(self):
        return f'{self.text}\n'


text1 = MyClass('some text')
text2 = MyClass('another text')
print(text1, text2)
