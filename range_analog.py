def range_analog2(r):
    if isinstance(r, int):
        start = 0
        stop = r - 1
        step = 1
        next_num = 0
        while next_num <= stop:
            yield next_num
            next_num = start + step
            start = next_num
        return

    if isinstance(r, tuple):
        if r[1] < r[0]:
            raise AttributeError
        if len(r) == 3:
            start = r[0]
            stop = r[1]
            step = r[2] or 1
            next_num = r[0]
            while next_num <= stop - 1:
                yield next_num
                next_num = start + step
                start = next_num
        elif len(r) == 2:
            start = r[0]
            stop = r[1]
            step = 1
            next_num = r[0]
            while next_num <= stop - 1:
                yield next_num
                next_num = start + step
                start = next_num
        else:
            raise IndexError('Function can take only 3 arguments')
        return


posl = range_analog2((0, 12, 3))
for i in posl:
    print(i)
