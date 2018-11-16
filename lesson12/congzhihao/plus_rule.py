
#99乘法表上
def plus99_up():
    for i in range(1,10):
        for j in range(i,10):
            print("{:2}*{:2}={:2}".format(i,j,i*j),end=' ')
        print()

#99乘法表下
def plus99_down():
    for i in range(1,10):
        for j in range(1,i+1):
            print("{:2}*{:2}={:2}".format(j,i,i*j),end=' ')
        print()

def main():
    plus99_up()
    print('-------------------------------')
    plus99_down()

if __name__ == '__main__':
    main()