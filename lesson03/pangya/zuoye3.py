import json, datetime, os

"""
用户登录账号：pangya
用户登录密码:123
"""
logininfo = ('pangya', '123')
count = 3  # count为密码重试次数

"""
判断用户是否被锁定
"""
unlock_flag = True  # 标记是否解锁，如果当前时间和锁住时间的差值小于1天，为False;大于1天，或者没有lock_time.txt文件，为True
if os.path.exists("lock_time.txt") == True:
    fd = open('lock_time.txt', 'r')
    membuf = fd.read()
    lock_time_str = json.loads(membuf)
    fd.close()
    lock_time = datetime.datetime.strptime(lock_time_str, "%Y-%m-%d %H:%M:%S")
    now_time = datetime.datetime.now()
    interval = now_time - lock_time
    if interval.days < 1:
        unlock_flag = False

"""
UserID               name                 tel                  address              age
1                    zs                   18312000000          hebei                25
2                    ls                   18909090902          beijing              35
3                    wu                   1586954512           shanxi               28
4                    zz                   1586954500           zhengzhou            18
5                    zq                   1222000022           luoyang              24
6                    p1                   1222000021           luoyang              39
7                    p2                   1222000023           luoyang              39
8                    p3                   1222000024           luoyang              39
9                    p4                   1222000025           luoyang              39
10                   p5                   1222000026           luoyang              39
11                   p7                   1222000027           luoyang              39
12                   p8                   1222000028           luoyang              39
备注：
每条用户信息以字典形式存放在列表中，列表以字符串格式存在user_message.txt文本中
"""

