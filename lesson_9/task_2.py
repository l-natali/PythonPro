func_list = []


def decor(f):
    func_list.append(f)
    return f


# @decor
# def summa(x, y):
#     return x + y


@decor
def mul(x):
    return x ** 2


@decor
def pow(x):
    return x ** 3


print(func_list)
x = [i for i in range(10)]
for func in func_list:
    print(list(map(func, x)))
