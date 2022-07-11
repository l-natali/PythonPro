def geom_prog(m, n):
    first_num = 1
    i = 1
    while i <= n:
        next_num = first_num * m
        first_num = next_num
        i += 1
        yield next_num
    return


for i in geom_prog(4, 10):
    print(i)
