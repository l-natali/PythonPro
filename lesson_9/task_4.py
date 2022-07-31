import logging
import time
import timeit

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

fileHandler = logging.FileHandler('chronos.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)


def decor(ch):
    def func(*args, **kwargs):
        end = time.time()
        t = end - start
        logger.info(f'{fibo.__name__} was called')
        logger.info(f'Time for running is {t} sec')
        return ch(*args, **kwargs), t
    start = time.time()
    return func


@decor
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
    return res[-1]


print(fibo(23), fibo(6), sep='\n')
x = fibo(5)

