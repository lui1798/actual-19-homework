import copy


def f1(a):
    a1 = copy.deepcopy(a)
    a1.append(4)




a = [1, 2, 3]
f1(a)
print(a)

'''
如果是[1, 2, 3]说明是深拷贝
如果是[1, 2, 3，4]说明是浅拷贝
'''




