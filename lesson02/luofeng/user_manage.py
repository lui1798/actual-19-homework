#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 下午10:53
# @Author  : LuoFeng
# @Site    :
# @File    : user_manage.py
# @Software: PyCharm

# 存储用户信息
userlist = []

# 定义循环次数和认证用户名和密码
count = 3
userinfo = ('admin', 'reboot')

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
username = input("please enter your username: ")
password = input("please enter your password: ")

# 用户登录
while count >= 0:
    # 判断登录用户和密码
    if username == userinfo[0] and password == userinfo[1]:
        print(succ_msg)
        op = input("select the option to operate: ")
        if op == "add":
            '''增加用户信息'''
            userCard = input("please add user information: ")
            uList = userCard.split(' ')
            if len(uList) != 4:
                print("\033[31m输入错误，请重新输入，格式:ID Name Age Address\033[0m")

            else:
                if len(userlist) == 0:
                    uid = 1
                    uList.insert(0, uid)
                    userlist.append(uList)
                else:
                    uid = (max([x[0] for x in userlist])+1)
                    uList.insert(0, uid)
                    userlist.append(uList)
                    print(userlist)

        elif op == "delete":
            '''删除用户信息'''
            del_id = input("Please enter the uid to delete: ")
            for data in userlist:
                chk_flag = 0
                if del_id in str(data[0]):
                    userlist.remove(data)
                    chk_flag = 1
                    print("\033[32m用户已从系统删除\033[0m")

            if chk_flag == 0:
                print("\033[31m用户UID不存在，请重新选择后在删除!!!")

        elif op == "update":
            '''更新用户信息'''
            update_user = input("Please enter the user name to update information: ")
            for serial, data in enumerate(userlist):
                if update_user in data[1]:
                    chk_flag = 0
                    new_data = input("Please modify the user information: ")
                    uList = new_data.split(' ')
                    uid = data[0]
                    uList.insert(0, uid)
                    del userlist[serial]
                    userlist.insert(serial, uList)
                    chk_flag = 1

            if chk_flag == 0:
                print("\033[31m用户不存在，请重新选择后在更新!!!")

        elif op == "find":
            '''查询用户信息'''
            chk_flag = 0
            query_name = input("please enter the user name to query: ")
            for account_name in userlist:
                if query_name in account_name:
                    chk_flag = 1
                    print("\033[32m-\033[0m"*50)
                    print("ID\t\tName\t\tSex\t\t\tAge\t\tAddress")
                    print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(account_name[0],account_name[1],account_name[2],account_name[3],account_name[4]))
                    print("\033[32m-\033[0m"*50)

            if chk_flag == 0:
                print("用户{}不存在，请重新选择后在查询!!!".format(query_name))

        elif op == "exit":
            '''退出用户系统'''
            break

        else:
            print("\033[31m未知操作，请重新选择，输入add|delete|update|find|exit选项!!!\033[0m")
    else:
        count-=1
        if count == 0:
            print("\033[31m用户登录失败，请15分钟后在尝试登录!!!\033[0m".format(count))
            break
        else:
            print("\033[31m登录失败，用户名或密码错误，还剩余{}次机会，请重新输入!!!\033[0m".format(count))
            username = input("please enter your username: ")
            password = input("please enter your password: ")
