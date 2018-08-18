logininfo = ('admin', '51reboot')
count = 3  # count为密码重试次数
'''
用户信息
UserID               name                 tel                  address              age
1                    zhangsan             15869565412          hebei                25
2                    lisi                 15869565012          beijing              25
3                    wangwu               1586954512           shanxi               28
'''
userinfo = [['1', 'zhangsan', '15869565412', 'hebei', '25'],
            ['2', 'lisi', '15869565012', 'beijing', '25'],
            ['3', 'wangwu', '1586954512', 'shanxi', '28']

            ]
# 用户id和age以字符串形式存放在列表中
while count > 0:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == logininfo[0] and password == logininfo[1]:
        print("****************************")
        print("\033[33m欢迎进入用户管理系统\033[0m")
        while True:
            op = input("请输入你的操作选项（注：add:添加用户信息；delete：删除用户信息；update：更新用户信息；list：查看当前用户列表；find：搜索用户信息；exit：退出用户系统)\n：")
            if op == "add":
                body = input("请输入你要添加用户的名字、电话、地址和年龄,并以空格隔开，（如wangli 18822888888 beijing 11）：")
                user_list = body.split(' ')
                if len(user_list) < 4:
                    print("\033[31m你添加的用户信息不完整\033[0m")
                elif len(user_list) == 4:
                    if len(userinfo) == 0:
                        user_list.insert(0, '1')
                        userinfo.append(user_list)
                    else:
                        uids = [int(x[0]) for x in userinfo]
                        new_id = max(uids) + 1
                        user_list.insert(0, str(new_id))
                        userinfo.append(user_list)
                    print("\033[32m该用户添加成功\033[0m")
                else:
                    print("\033[31m你添加的用户信息格式错误\033[0m")
            elif op == "delete":
                uid = input("请输入你要删除用户的ID：")
                if uid in [x[0] for x in userinfo]:  # 列表生成式：List=[值，循环，条件]
                    for x in userinfo:
                        if x[0] == uid:
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
                   if user_update[0] in [x[0] for x in userinfo]:
                       update_id = int(user_update[0])  # update为要更新的用户ID
                       type_list = ['name', 'tel', 'address', 'age']  # type_list为可以更改的类型列表，与用户信息列表中的类型顺序一致
                       uids = [int(x[0]) for x in userinfo]  # uids为系统里有的用户信息ID
                       if user_update[1] in type_list:
                            for i, j in enumerate(type_list):  # enumerate 函数用于遍历序列中元素以及它们的下标，故i表示信息类型在类型列表中的下标，j表示信息类型
                                if user_update[1] == j:
                                    userinfo[update_id - 1][i + 1] = user_update[2]  # 更新用户信息
                                    print("\033[32m更新成功\033[0m")
                       else:
                            print("\033[31m你要更改的信息类型不存在\033[0m")
                   else:
                        print("\033[31m该用户ID不存在\033[0m")
                else:
                    print("\033[31m你输入的修改信息格式有误\033[0m")
            elif op == "list":
                for i in ['UserID', 'name', 'tel', 'address', 'age']:
                    print("{:<20}".format(i), end=' ')
                print('')
                for x in userinfo:
                    for j in x:
                        print("{:<20}".format(j), end=' ')
                    print('')
            elif op == "find":
                body = input("输入要搜索的信息（该信息可为User ID,Name,Tel,Address或Age，如：1/pangya/18822220011）：")
                num = 0  # 标记不包含该搜索信息的用户个数
                for x in userinfo:
                    if body in x:
                        for i in ['UserID', 'name', 'tel', 'address', 'age']:
                            print("{:<20}".format(i), end=' ')
                        print('')
                        for j in x:
                            print("{:<20}".format(j), end=' ')
                        print('')
                    else:
                        num += 1
                if num == len(userinfo):
                    print("\033[31m无这个信息\033[0m")
                else:
                    print("\033[32m有这个信息\033[0m")
            elif op == "exit":
                print("****************************")
                print("\033[33m你已退出用户管理系统\033[0m")
                break
            else:
                print("\033[31m你输入的选项不存在\033[0m")
            continue
        break
    else:
        print("\033[31m密码错误!\033[0m")
        count -= 1
if count == 0:
    print("\033[31m你的账号已被锁\033[0m")
