#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2018/8/20
# @Author    : Roger
# @File      : usermgt_les3.py
# @Software  : PyCharm
# @Desc      : 用户管理系统

import datetime
import json

# 登录用户名和密码
logininfo = {'name': 'admin', 'password': 123456}

try:
    fd = open('user.db', 'r')
    data = fd.read()
    userlist = json.loads(data)
    fd.close()
    # print(userlist)
except Exception as e:
    print(e)

# userlist = [{"name": "asa", "age": "12", "tel": "828272881", "address": "shanghai"},
#             {"name": "jj", "age": "26", "tel": "2781788712721", "address": "beijing"},
#             {"name": "nn", "age": "26", "tel": "1287261", "address": "xian"},
#             {"name": "Eo", "age": "76", "tel": "28276151", "address": "QINGDAO"},
#             {"name": "YY", "age": "25", "tel": "2827615154", "address": "zude"},
#             {"name": "Hq", "age": "72", "tel": "27165272819", "address": "memo"},
#             {"name": "TT", "age": "25", "tel": "mm", "address": "hefei"},
#             {"name": "dd", "age": "25", "tel": "817166182", "address": "hangzhou"},
#             {"name": "TTT", "age": "42", "tel": "261617118", "address": "jinan"},
#             {"name": "iao", "age": "27", "tel": "289272165", "address": "jinan"},
#             {"name": "pl", "age": "25", "tel": "2927615111", "address": "dalian"},
#             {"name": "erer", "age": "23", "tel": "09876555261", "address": "fushun"}]
count = 0
# 定义结束时间为一天后的现在
etime = (datetime.datetime.now() + datetime.timedelta(minutes=1 * 60 * 24)).strftime('%F %T')
while count < 3:
    username = input('please input usernmae:')
    password = input('please input password:')
    try:
        # 验证用户名密码
        if username.strip() == logininfo['name'] and int(password.strip()) == logininfo['password']:
            print('-------------------usage---------------------')
            print('list: list all users\'s information')
            print('add: add a user\'s information')
            print('update: update a user\'s information by name ')
            print('delete: delete a user\'s information by id')
            print('find: find a user\'s information by id or name')

            while True:
                op = input('please input action:list or add or update or delete or find or exit:').upper()
                if op == 'LIST':
                    # '''
                    #     -----------------------------
                    #     id name age tel    address
                    #     -----------------------------
                    #     1 monkey 28 132xxx beijing
                    #     1 zhengyscn 21 135xxx shanghai
                    #     1 wd 28 131xxx zhengzhou
                    #     1 xuegao 28 139xxx shandong
                    #     -----------------------------
                    # '''
                    # 总记录数
                    tot_recode = len(userlist)
                    print(
                        '----------------------------------------------------------------------------------------------------')
                    print('{:2}  {:10}  {:4}  {:20}  {:20}'.format('id', 'name', 'age', 'tel', 'address'))

                    if len(userlist):
                        for user in userlist:
                            print('{:2}  {:10}  {:4}  {:20}  {:20}'.format(userlist.index(user), user['name'],
                                                                           user['age'], user['tel'], user['address']))
                    print(
                        '----------------------------------------------------------------------------------------------------')

                elif op == 'ADD':
                    # '''
                    #     monkey 28 132xxx beijing
                    # '''
                    # 添加时未做年龄手机号判断
                    namelist = []
                    flag = True
                    for user in userlist:
                        namelist.append(user['name'])
                    while flag == True:
                        newname = input('please input name:')
                        if newname in namelist:
                            print('Name aleady in list.please input again.')
                        else:
                            flag = False
                    newage = input('please input age:')
                    newtel = input('please input telphone:')
                    newaddress = input('please input city:')
                    userlist.append({'name': newname, 'age': newage, 'tel': newtel, 'address': newaddress})
                    print('Input done.')

                elif op == 'UPDATE':
                    # '''
                    #     monkey 28 132xxx beijing
                    # '''
                    name1 = input('whose information you want to change:')
                    flag1 = True
                    flag2 = True
                    namelist = []
                    # 取出现有所有的name，组成一个list
                    for user in userlist:
                        namelist.append(user['name'])
                    if name1 not in namelist:
                        print('User not found!')
                    else:
                        for user in userlist:
                            if name1 == user['name']:
                                # 如果不为True,就停止更新其他内容,更新时未做年龄手机号判断
                                while flag1 == True:
                                    # 收集更新类型
                                    chtype = input(
                                        'please input the type you want to change:(name or age or tel or address)').upper().strip()
                                    if chtype == 'NAME':
                                        # 如果不是True,就结束更新
                                        while flag2 == True:
                                            newname = input('please input true name:')
                                            if newname in namelist:
                                                print('Name aleady in list.please input again.')
                                            else:
                                                flag2 = False
                                        user['name'] = newname
                                    elif chtype == 'AGE':
                                        newage = input('please input true age:')
                                        user['age'] = newage
                                        print('%s\'s new age is %s' % (user['name'], newage))
                                    elif chtype == 'TEL':
                                        newtel = input('please input true telphone:')
                                        user['tel'] = newtel
                                        print('%s\'s new tel is %s' % (user['name'], newtel))
                                    elif chtype == 'ADDRESS':
                                        newaddress = input('please input true address:')
                                        user['address'] = newaddress
                                        print('%s\'s new address is %s' % (user['name'], newaddress))
                                    else:
                                        print('Input error')
                                    flag1 = input('Do you need to continue changing ？y or n (defaut n)')
                                    if not flag1:
                                        flag1 = False



                elif op == 'DELETE':
                    # '''
                    #     delete 1
                    # '''
                    flag = ''
                    try:
                        delid = int(input('Please enter the ID number you want to delete:'))
                        del userlist[delid]
                    except Exception as e:
                        print(e)

                elif op == 'FIND':
                    # '''
                    #     find 1
                    #     find monkey
                    # '''
                    # 取出现有所有的name，组成一个list
                    namelist = []
                    for user in userlist:
                        namelist.append(user['name'])
                    info = input('Please enter the ID or name you want to query:')
                    try:
                        # 如果是名字，就找到名字的索引号
                        if info in namelist:
                            print('{:2}  {:10}  {:4}  {:20}  {:20}'.format(namelist.index(info),
                                                                           userlist[namelist.index(info)]['name'],
                                                                           userlist[namelist.index(info)]['age'],
                                                                           userlist[namelist.index(info)]['tel'],
                                                                           userlist[namelist.index(info)]['address']))
                        # 如果是数字ID，就直接抓出数据
                        elif int(info) < len(userlist) - 1:
                            print('{:2}  {:10}  {:4}  {:20}  {:20}'.format(int(info),
                                                                           userlist[int(info)]['name'],
                                                                           userlist[int(info)]['age'],
                                                                           userlist[int(info)]['tel'],
                                                                           userlist[int(info)]['address']))
                        else:
                            print('Input error,Not found')
                    except:
                        print('Input error or nothing found')

                elif op == 'EXIT':
                    # 将计数器等于4，退出总循环
                    count = 4
                    break
                else:
                    # 加上颜色 警告信息
                    print('\033[1;31m invalid cmd! \033[0m')
        else:
            print('Username or password is incorrect!')
            count += 1
            # 取当前时间
            cur_time = datetime.datetime.now().strftime('%F %T')
            if count == 3:
                print('Maximum number of attempts to login, Try next day')
            # 如果现在时间大于结束时间，就初始化结束时间和计数器
            elif cur_time > etime:
                count = 0
                etime = (datetime.datetime.now() + datetime.timedelta(minutes=1 * 60 * 24)).strftime('%F %T')
    except Exception as e:
        print('Username or password is incorrect!')
        count += 1
        cur_time = datetime.datetime.now().strftime('%F %T')
        if count == 3:
            print('Maximum number of attempts to login, Try next day')
        # 如果现在时间大于结束时间，就初始化结束时间和计数器
        elif cur_time > etime:
            count = 0
            etime = (datetime.datetime.now() + datetime.timedelta(minutes=1 * 60 * 24)).strftime('%F %T')

try:
    fd = open('user.db', 'w')
    membuf = json.dumps(userlist)
    fd.write(membuf)
    fd.close()
except Exception as e:
    print(e)

