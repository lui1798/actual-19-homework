






# def f1():
#     global A
#     A = A + 1
#     print(A)
#
#
#
# f1()
# # print(A)


# def f2():
#     return A + 1
#
#
# # A = f2()
# # print(A)
# A = 101
# print(A)

# A = 100
#
#
# def f():
#     A = 200
#
#     def f2():
#         global A
#         A = A + 100
#         print(A)
#
#     f2()
#
#
# f()

# __file__ = 100
#
# def f():
#     # __file__ = 101
#
#     def f2():
#         # __file__ = 102
#         print(__file__)
#
#     f2()
#
#
# f()


#
# def wrapper():
#
#     def func():
#         print("hello world")
#
#
#     return func()
#
#
#
# f = wrapper()
# f