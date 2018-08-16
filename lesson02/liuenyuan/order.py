#!/usr/bin/env python3
#排序
def order(data):
    if len(data) <= 1:
        return data
    else:
        for i in range(0,len(data)):
            for j in range(i,len(data)):
                if data[i] < data[j]:
                    pit = data[i]
                    data[i] = data[j]
                    data[j] = pit
                j = j + 1
            i = i + 1
        return data
data = []
print("""
     请输入一些有理数，你可以一次或者多次进行输入，输入完毕后!!!按
     q & Q)退出程序
     s & S)展示已经输入的数
     o & O)输入完成进行排序
""")
while True:
    try:
        choose = input("""
        请输入你的选择！！！！
        (提示：可输入q、s、o、也可以输入有理数进行排序)        
        ： """)
        request = float(choose)
    except:
        if not choose:
            print("输入为空，请重新输入")
        elif choose == "q" and "Q":
            print("程序退出")
            break
        elif choose == "s" and "S":
            print("当前数据列表为{}".format(data))
        elif choose == "o" and "O":
            data = order(data)
            print("当前排序结果为{}".
            format(data))
        else:
            print("输入不和规，请重新输入")
    else:
        data.append(request)
        print("添加数据成功！！！继续输入你的选择")

