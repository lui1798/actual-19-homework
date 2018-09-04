import datetime
import functools


def decoratorFunc(func):

    def wrapper(*args, **kwargs):
        print("Before login", datetime.datetime.now())
        print(args)
        func(*args)
        print("After login", datetime.datetime.now())
        return '123'

    # return functools.wraps(func)(wrapper)
    return wrapper
