userinfo = []
'''
liang1 20 132xxx beijing
liang2 20 132xxx beijing
liang3 20 132xxx beijing
liang4 24 132xxx shenzhen
liang5 25 132xxx shenzhen
'''
login_tup = ('admin', '123456')
n = 1
while True:
    username = input('请输入管理员用户名: ')
    passwd = input('请输入密码: ')
    if username == login_tup[0] and passwd == login_tup[1]:
        print('登录成功!')
        while True:
            op = input('请输入以下选项add,delete,update,list,find: ')
            '''
             输入选项，增删改查 ，add，delete，update，list，find

            '''
            if op == 'add':
                user = input('请输入你要添加的信息: ')
                user_list = user.split(' ')
                if len(userinfo) == 0:
                    user_list.insert(0, 1)
                    userinfo.append(user_list)
                else:
                    uids = [x[0] for x in userinfo]
                    new_id = max(uids) + 1  # 取最大值加1作为序列号
                    user_list.insert(0, new_id)
                    userinfo.append(user_list)
            elif op == 'delete':
                uid = input("输入想要删除的序号: ")  # 输入想要删除的序列
                for x in userinfo:
                    if x[0] == int(uid):
                        userinfo.remove(x)
            elif op == 'update':
                print('---------显示已有的信息-----------')
                for i in userinfo:
                    for x in i:
                        print(x, end=' ')
                    print()
                uid = input('请输入你要更新的行号: ')
                for x in userinfo:
                    if x[0] == int(uid):
                        print(x)
                        newuser = input('请输入新的信息: ')
                        list1 = newuser.split(' ')
                        list1.insert(0, uid)
                        print(list1)
                        userinfo[int(uid) -1] = list1
                        print(userinfo)
            elif op == 'list':
                print('---------显示已有的信息-----------')
                for i in userinfo:
                    for j in i:
                        print(j, end=' ')
                    print()

            elif op == 'find':
                select = input("请输入查找的字: ")
                for i in userinfo:
                    if select in i:
                        print(i)
            elif op == 'exit':
                print("-------退出信息-----------")
                break
               # exit()
            elif op =='check':
                print(userinfo)
            else:
                print("无效的操作,请输入 add，delete，update，list，find,exit")
    else:
        n += 1
        print('错误的用户名或密码')
        if n > 3:  # 三次登录失败
            print('3次登录失败，退出!')
            break

