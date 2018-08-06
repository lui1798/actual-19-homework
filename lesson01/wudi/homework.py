import random

# 1.9*9乘法表
print('############1.1 9*9乘法表################')

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}x{}={}".format(j, i, i * j), end=' ')

    print('')

# 2.一个100以内的数,6次机会,每次猜时,猜对了,太小了,太大了

print('############2.1 折半查找################')
# 2.1 折半查找
# 生成范围
start = 0
end = 100

randomNum = random.randint(start, end)
# 计数器
count = 0
print("randomNum=", randomNum)

while end >= randomNum >= start:
    count += 1
    target = (start + end) // 2
    if target == randomNum:
        print('猜对了,randomNum={},count={}'.format(randomNum, count))
        break
    elif target > randomNum:
        print('猜大了,target={}'.format(target))
        end = target
    else:
        print('猜小了,target={}'.format(target))
        start = target


# 2.2 手动输入

print('############2.2 手动输入################')
start = 0
end = 100

randomNum = random.randint(start, end)
# 计数器
count = 0
print("randomNum=", randomNum)


while True:
    target = int(input('请输入一个数字[0 - 100]:'))
    if target > 100:
        print('请输入一个0-100的数字.')
    elif target == randomNum:
        print('猜对了,randomNum=', randomNum);
    elif target < randomNum:
        print('猜小了')
    else:
        print('猜大了')

    count += 1
    if count >= 6:
        print('只能猜6次')
        break
