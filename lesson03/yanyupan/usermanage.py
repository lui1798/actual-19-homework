#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    userlist = [
        {'name' : 'monkey1', 'age':20, 'tel':'132xxx', 'address':'beijing', 'id':'1'},
        {'name' : 'monkey2', 'age':20, 'tel':'132xxx', 'address':'beijing', 'id':'2'},
        {'name' : 'monkey3', 'age':20, 'tel':'132xxx', 'address':'beijing', 'id':'3'},
    ]

    分页
    分页示例：
    page=1&page_size=10
    page=2&page_size=10
    page=3&page_size=10


    提示：
    list 1 10
    list 2 10
    list 3 10
    持久化
    import json

    # write
    fd = open('persistence.db', 'w')
    membuf = json.dumps(xxxxx) ### xxxxx是用户列表
    fd.write(membuf)
    fd.close()

    # read
    fd = open('persistence.db', 'r')
    data = fd.read()
    membuf = json.loads(data)
    fd.close()
    异常处理
    try:
        pass
    except:
        pass
    else:
        pass
    finally:
        pass

    一天之内不准超过三次
'''

import json, datetime

loginuser = ('admin', 111111)

# 初始化，从lockinfo.db读取被锁定的相关信息，如果没有该文件则创建并赋初始数据:{'lock_time': 0, 'count': 0}
try:
    fl = open('lockinfo.db', 'r')
except FileNotFoundError:
    fl = open('lockinfo.db', 'w+')
    membuf = json.dumps({'lock_time': 0, 'count': 0})
    fl.write(membuf)
finally:
    fl = open('lockinfo.db', 'r')
    lockdata = fl.read()
    lockinfo = json.loads(lockdata)
    fl.close()

# 初始化，从userlist.db读取用户列表信息，如果没有该文件则创建并赋初始数据:[]
try:
    fu = open('userlist.db', 'r')
except FileNotFoundError:
    fu = open('userlist.db', 'w+')
    membuf = json.dumps([])
    fu.write(membuf)
finally:
    fu = open('userlist.db', 'r')
    userdata = fu.read()
    userlist = json.loads(userdata)
    fu.close()

# 获取当前时间
cur_time = int(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

if lockinfo['lock_time'] == 0 or lockinfo['lock_time'] < cur_time:
    # 当锁定时间小于当前时间时把输入错误数置0
    if lockinfo['count'] == 3:
        lockinfo['count'] = 0

    while lockinfo['count'] < 3:
        user = (input('\033[32m请输入账号：\033[0m')).strip()
        if user == loginuser[0]:
            # 当输入用户名正确时，重置错误次数为0次，允许密码输错三次
            lockinfo['count'] = 0
            # 当输入密码错误次数小于3次时可以进行相关操作
            while lockinfo['count'] < 3:
                passwd = int(input('\033[32m请输入密码：\033[0m').strip())
                while passwd == loginuser[1]:
                    op = input('\033[32m请输入你的操作[list add del upd find exit]：\033[0m')
                    # 当用户输入list时，对用户信息列表进行显示
                    if op == 'list':
                        # 如果用户信息列表为空时，给出提示
                        if len(userlist) == 0:
                            print('\033[33m目前用户信息列表为空，请选择其它操作！\033[0m')
                        # 如果用户信息列表不为空时，进行格式化输出
                        else:
                            # 显示方法分显示所有与分页显示，分页显示用户需输入每页记录数及要查看的页数
                            list_method = input('\033[32m请输分查看用户信息列表的方式[total page]：\033[0m')
                            if list_method == 'total':
                                print('\033[4;34m' + 'id' + ' ' * 3 + 'name' + ' ' * 6 + 'age' + ' ' * 2 + 'tel' + ' ' * 12 + 'address' + ' ' * 13 + '\033[0m')
                                for x in userlist:
                                    print('\033[34m{0:<5}{1:<10}{2:<5}{3:<15}{4:<20}\033[0m'.format(x['id'], x['name'], x['age'], x['tel'], x['address']))
                            elif list_method == 'page':
                                per = int(input('\033[32m请输入每页包含的记录数：\033[0m'))
                                pg = int(input('\033[32m请输入你要查看的页码：\033[0m'))
                                if pg > 0 and per > 0:
                                    # 根据列表长度与每页的记录取余结果判断总页数，余数为0时，总页数等于整除数，否则需加1
                                    s = len(userlist) % per
                                    if s == 0:
                                        totle_pg = len(userlist) // per
                                    else:
                                        totle_pg = len(userlist) // per + 1
                                else:
                                    print('\033[31m你输入存在错误！\033[0m')
                                    continue

                                if pg <= totle_pg:
                                    print(
                                        '\033[4;34m' + 'id' + ' ' * 3 + 'name' + ' ' * 6 + 'age' + ' ' * 2 + 'tel' + ' ' * 12 + 'address' + ' ' * 13 + '\033[0m')
                                    for x in userlist[per * (pg - 1):per * pg]:
                                        print('\033[34m{0:<5}{1:<10}{2:<5}{3:<15}{4:<20}\033[0m'.format(x['id'], x['name'], x['age'], x['tel'], x['address']))
                                else:
                                    print('\033[31m你输入页码超出范围，最大页数为{}！\033[0m'.format(totle_pg))
                            else:
                                print('\033[31m你输入有误！\033[0m')
                                continue


                    # 当用户输入add时，对用户信息列表进行增加操作
                    elif op == 'add':
                        # 定义user字典获取用户输入数据
                        user = {}
                        user['name'] = input('\033[32m请输入所要添加用户的姓名：\033[0m').strip()
                        user['age'] = int(input('\033[32m请输入所要添加用户的年龄：\033[0m').strip())
                        user['tel'] = input('\033[32m请输入所要添加用户的手机号：\033[0m').strip()
                        user['address'] = input('\033[32m请输入所要添加用户的地址：\033[0m').strip()
                        # 根据用户信息列表的长度给用户ID定义不同的值，空时ID为1，不为空时ID为列表最后一行信息ID的值加1
                        if len(userlist) == 0:
                            user['id'] = 1
                        else:
                            uids = [x['id'] for x in userlist]
                            user['id'] = max(uids) + 1
                            # uid = int(userlist[len(userlist) - 1]['id']) + 1
                            # user['id'] = str(uid)
                        # 添加新增的用户信息到列表中
                        userlist.append(user)

                    # 当用户输入delete时进行删除操作
                    elif op == 'del':
                        if len(userlist) == 0:
                            print('\033[33m目前用户信息列表为空，请选择其它操作！\033[0m')
                            continue
                        else:
                            dlist = []
                            k = input('\033[32m请输入要删除的字段：\033[0m').strip()
                            v = input('\033[32m请输入要删除的字段对应的值：\033[0m').strip()
                            for user in userlist:
                                for x, y in user.items():
                                    if k == x and v == str(y):
                                        dlist.append(userlist.index(user))
                            if len(dlist) == 0:
                                print('\033[31m对不起，你输入的用户信息不存！\033[0m')
                                continue
                            else:
                                didx = 0
                                for idx in dlist:
                                    del userlist[idx - didx]
                                    print('\033[32m删除的用户信息成功！\033[0m')
                                    didx += 1

                    # 当用户输入update时进行更新操作
                    elif op == 'upd':
                        if len(userlist) == 0:
                            print('\033[33m目前用户信息列表为空，请选择其它操作！\033[0m')
                            continue
                        else:
                            # 先根据用户输入的信息找出要修改的用户信息表的所有索引存放于ulist列表中
                            ulist = []
                            k = input('\033[32m请输入要修改信息的依据字段：\033[0m').strip()
                            v = input('\033[32m请输入要修改信息该字段的值：\033[0m').strip()
                            for user in userlist:
                                for x, y in user.items():
                                    if k == x and v == str(y):
                                        ulist.append(userlist.index(user))

                            if len(ulist) == 0:
                                print('\033[31m对不起，你要修改的用户信息不存！\033[0m')
                                continue
                            else:
                                uk = input('\033[32m请输入要修改的字段：\033[0m').strip()
                                if uk == 'age':
                                    uv = int(input('\033[32m请输入该字段的值：\033[0m').strip())
                                else:
                                    uv = input('\033[32m请输入该字段的值：\033[0m').strip()
                                for idx in ulist:
                                    userlist[idx][uk] = uv
                                    print('\033[32m用户信息修改成功！\033[0m')

                    # 当用户输入find时进行查找操作
                    elif op == 'find':
                        if len(userlist) == 0:
                            print('\033[33m目前用户信息列表为空，请选择其它操作！\033[0m')
                            continue
                        else:
                            ulist = []
                            k = input('\033[32m请输入要查找所依据的字段：\033[0m').strip()
                            v = input('\033[32m请输入要该字段的值：\033[0m').strip()
                            for user in userlist:
                                for x, y in user.items():
                                    if k == x and v == str(y):
                                        ulist.append(userlist.index(user))

                            if len(ulist) == 0:
                                print('\033[31m对不起，你要查找的用户信息不存！\033[0m')
                                continue
                            else:
                                print('\033[4;34m' + 'id' + ' ' * 3 + 'name' + ' ' * 6 + 'age' + ' ' * 2 + 'tel' + ' ' * 12 + 'address' + ' ' * 13 + '\033[0m')
                                for idx in ulist:
                                    print('\033[34m{0:<5}{1:<10}{2:<5}{3:<15}{4:<20}\033[0m'.format(userlist[idx]['id'], userlist[idx]['name'], userlist[idx]['age'], userlist[idx]['tel'], userlist[idx]['address']))

                    # 当用户输入exit时给出提示并退出并将最新的用户信息更新到userlist.db中
                    elif op == 'exit':
                        fu = open('userlist.db', 'w+')
                        membuf = json.dumps(userlist)
                        fu.write(membuf)
                        fu.close()
                        print('\033[34m已经成功退出系统，欢迎再次光临！\033[0m')
                        exit()
                    else:
                        print('\033[31m你输入的操作方式不存在！请重输！\033[0m')
                        continue

                print('\033[31m你输入的密码有误！\033[0m')
                lockinfo['count'] += 1
        else:
            print('\033[31m你输入的用户名有误！\033[0m')
            lockinfo['count'] += 1

    # 最大错误次数超3次后退出给出错误提示并更新锁定信息文件lockinfo.db
    locktime = int((datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y%m%d%H%M%S'))
    fl = open('lockinfo.db', 'w+')
    lockinfo['lock_time'] = locktime
    membuf = json.dumps(lockinfo)
    fl.write(membuf)
    fl.close()
    print('\033[31m你输入错误已经超过3次！请过段时间再试！\033[0m')
else:
    print('\033[31m由于你之前输入错误超3次，还处于被锁定！锁定终止时间为：{}\033[0m'.format(lockinfo['lock_time']))

