#! /usr/bin/python
# -*- coding: utf-8 -*-
# @File  : UserManage.py
# @Author: ZhouGui
# @Date  : 2018/8/13

userInfo = []  # 用户列表
count = 0  # 登录次数
adminInfo = ('admin', 'admin123')  # 管理员登录用户
while count < 3:
    username = input("Please input your username:")
    password = input("Please input your password:")
    if username == adminInfo[0] and password == adminInfo[1]:
        print("\033[1;32m 欢迎使用员工系统！！\033[0m")
        while True:
            flag = False
            op = input("Please input your option [add|del|update|list|find|exit]:")
            if op == "add":
                bodyinfo = input("Please input userinfo:")
                userList = bodyinfo.split(' ')
                if len(userInfo) == 0:
                    userList.insert(0, 1)
                    userInfo.append(userList)
                    print("新增用户信息成功！！！")
                    print(userInfo)
                else:
                    uids = int(len(userInfo))
                    new_id = uids + 1
                    userList.insert(0, new_id)
                    userInfo.append(userList)
                    print(userInfo)
            elif op == "del":
                uid = input("input uid: ")
                for x in userInfo:
                    if x[0] == int(uid):
                        userInfo.remove(x)
                        print("删除用户信息成功！！！")
                print(userInfo)
            elif op == "update":
                uid = input("请输入用户uid: ")
                for x in userInfo:
                    isexist = [];
                    for x in userInfo:
                        if x[0] == int(uid):
                            isexist = x
                            break
                    if isexist == []:
                        print("您查找的用户不存在！！！")
                        break
                    else:
                        mod = input("Please choice your mod [name|age|tel|address]:")  # 需要修改的信息字段
                        if mod == "name":
                            message = input("Please input your message:")  # 输入的修改内容
                            x[1] = message
                            print(userInfo)
                            break
                        elif mod == "age":
                            message = input("Please input your message:")
                            x[2] = message
                            print(userInfo)
                            break
                        elif mod == "tel":
                            message = input("Please input your message:")
                            x[3] = message
                            print(userInfo)
                            break
                        elif mod == "address":
                            message = input("Please input your message:")
                            x[4] = message
                            print(userInfo)
                            break
                        else:
                            print("invalid option.")
            elif op == "list":
                print(userInfo)
            elif op == "find":
                uid = input("请输入用户uid: ")
                isexist = [];
                for x in userInfo:
                    if x[0] == int(uid):
                        isexist = x
                        break
                if isexist == []:
                    print("您查找的用户不存在！！！")
                else:
                    print(isexist)
            elif op == "exit":
                print("欢迎下次使用员工系统！！！")
                flag = True
                break
            else:
                print("invalid option.")
    else:
        print("\033[1;31m 请输入正确的用户名及密码！！！\033[0m")
    count += 1
else:
    print("\033[1;31m 很抱歉，今天三次机会用完了！！！\033[0m")
