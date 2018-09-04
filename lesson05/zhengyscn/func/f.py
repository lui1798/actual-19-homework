

'''
    f1
        x, y
        y, x

'''

def f1(x, y):
    return y, x


def f2(x, y, z):
    print(x, y, z)


# x, y = '2', '3'
# print(x, y)
#
# x, y = f1(x, y)
# print(x, y)

# 位置参数
# f2(2, 1, 3)

# 关键字参数
# f2(y=2, x=1, z=3)

# 位置参数 & 关键字参数
# 位置参数一定要放在关键字参数前面  @所有
# f2(2, z=5, y=3)
# f2(z=5, y=3, 2)
# f2(2, z=5, y=3)
# f2(x=2, 3, y=5)
# f2(5, x=2, y=3)

# 默认参数
# def f3(x=1, y=2, z=5):
#     print(x, y, z)
#     return
#
#
# msg = f3()
# print(msg)



# def f4(x, y, z=10, *args, **kwargs):
#     print(x)
#     print(y)
#     print(z)
#     print(args)    # tuple
#     print(kwargs)  # dict
#
#
#
# # f4(1, 3, 2, 5, 7, 8, zz=100, name='monkey', address='beijing')
# t = list(range(1, 6))
# d = {'name' : 'monkey', 'address' : 'beijing'}
# f4(8, *t, **d)

# def f5(kwargs):
#     print(kwargs)
#
# def f6(x, kwargs):
#     print(x)
#     print(kwargs)
#
#
# d = {'name' : 'monkey', 'address' : 'beijing'}
# f5(d)
#
# f6(**d)


