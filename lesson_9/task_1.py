def count_func(f):
    def counter(*args, **kwargs):
        counter.count += 1
        return f(*args, **kwargs)
    counter.count = 0
    return counter


@count_func
def summa(x, y):
    return x + y


print(summa(2, 3))
print(summa(3, 4))
print(summa(4, 5))
print('Function was called', summa.count, 'times')
