#encoding:utf-8

# 打印乘法口诀
# 提示：尝试print(‘monkey’)与print(‘monkey’, end=‘’)的区别

i = 1
while i < 10:
    j = 1
    while j < i + 1:
        print('%s * %s = %s   ' %(j,i,j * i),end='')
        j += 1
    print('')
    i += 1
