import timeit

test_code = '''
def fibonachi():
    first_number = 0
    second_number = 1

    def next_num():
        nonlocal second_number
        nonlocal first_number
        next_number = second_number + first_number
        first_number = second_number
        second_number = next_number
        return next_number
    return next_num

f = fibonachi()
for i in range(10):
    print(f(), end=' ')
'''

print(timeit.timeit(test_code, number=10))


test_code2 = '''
def fibo(n):
    first_number = 0
    second_number = 1
    i = 1
    res = [first_number]
    while i <= n:
        next_number = second_number + first_number
        first_number = second_number
        second_number = next_number
        i += 1
        res.append(next_number)
    return res


n = fibo(10)
print(n)
'''

print(timeit.timeit(test_code2, number=10))
