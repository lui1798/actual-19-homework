
'''
a1 = [1, 2, 3]
a2 = a1

a1 == a2
a1 is a2

a3 = [1, 2, 3]

a3 == a2
a3 is a2



== 判断值
is 判断内存地址
'''

'''
a1 = [1, 2, 3]
a2 = a1
a2.append(4)

print("a1 {}".format(a1))
print("a2 {}".format(a2))
'''

'''
a1 = [1, 2, 3, [1, 2, 3]]
a2 = a1

# a2.append(4)  # [1, 2, 3, [1, 2, 3], 4]

# a2[-1].append(4)  # [1, 2, 3, [1, 2, 3, 4]]

# a2[-1] = "4"
a2[-1][-1] = 4
print("a1 {}".format(a1))


a1 = [1, 2, 3, [1, 2, 3]]
a2 = a1



a1[0] = 0
print("a2 {}".format(a2))


a1 = [1, 2, 3, [1, 2, 3]]
a2 = [1, 2, 3, [1, 2, 3]]
a2[-1][0] = 0
print("a1 {}".format(a1))


import copy

a1 = [1, 2, 3, ["11", "22", "33"]]
a2 = copy.copy(a1)

# print(a1)
# print(a2)


# a2[-1][2] = "abc"
# print("a1 {}".format(a1))
# print("a2 {}".format(a2))



# a1[0] = 0
# print("a1 {}".format(a1))
# print("a2 {}".format(a2))



a1[-1][-1] = "abc"
print("a1 {}".format(a1))
print("a2 {}".format(a2))



a = 100
b = 100

print(a == b)
print(a is b)


a1 = 1000
b1 = 1000

print(a1 == b1)
print(a1 is b1)



a = "hello workd 51reboot"
b = "hello workd 51reboot"

print(a == b)
print(a is b)



a1 = []
a2 = []
print(a1 == a2)
print(a1 is a2)
'''






















