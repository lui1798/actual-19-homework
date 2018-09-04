

'''
    1. 统计文件中ip出现的列表， 去重；11:03

    要求
        1. 必须有返回值
        2. 返回值得类型是列表

'''

LOGFILE = 'access.log'


def ip_set_v1():
    ip_set = []

    # 1. 打开文件
    fd = open(LOGFILE, 'r')

    # 2. 文件操作
    for line in fd:
        # 以空格进行分割
        line_str = line.strip('\n').strip()
        line_list = line_str.split()  # 默认以空格进行切分
        # print(line_list)
        ip = line_list[0]
        if ip not in ip_set:
            ip_set.append(ip)
        # print(line.strip('\n'))

    # 3. 关闭文件
    fd.close()

    return ip_set


def ip_set_v1():
    ip_set = set()

    # 1. 打开文件
    fd = open(LOGFILE, 'r')

    # 2. 文件操作
    for line in fd:
        # 以空格进行分割
        line_str = line.strip('\n').strip()
        line_list = line_str.split()  # 默认以空格进行切分
        # print(line_list)
        ip = line_list[0]
        ip_set.add(ip)
        # if ip not in ip_set:
        #     ip_set.append(ip)
        # print(line.strip('\n'))

    # 3. 关闭文件
    fd.close()

    return ip_set



'''
    1. 统计不同状态码出现的次数；

    要求
        1. 必须有返回值
        2. 返回值得类型是{}
        3. 不能有遗漏

'''
def get_http_status_count():
    status_code_dic = {}
    status_code_range = [ str(x) for x in range(200, 600) ]

    # 1. 打开文件
    fd = open(LOGFILE, 'r')

    # 2. 文件操作
    for line in fd:
        line_str = line.strip('\n').strip()
        line_list = line_str.split()  # 默认以空格进行切分
        status_code = line_list[8]  # 取出状态码

        '''
            1. 首先判断是否为数字 如果不是数字 直接跳过
            2. 判断状态码是否在取值范围之内， 如果在 就处理， 否则 就跳过
            
        '''
        if status_code.isdigit():
            if status_code in status_code_range:    # 判断状态码的是否在制定的范围
                # print(status_code)
                status_code_dic[status_code] = status_code_dic.get(status_code, 0) + 1
                # if status_code in status_code_dic:
                #     status_code_dic[status_code] += 1
                # else:
                #     status_code_dic[status_code] = 1
            else:
                status_code = line_list[-5]
                status_code_dic[status_code] = status_code_dic.get(status_code, 0) + 1
                # if status_code in status_code_dic:
                #     status_code_dic[status_code] += 1
                # else:
                #     status_code_dic[status_code] = 1
        else:
            status_code = line_list[-5]
            status_code_dic[status_code] = status_code_dic.get(status_code, 0) + 1
            # if status_code in status_code_dic:
            #     status_code_dic[status_code] += 1
            # else:
            #     status_code_dic[status_code] = 1

    # 3. 关闭文件
    fd.close()

    return status_code_dic


def get_http_status_count_v2():
    status_code_dic = {}
    status_code_range = [str(x) for x in range(200, 600)]

    # 1. 打开文件
    fd = open(LOGFILE, 'r')

    # 2. 文件操作
    for line in fd:
        line_str = line.strip('\n').strip()
        line_list = line_str.split()  # 默认以空格进行切分
        status_code = line_list[8]  # 取出状态码

        '''
            1. 首先判断是否为数字 如果不是数字 直接跳过
            2. 判断状态码是否在取值范围之内， 如果在 就处理， 否则 就跳过

        '''
        if status_code.isdigit() and status_code in status_code_range:  # 判断状态码的是否在制定的范围:
            # if status_code in status_code_range:  # 判断状态码的是否在制定的范围
                status_code_dic[status_code] = status_code_dic.get(status_code, 0) + 1
        #     else:
        #         status_code_dic[status_code] = status_code_dic.get(line_list[-5], 0) + 1
        # else:
        #     status_code_dic[status_code] = status_code_dic.get(line_list[-5], 0) + 1
        else:
            status_code_dic[status_code] = status_code_dic.get(line_list[-5], 0) + 1

    # 3. 关闭文件
    fd.close()

    return status_code_dic



def read_log():
    iplist = []
    fd = open('access.log', 'r')
    nginx = fd.readline()
    i = 0
    # 如果为空 则为假
    while nginx:
        nginx = fd.readline().strip()
        if not nginx:
            break
        request = nginx.split()
        try:
            print(request[0])
            print(request)
        except:
            print("[debug] {} {}".format(i, nginx))
            break
        finally:
            i += 1
    fd.close()



def fdwith():
    with open('access.log', 'r') as fd:
        for line in fd:
            print(line)
    print("end")

'''入口函数'''
def main():
    # msg = ip_set_v1()
    # print(msg)

    # msg = get_http_status_count()
    # print(msg)

    read_log()



if __name__ == '__main__':
    main()