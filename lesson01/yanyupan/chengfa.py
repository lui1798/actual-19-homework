# 打印乘法口诀
# 1 x 1 = 1
# 2 x 1 = 2    2 x 2 = 4
# .............
# 9 x 1 = 9    9 x 2 = 18    9 x 3 = 27 ......

# 要点：
# 1>print("输出信息", end="输出信息尾部增加的内容")，print("输出信息")默认end是换行：即"/n"
# 2>每行的列的值都小于等于行数，当列值与行值相等时才换行

row = 1
while row < 10:
    col = 1
    while col <= row:
        if col < row:
            print("{} * {} = {}".format(row, col, row * col), end="\t")
        else:
            print("{} * {} = {}".format(row, col, row * col))
        col += 1
    row += 1
