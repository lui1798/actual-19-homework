
'''
需求：
    用range 配合sum
    求和 1， 100
    求平均值 1， 100

    求 1,100的和 和1,100最小值得平均值
'''


# # 1. 生成1个从1开始到100的列表
# arr = range(1, 101)
#
# # 2. sum求和
# ssum = sum(arr)
#
# # 3. 打印
# print(ssum)


# # 1. 生成1个从1开始到100的列表
# arr = range(1, 101)
#
# # 2. sum求和
# ssum = sum(arr)
#
# # 3. 求长度
# length = len(list(arr))
#
# # 3. 打印平均值
# print(ssum/length)


# range_iter = list(range(1, 101))
#
# # 1. 求和
# ssum = sum(range_iter)
#
# # 2. 求最小值
# mmin = min(range_iter)
#
# # 3.求平均值
# avg = sum([ssum, mmin]) / len([ssum, mmin])
# print(avg)


# import random
# randint = [ random.randint(1, 8) for x in range(1, 25) ]
# print(randint)




'''
需求：
    arr = [7, 8, 5, 8, 5, 4, 7, 1, 3, 1, 1, 4, 8, 5, 2, 6, 7, 3, 3, 4, 5, 5, 1, 2]
    1. 求1 和 2分别出现的次数， 打印成 '1出现的次数为<xxx>, 2出现的次数为<xxx>.'
    2. 把1和2都删除掉， 上课时讲的面试题
    3. 返回一个列表类型，元素是偶数
'''

arr = [7, 8, 5, 8, 5, 4, 7, 1, 3, 1, 1, 4, 8, 5, 2, 6, 7, 3, 3, 4, 5, 5, 1, 2]
# print("1出现的次数为{}, 2出现的次数为{}.".format(arr.count(1), arr.count(2)))


# while 1 in arr or 2 in arr:
#     arr.remove(1)
#
# # while 2 in arr:
# #     arr.remove(2)
#
# print(arr)
#

# for i in arr:
# # for i in range(len(arr)):
#     if 1 in arr:
#         arr.remove(1)
#     elif 2 in arr:
#         arr.remove(2)
# print(arr)
#

# arr = [2, 2]
# # for i in arr:
# for i in range(len(arr)):
#     if 1 in arr:
#         arr.remove(1)
#     elif 2 in arr:
#         arr.remove(2)
# print(arr)

# arr = list(range(1, 11))
# cnt = 0
# for x in range(1, len(arr)):
#     arr.remove(x)
#     cnt += 1
# print(cnt)

