"""
用户密码未被锁定，输入密码进入用户管理系统
"""
fd = open('user_message.txt', 'r')  # 读取当前用户信息
membuf = fd.read()
userinfo = json.loads(membuf)
fd.close()
while count > 0:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == logininfo[0]:
        if unlock_flag == True:
            if password == logininfo[1]:
                print("****************************")
                print("\033[33m欢迎进入用户管理系统\033[0m")
                while True:
                    op = input(
                            "请输入你的操作选项（注：add:添加用户信息；delete：删除用户信息；update：更新用户信息；list：查看当前用户列表；find：搜索用户信息；write：保存用户信息；exit：退出用户系统)\n：")
                    if op == "add":
                        body = input("请输入你要添加用户的名字、电话、地址和年龄,并以空格隔开，（如wangli 18822888888 beijing 11）：")
                        user_list = body.split(' ')
                        if len(user_list) < 4:
                            print("\033[31m你添加的用户信息不完整\033[0m")
                        elif len(user_list) == 4:
                            title = ['seq', 'name', 'tel', 'address', 'age']
                            if len(userinfo) == 0:
                                user_list.insert(0, '1')
                                user_dict = dict((zip(title, user_list)))
                                userinfo.append(user_dict)
                            else:
                                uids = [int(x['seq']) for x in userinfo]
                                new_id = max(uids) + 1
                                user_list.insert(0, str(new_id))
                                user_dict = dict((zip(title, user_list)))
                                userinfo.append(user_dict)
                            print("\033[32m该用户添加成功\033[0m")
                        else:
                            print("\033[31m你添加的用户信息格式错误\033[0m")
                    elif op == "delete":
                        uid = input("请输入你要删除用户的ID：")
                        if uid in [x['seq'] for x in userinfo]:  # 列表生成式：List=[值，循环，条件]
                            for x in userinfo:
                                if x['seq'] == uid:
                                    userinfo.remove(x)
                                    print("\033[32m用户{}删除成功\033[0m".format(uid))
                        else:
                            print("\033[31m该用户ID不存在\033[0m")
                    elif op == "update":
                        body = input("请输入你要更新的用户ID、信息类型（name/tel/address/age）和更新内容，以空格隔开，（如：2 tel 18800990002）：")
                        user_update = body.split(' ')
                        if body == "":
                            print("\033[31m你输入的内容为空\033[0m")
                        elif len(user_update) == 3:
                            if user_update[0] in [x['seq'] for x in userinfo]:
                                for (i, y) in enumerate(userinfo):
                                    if user_update[0] == y['seq']:
                                        if user_update[1] in ['name', 'tel', 'address', 'age']:
                                            userinfo[i][user_update[1]] = user_update[2]
                                        else:
                                            print("\033[31m你要更改的信息类型不存在\033[0m")
                            else:
                                print("\033[31m该用户ID不存在\033[0m")
                        else:
                            print("\033[31m你输入的修改信息格式有误\033[0m")
                        print(userinfo)
                    elif op == "list":
                        try:
                            page_size = int(input("请输入每页显示个数（如 5）："))
                        except ValueError:
                            print("\033[31m你输入的内容不是数字\033[0m")
                        else:
                            if page_size == 0:
                                print("\033[31m每页显示个数不能为0\033[0m")
                            else:
                                page_num = len(userinfo) // page_size + 1
                                while True:
                                    try:
                                        n = int(input("请输入你要查看第几页（如 2）："))
                                    except ValueError:
                                        print("\033[31m你输入的内容不是数字\033[0m")
                                    else:
                                        if n in range(1, page_num + 1):
                                            for i in ['UserID', 'name', 'tel', 'address', 'age']:
                                                print("{:<20}".format(i), end=' ')
                                            print('')
                                            for x in userinfo[(n - 1) * page_size:n * page_size]:
                                                for j in x:
                                                    print("{:<20}".format(x[j]), end=' ')
                                                print('')
                                            op1 = input("是否继续查看（继续查看输入y/Y，退出查看按任意键）：")
                                            if op1.lower() != 'y':
                                                break
                                        else:
                                            print("\033[31m此页无用户信息\033[0m")
                    elif op == "find":
                        body = input("输入要搜索的信息（该信息可为User ID,Name,Tel,Address或Age，如：1/pangya/18822220011）：")
                        num = 0  # 标记不包含该搜索信息的用户个数
                        for i in ['UserID', 'name', 'tel', 'address', 'age']:
                            print("{:<20}".format(i), end=' ')
                        print('')
                        for x in userinfo:
                            if body in list(x.values()):
                                for j in x:
                                    print("{:<20}".format(x[j]), end=' ')
                                print('')
                            else:
                                num += 1
                        if num == len(userinfo):
                            print("\033[31m无这个信息\033[0m")
                        else:
                            print("\033[32m有这个信息\033[0m")
                    elif op == "write":
                        data2 = json.dumps(userinfo)
                        fd = open('user_message.txt', 'w')
                        fd.write(data2)
                        fd.close()
                        print("\033[32m用户信息保存成功\033[0m")
                    elif op == "exit":
                        fd = open('user_message.txt', 'r')
                        membuf = fd.read()
                        fd.close()
                        userinfo_0 = json.loads(membuf)
                        flag_exit = True  # 标记是否执行退出，当输入y时flag_exit为True，输入其他任意键时flag_exit为false；当不需要保存时，flag_exit为True
                        if userinfo_0 != userinfo:
                            op1 = input("你修改的用户信息未保存，仍继续退出请输入y/Y，返回输入任意键：")
                            if op1.lower() != 'y':
                                flag_exit = False
                        if flag_exit == True:
                            print("****************************")
                            print("\033[33m你已退出用户管理系统\033[0m")
                            break
                    else:
                        print("\033[31m你输入的选项不存在\033[0m")
                    continue
                break
            else:
                print("\033[31m你输入的密码错误!\033[0m")
                count -= 1
        else:
            print("\033[31m你的账号已被锁,请1天后重试\033[0m")
    else:
        print("\033[31m你输入的用户名不存在!\033[0m")
if count == 0:
    print("\033[31m你的账号已被锁\033[0m")
    lock_time = datetime.datetime.now()
    lock_time_str = lock_time.strftime("%Y-%m-%d %H:%M:%S")
    data3 = json.dumps(lock_time_str)
    fd = open('lock_time.txt', 'w')
    fd.write(data3)
    fd.close()
