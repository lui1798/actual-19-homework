import os


'''
    需求：
        1. 获取/etc/下每个文件 及文件大小
        2. 算出所有文件的和 以M为单位
'''

def fileWalk():
    sum_size = 0
    rootpath = "/etc"
    for dirpath, dirnames, filenames in os.walk(rootpath):
        # print(dirpath)  # 目录
        # print(dirnames) # 目录下的目录
        # print(filenames) # 目录下的所有文件
        # input()
        for file in filenames:
            abspath = os.path.join(dirpath, file)
            filesize = os.path.getsize(abspath)
            print("{:50} {:15}".format(abspath, filesize))
            sum_size += filesize

    return round(sum_size / 1024 / 1024, 2)  # 精确浮点位数





def main():
    sum_size = fileWalk()
    print(sum_size)





if __name__ == '__main__':
    main()
