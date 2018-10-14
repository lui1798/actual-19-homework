

def wrapper(f):

    def func(x, y):
        print("一次请求")
        return f(x, y)

    return func


def ssum(x, y):
    return x + y


f = wrapper(ssum)
s = f(2, 3)
print(s)