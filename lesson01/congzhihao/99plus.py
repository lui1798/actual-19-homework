###打印99乘法表
i=0
j=0
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i,j,i*j),end="  ")
    print("")