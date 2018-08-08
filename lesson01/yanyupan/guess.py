import random

# num = int(input("请输入你猜的数字："))
# num = ""
# rnum = random.randint(0, 100)
# count = 0
# while num != rnum:
#     if count > 6:
#         print("您已猜错超过6次，请下回再试吧！")
#         break
#     else:
#         num = int(input("请输入你猜的数字："))
#         if num < rnum:
#             print("小了")
#         if num > rnum:
#             print("大了")
#         count += 1
#
# print("猜对了！")



# 使用random.randint生成0-100的随机数，0和100都包含在内
# rnum = random.randint(0, 100)
# print(rnum)
# count = 0
# while count < 6:
#     remain = remain - count
#     num = int(input("请输入你猜的数字："))
#     if num == rnum:
#         print("猜对了！")
#         exit()
#     elif num < rnum:
#         print("小了")
#     else:
#         print("大了")
#     count += 1
#
# print("您已猜错超过6次，请下回再试吧！")

# 输出两种格式：
# 1>"{}".format(对应的变量)     ---> {}有几个，后面的变量就要有几个
# 2>"%s" % (变量)               ---> %s表示占位符，可以是%s %d %f，对应表示：字符串，数字，符点数
#                                    后面的变量为对应的字符类型，如果只有一个占位符可以不用括号，
#                                    或直接拼接print("小了，你还有", str(remain), "次机会！")
#                                    如果多个必须括号括起来，","号分开："%s %s" %(变量1, 变量2)
rnum = random.randint(0, 100)
print(rnum)
totle = 6
count = 1

while count <= totle:
    remain = totle - count
    num = int(input("请输入你猜的数字："))
    if num == rnum:
        print("猜对了！")
        exit()
    elif num < rnum:
        print("小了，你还有{}次机会！".format(remain))
    else:
        print("大了，你还有%d次机会！" % remain)
        # print("大了，你还有", str(remain), "次机会！")
    count += 1

print("您已猜错超过6次，请下回再试吧！")

