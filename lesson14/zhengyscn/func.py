
'''
nums = range(1, 10)

# 列表解析式
print([ x for x in nums if x % 2 == 0 ])

# filter过滤
# print(list(filter(lambda x : x % 2 == 0, nums)))

def func1(x):
    return x % 2 == 0

print(list(filter(func1, nums)))
'''


'''
    [1, 3, 5, 7]
    [2, 4, 6, 8]
    [3, 6, 9, 12]



print(list(map(lambda x,y,z:x+y+z, range(1, 100, 2), range(2, 100, 2), range(3, 100, 3))))
'''


from functools import reduce

print(reduce(lambda x, y: x+y, range(1, 101)))


