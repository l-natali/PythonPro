func_list = []


def decor(f):
    func_list.append(f)
    return f


@decor
def summa(x, y):
    return x + y


@decor
def mul(x, y):
    return x - y


@decor
def pow(x, y):
    return x ** y


print(func_list)
