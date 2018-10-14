def wrapper(f):

    def func(x, y):
        print("一次请求")
        return f(x, y)

    return func

@wrapper
def ssum(x, y):
    return x + y

s = ssum(2, 3)
print(s)