def cube(n):
    yield [x ** 2 for x in range(n)]
    return


n = cube(5)
print(list(n))
