

s = 'name=monkey3, age=20'

s1="username='monkey123', age=23"

# 1. 将字符串按照逗号分隔列表
# for x in s.split(','):
#     print(x)
print(','.join(["{}='{}'".format(x.split('=')[0], x.split('=')[1]) for x in s.split(',')]))

# 2. 循环列表遍历每个元素 每个元素在按照等号分割， 字符串格式化输出就ok了

'''
# str -> list
str.split  

# list -> str 
str.join
'''