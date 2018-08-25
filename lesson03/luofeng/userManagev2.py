#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/25 下午2:21
# @Author  : LuoFeng
# @Site    : 
# @File    : userManagev2.py
# @Software: PyCharm

import time
import json
import datetime as d
from datetime import datetime as t


# 存储用户信息
userList = []

# 定义用户名和密码，可登录次数，登录状态, 登录时间
loginPass = {'name': 'admin', 'pwd': 'reboot', 'count': 3, 'state': False, 'loginTime': None}

# 定义登录成功后提示信息
succ_msg = '''\033[32m
-------------------------------
欢迎登录用户系统，请选择对应的操作选项
-------------------------------
    1. 增加用户信息(add)
    2. 删除用户信息(delete)
    3. 更新用户信息(update)
    4. 查询用户信息(find)
    5. 退出用户管理系统(exit)
-------------------------------
\033[0m'''

# 获取用户名和密码
count = loginPass['count']
isState = False
while count > 0:
    try:
        username = input("please enter your username: ").strip()
        password = input("please enter your password: ").strip()
        currTime = time.strftime('%Y%m%d%H%M%S')
        exprTime = (t.now() + d.timedelta(days=1)).strftime('%Y%m%d%H%M%S')

        if loginPass['name'] == username and loginPass['pwd'] == password:
            loginPass['state'] = True
            loginPass['loginTime'] = currTime
            print(succ_msg)
            break

        else:
            count -= 1
            print("\033[31m登录失败，还剩余{}次机会，请重新输入!!!\033[0m".format(count))

    except Exception as e:
        print("输入有误，请重新输入",e)

# 登录成功，根据用户选择的进行增删改查
state = loginPass['state']
while state is True:
    userCards = {}
    op = input("select the option to operate: ").strip()
    if op == "add":
        userCard = input("please add user information: ").strip()
        uList = userCard.split(' ')
#        {'name': 'monkey1', 'age': 20, 'tel': '132xxx', 'address': 'beijing', 'id': '1'},
        try:
            if len(userList) == 0:
                uid = 1
                userCards['uid'] = uid
                userCards['name'] = uList[0]
                userCards['age'] = uList[1]
                userCards['tel'] = uList[2]
                userCards['address'] = uList[3]
                userList.append(userCards)

            else:
                uid = max([x['uid'] for x in userList]) + 1
                userCards['uid'] = uid
                userCards['name'] = uList[0]
                userCards['age'] = uList[1]
                userCards['tel'] = uList[2]
                userCards['address'] = uList[3]
                userList.append(userCards)

        except Exception as e:
            print(e)

    elif op == "delete":
        '''删除用户信息'''
        try:
            del_id = int(input("Please enter the uid to delete: ").strip())
            idList = [x['uid'] for x in userList]
            isState = 0
            if del_id in idList:
                delPos = del_id - 1
                del userList[delPos]
                isState = True
                print(userList)

            if isState is not True:
                print("\033[31m用户UID不存在，请重新选择后在删除!!!\033[0m")

        except Exception as e:
            print("please enter a integer num, such as figures 1, 5, 10.")

    elif op == "update":
        '''更新用户信息'''
        try:
            updateUser = input("Please enter the user name to update information: ").strip()
            for serial, data in enumerate(userList):
                if updateUser == data['name']:
                    isState = True
                    userCard = input("Please modify the user information: ").strip()
                    uList = userCard.split(' ')
                    userList[serial]['uid'] = data['uid']
                    userList[serial]['name'] = uList[0]
                    userList[serial]['age'] = uList[1]
                    userList[serial]['tel'] = uList[2]
                    userList[serial]['address'] = uList[3]
                    print(userList)

            if isState is not True:
                print("\033[33m用户{}不存在，无法删除!!!\033[0m".format(updateUser))

        except Exception as e:
            print(e)

    elif op == "list":
        '''查询用户信息'''
        try:
            queryName = input("please enter the user name to query: ")
            for data in userList:
                if queryName == data['name']:
                    isState = True
                    print("\033[32m-\033[0m" * 50)
                    print("uid\t\tname\t\tage\t\ttel\t\taddress")
                    print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(data['uid'], data['name'], data['age'], data['tel'], data['address']))
                    print("\033[32m-\033[0m" * 50)

            if isState is not True:
                print("\033[33m用户{}不存在，请重新选择后在查询!!!\033[0m".format(queryName))

        except Exception as e:
            print(e)

    elif op == "exit":
        '''退出用户管理系统'''
        dataFile = './usercards.txt'
        try:
            f = open(dataFile, 'w')
            json.dumps(userList)
            f.write(str(userList))

        except Exception as e:
            print('数据写入异常',e)

        finally:
            f.close()
            break

    else:
        print("\033[31m未知操作，请重新选择，输入add|delete|update|find|exit选项!!!\033[0m")
