#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 登录用户
loginuser = ('admin', '111111')

# 用户信息列表
userlist = [
    [1, 'monkey', 20, '13266666666', 'beijing'],
    [2, 'li', 20, '13755544544', 'xian'],
    [3, 'wang', 20, '13734534678', 'shanghai'],
    [5, 'he', 20, '13534562356', 'hebei'],
    [5, 'he', 20, '13534562356', 'hebei'],
]

# 定义初始输入错误次数为0次
count = 0

# 当输入错误次数小于3次时可以进行正常的操作
while count < 3:
    user = input('\033[32m请输入账号：\033[0m')
    if user == loginuser[0]:
        # 当输入用户名正确时，重置错误次数为0次，允许密码输错三次
        count = 0
        # 当输入密码错误次数小于3次时可以进行相关操作
        while count < 3:
            passwd = input('\033[32m请输入密码：\033[0m')
            while passwd == loginuser[1]:
                op = input('\033[32m请输入你的操作[list add delete update find exit]：\033[0m')
                # 当用户输入list时，对用户信息列表进行显示
                if op == 'list':
                    # 如果用户信息列表为空时，给出提示
                    if len(userlist) == 0:
                        print('\033[33m目前用户信息列表为空，请选择其它操作！\033[0m')
                    # 如果用户信息列表不为空时，进行格式化输出
                    else:
                        # 显示方法分显示所有与分页显示，分页显示用户需输入每页记录数及要查看的页数
                        list_method = input('\033[32m请输分查看用户信息列表的方式[total page]：\033[0m')
                        if list_method == 'totle':
                            print('\033[4;34m' + 'id' + ' ' * 3 + 'name' + ' ' * 6 + 'age' + ' ' * 2 + 'tel' + ' ' * 12 + 'address' + ' ' * 13 + '\033[0m')
                            for x in userlist:
                                print('\033[34m{0:<5}{1:<10}{2:<5}{3:<15}{4:<20}\033[0m'.format(x[0], x[1], x[2], x[3],x[4]))
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
                                print('\033[4;34m' + 'id' + ' ' * 3 + 'name' + ' ' * 6 + 'age' + ' ' * 2 + 'tel' + ' ' * 12 + 'address' + ' ' * 13 + '\033[0m')
                                for x in userlist[per * (pg - 1):per * pg]:
                                    print('\033[34m{0:<5}{1:<10}{2:<5}{3:<15}{4:<20}\033[0m'.format(x[0], x[1], x[2],x[3], x[4]))
                            else:
                                print('\033[31m你输入页码超出范围，最大页数为{}！\033[0m'.format(totle_pg))
                        else:
                            print('\033[31m你输入有误！\033[0m')
                            continue


                # 当用户输入add时，对用户信息列表进行增加操作
                elif op == 'add':
                    user = input('\033[32m请输入要添加的用户信息[姓名  年龄  手机号  地址]：\033[0m').strip().split(' ')
                    # 根据用户信息列表的长度给用户ID定义不同的值，空时ID为1，不为空时ID为列表最后一行信息ID的值加1
                    if len(userlist) == 0:
                        user.insert(0, 1)
                    else:
                        # uids = [x[0] for x in userlist]
                        # new_id = max(uids) + 1
                        # user.insert(0, new_id)
                        uid = userlist[len(userlist) - 1][0] + 1
                        user.insert(0, uid)
                    # 添加新增的用户信息到列表中
                    userlist.append(user)

                # 当用户输入delete时进行删除操作
                elif op == 'delete':
                    uid = int(input('\033[32m请输入要删除的用户的ID：\033[0m'))
                    # 获取用户信息列表的所有ID值   x[0] for x in userlist  ---> 知识点：取值：x[0]  循环：for x in userlist  条件：可以增加条件
                    uids = [x[0] for x in userlist]
                    # 输入的用户ID在用户所有ID值列表中，则遍历用户信息列表删除对应的记录
                    if uid in uids:
                        for x in userlist:
                            if x[0] == uid:
                                userlist.remove(x)
                    # 输入ID不存在给出提示
                    else:
                        print('\033[31m对不起，你输入的用户ID号不存在！\033[0m')

                # 当用户输入update时进行更新操作
                elif op == 'update':
                    uid = int(input('\033[32m请输入要修改的用户的ID号：\033[0m'))
                    uids = [x[0] for x in userlist]
                    # 判断输入的ID值是否在用户所有ID值列表中
                    if uid in uids:
                        newuser = []
                        # 当输入的信息不全时不进行更新直接用户输入所有字段值
                        while len(newuser) < 4:
                            newuser = input('\033[32m请输入要修改后的用户信息[姓名  年龄  手机号  地址]：\033[0m').strip().split(' ')
                        # 遍历用户信息列表，当用户列表中第一个元素即ID值与输入的一致则给这条记录赋新的值
                        for x in userlist:
                            if x[0] == uid:
                                newuser.insert(0, uid)
                                userlist[userlist.index(x)] = newuser
                    else:
                        print('\033[31m对不起，你输入的用户ID号不存在！\033[0m')

                # 当用户输入find时进行查找操作
                elif op == 'find':
                    ukey = input('\033[32m请输入你想要查找的用户ID或姓名的关键字：\033[0m')
                    # 如果用户输入的是ID，利用异常处理对输入的信息进行转换整形转换，否则不做操作
                    try:
                        ukey = int(ukey)
                    except ValueError as e:
                        pass
                    for user in userlist:
                        # 如果用户输入的信息等于用户信息列表中用户的ID或用户姓名则显示出结果
                        if ukey == user[0] or ukey == user[1]:
                            print('\033[4;34m' + 'id' + ' ' * 3 + 'name' + ' ' * 6 + 'age' + ' ' * 2 + 'tel' + ' ' * 12 + 'address' + ' ' * 13 + '\033[0m')
                            print('\033[34m{0:<5}{1:<10}{2:<5}{3:<15}{4:<20}\033[0m'.format(user[0], user[1], user[2], user[3], user[4]))

                # 当用户输入exit时给出提示并退出
                elif op == 'exit':
                    print('\033[34m已经成功退出系统，欢迎再次光临！\033[0m')
                    exit()
                else:
                    print('\033[31m你输入的操作方式不存在！请重输！\033[0m')
                    continue

            print('\033[31m你输入的密码有误！\033[0m')
            count += 1
    else:
        print('\033[31m你输入的用户名有误！\033[0m')
        count += 1

# 最大错误次数超3次后退出并给出错误提示
print('\033[31m你输入错误已经超过3次！请过段时间再试！\033[0m')
