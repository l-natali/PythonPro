def my_func(seq, predicate):
    res = [predicate(i) for i in seq]
    return res


def func_one(i):
    return i ** 2


def func_two(i):
    return i * 2


seq = [1, 2, 3, 4, 5, 6]

print(my_func(seq, func_one), sum(my_func(seq, func_one)))
print(my_func(seq, func_two), sum(my_func(seq, func_two)))
