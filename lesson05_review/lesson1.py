

# 这是一个注释信息1

'这是一个注释信息1'

"这是一个注释信息1"

'''这是一个注释信息1'''

"""这是一个注释信息1"""

# print("hello world")

'''
    false and true  -> false
    
    not (2 + 3 == 6 and 1 + 1 == 2)
    
    
    2 + 3 == 6 false
    1 + 1 == 2 true
    false and true -> false
    not false -> true
'''

# if not (2 + 3 == 6 and 1 + 1 == 2):
#     print("true")
# else:
#     print('false')

# for i in range(10):
#     for x in '123456':
#         break
#         print(x)
# else:
#     print("else")


# if 1:
#     print('true')


# while 0:
#     print("true")


# s = '123456789'
# for x in s:
#     if int(x) == 6:
#         continue  # 跳过本次循环
#     print(x)
#
# print("for end")

# for x in s:
#     if int(x) == 8:
#         break  # 跳出当前循环
#     print(x)
#
# print("for end")


# if True:
#     print(1)
# else:
#     pass


'''
    需求：
    生成长度为10的随机数
'''
import random
# # 1. 定义一个字符串变量
# s = ''
#
# # 2. 循环10次
# for x in range(10):
# # 3. 生成一个随机数
#     randint = random.randint(0, 9)
#     s = s + str(randint)
# # 4. 打印这个字符串变量
# print(s)

# print(random.randint(1000000000, 9999999999))


'''
需求：
range
生成一个偶数的字符串02468
'''

# # 1. 定义一个空的字符串
# s = ''
#
# # 2. 对range(0, 9)循环
# for x in range(0, 9):
#
# # 3. 对循环的元素% 求偶数
#     if x % 2 == 0:
#
# # 4. 拼接字符串
#         s = s + str(x)
#
# # 5. 打印这个字符串变量
# print(s)

# 1. 生成一个偶数列表 [0, 2, 4, 6, 8]
arr = range(0, 9, 2)

# 2. 类型转换成它['0', '2', '4', '6', '8']
arr_string = [ str(x) for x in arr ] # 推导式 列表解析式

# 3. 转换成我们要的结果 '02468'
s = ''.join(arr_string)
print(s)






















