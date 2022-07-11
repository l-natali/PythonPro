def simple_num(n):
    for i in range(n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i
    return


for i in simple_num(100):
    print(i)
