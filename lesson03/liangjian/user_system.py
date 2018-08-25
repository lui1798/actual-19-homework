import datetime
import json


userinfo = []
login_tup = ('admin','123456')
n = 1
while True:
    count = 0  # 登录次数
    adminInfo = ('admin', 'admin123')  # 管理员
    username = input("Please input your name: ")
    password = input("Please input your passwd: ")
    if username.strip() == login_tup[0] and password.strip() == login_tup[1]:
        print("\033[1;32m 欢迎登录管理员系统\033[0m")
        while True:
            flag = False
            new_user = {}
            op = input("please input your option [add,del,update,list,find,exit]")
            if op == 'add':
                new_user['name'] = input('please input your name: ')
                new_user['age'] = input('please input your age: ')
                new_user['tel'] = input('please input your tel: ')
                new_user['address'] = input('please input your address: ')
                if len(userinfo) == 0:
                    new_user['id'] = 1
                    userinfo.append(new_user)
                else:
                    uids = [int(x['id']) for x in userinfo]
                    new_id = max(uids) + 1
                    new_user['id'] = new_id
                    userinfo.append(new_user)
                print('添加用户')
            elif op == 'update':
                uid = int(input('请输入要更新的id: '))
                if uid in [x['id'] for x in userinfo]:
                    userinfo[uid-1]['id'] = input('please input your id: ')
                    userinfo[uid-1]['name'] = input('please input your name: ')
                    userinfo[uid-1]['age'] = input('please input your age: ')
                    userinfo[uid-1]['tel'] = input('please input your tel: ')
                    userinfo[uid-1]['address'] = input('please input your address: ')
                    print('更新成功')
                else:
                    print('没有这个ID,更新不了')
            elif op == 'del':
                uid = int(input('请输入要删除的id: '))
                if uid in [x['id'] for x in userinfo]:
                    for x in userinfo:
                        if x['id'] == uid:
                            userinfo.remove(x)
                else:
                    print('没有这个ID')
            elif op =='find':
                uid = int(input('请输入要查找的id: '))
                for x in userinfo:
                    if x['id'] == int(uid):
                        print('要查找到的用户是: {}'.format(x))

            elif op == 'list':
                for i in range(0, len(userinfo), 4):
                    print('----------用户查询结果----------')
                    print("id\tname\tage\ttel\taddress\t")
                    for u in userinfo[i:i + 4]:
                        print("{}\t{}\t{}\t{}\t{}".format(u['id'], u['name'], u['age'], u['tel'], u['address']))
                    print('----------------------------')
            elif op == 'exit':
                print('退出当前')
                break
            else:
                print('无效的操作')

    else:
        print('第{}次用户名或密码错误'.format(n))
        n += 1
        if n > 3:
            print('3次登录失败,退出')
            break

