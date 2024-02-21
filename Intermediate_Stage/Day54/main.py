import time


def speed_calc_decorator(func):
    def wrapper():
        before_execution = time.time()
        func()
        after_execution = time.time()
        print(f'{func.__name__} speed run:  {after_execution-before_execution}s')
    return wrapper


@speed_calc_decorator
def fast_function():
    k = 1
    for i in range(1, 1001):
        k *= 1


@speed_calc_decorator
def slow_function():
    k = 1
    for i in range(1, 1000001):
        k *= 1


fast_function()
slow_function()
