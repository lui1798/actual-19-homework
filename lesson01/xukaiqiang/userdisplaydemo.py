#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 上午12:22
# @Author  : iteemo
# @File    : c10.py

import os
import json
import time

userauth = ("admin", "123456")
count = 0  # 计数器
userinfo_log = os.path.exists("./userinfo.log")  # 用户表文件
userinfo = []
if userinfo_log:  # 加载用户信息
    if os.path.getsize('./userinfo.log'):
        with open("userinfo.log", "r")as f:
            userinfo = json.loads(f.read())
    else:
        userinfo = []
nowtime = time.time()
while count < 3:
    username = input("Please your name:")
    passwd = input("Please input your password:")
    block_file = os.path.exists("./block_user.log")  # 用户锁文件
    if block_file:
        with open('block_user.log', 'r')as f:
            blockuser = f.read()  # 读取锁定用户
        if username in blockuser:
            nowtime = time.time()
            with open("time.log", "r")as f:
                locktime = f.read()
                locktime = float(locktime)
            if nowtime - locktime < 120:
                blocktime = nowtime - locktime
                print("用户被锁定,且锁定时间未到,剩余时间为%ss" % (int(blocktime)))
                exit()
            else:
                with open("userinfo.log", "w")as f:
                    f.truncate()
                    f.closed
        # while True:
    if username == userauth[0] and passwd == userauth[1]:
        print("\033[32m 欢迎登陆用户系统 \033[0m")
        print("""\033[32m
                请输入你的操作(可以输入字母或者数字):
                1.add or ADD or 添加用户
                2.del or DEL or 删除用户
                3.update or UPDATE or 更新用户
                4.list or LIST  or 查看用户
                5.find or FIND or 查找用户
                6.quit or exit or 退出系统
                7.help or h or 帮助信息\033[0m
                """)
        actionjudge = [
            ["1", "add", "ADD", "添加用户"],
            ["2", "del", "DEL", "删除用户"],
            [3, "update", "UPDATE", "更新用户"],
            [4, "list", "LIST", "查看用户"],
            [5, "find", "FIND", "查找用户"],
            [6, "quit", "exit", "QUIT", "EXIT", "退出系统"],
            [7, "help", "h", "HELP", "H", "帮助信息"]
        ]
        while True:
            action = input("请输入操作指令(按h即可显示帮助信息):")
            # 添加用户操作
            if action in actionjudge[0]:
                print("""\033[32m请输入你需要添加的用户信息请用,后者空格进行隔开(
                    例如:
                    iteemo,29,13813813813,beijing
                    iteemo 29 13813813813 beijing
                    )\n :\033[0m""")
                adduser = input("请按照上面的提示输入你要添加的用户信息:")
                if "," in adduser:
                    adduserlist = adduser.split(",")
                    print(len(adduserlist))
                    print(adduserlist)
                    if len(adduserlist) != 4:
                        print("不符合输入规则,请重新输入1")
                        continue
                else:
                    adduserlist = adduser.split()
                    if len(adduserlist) != 4:
                        print("不符合输入规则,请重新输入2")
                        continue
                # 将信息插入userinfo用户表
                if len(userinfo) > 0:
                    # 自增uid
                    maxuid = max(userinfo)
                    maxuid = int(maxuid[0]) + 1

                    adduserlist.insert(0, maxuid)
                    userinfo.append(adduserlist)
                    print(adduserlist)
                    print(userinfo)
                    print("用户添加完成,新添加的用户为%s" % (adduserlist))
                    continue
                else:
                    maxuid = 0
                    adduserlist.insert(0, maxuid)
                    userinfo.append(adduserlist)
                    print("用户添加完成,新添加的用户为%s" % (adduserlist))
                    continue
            # 删除用户操作
            elif action in actionjudge[1]:
                deluid = int(input("请输入要删除用户的UID:"))
                delbool = False
                #判断用户时候存在于用户表中
                for x in userinfo:
                    if deluid in x:
                        # deluidindex = userinfo.index(x)
                        # print(deluidindex)
                        # userinfo.pop(deluidindex)
                        userinfo.remove(x)
                        print("您删除的用户为%s" % (x))
                        delbool = True
                if not delbool:
                    print("您删除的用户UID:%s不存在" % (deluid))
                continue
            # 更新用户信息
            elif action in actionjudge[2]:

                updateuserinfo = input("""请输入要更新用户的信息
                    例如:iteemo,29,13813813813,beijing
                    """)
                if "," in updateuserinfo:
                    updateuserlist = updateuserinfo.split(",")

                else:
                    updateuserlist = updateuserinfo.split()
                # 将信息插入userinfo用户表
                if len(userinfo) > 0:
                    # 自增uid
                    upmaxuid = max(userinfo)
                    upmaxuid = int(upmaxuid[0]) + 1

                    updateuserlist.insert(0, upmaxuid)
                    userinfo.append(updateuserlist)
                    print(updateuserlist)
                    print("用户添加完成,新添加的用户为%s" % (updateuserlist))
                    continue
                else:
                    upmaxuid = 0
                    updateuserlist.insert(0, upmaxuid)
                    userinfo.append(updateuserlist)
                    print("用户添加完成,新添加的用户为%s" % (updateuserlist))
                    continue
            # 查看用户信息
            elif action in actionjudge[3]:
                print("-" * 50)
                print("uid\t""name\t"    "age\t"     "tel\t"     "address")
                print("-" * 50)
                # 循环输出用户信息表
                for i in userinfo:
                    uid = i[0]
                    name = i[1]
                    age = i[2]
                    tel = i[3]
                    address = i[4]
                    print("{0}\t{1}\t{2}\t{3}\t{4}".format(uid, name, age, tel, address))
                print("-" * 50)
            # 查找用户信息
            elif action in actionjudge[4]:
                finduserinfo = input("请输出你要查找的信息,如姓名,年龄,电话,地址等\n:")
                for i in userinfo:
                    if finduserinfo in i:
                        print(i)
            # 退出系统
            elif action in actionjudge[5]:
                # 退出之前写入文件
                with open("userinfo.log", "w")as f:
                    userinfo = json.dumps(userinfo)
                    f.write(userinfo)
                    f.closed
                exit()
            # 帮助信息 
            elif action in actionjudge[6]:
                print("""请输入你的操作(可以输入字母或者数字):
                        1.add or ADD or 添加用户
                        2.del or DEL or 删除用户
                        3.update or UPDATE or 更新用户
                        4.list or LIST  or 查看用户
                        5.find or FIND or 查找用户
                        6.quit or exit or 退出系统
                        7.help or h or 帮助信息
                        """)
            else:
                print("输入错误,请按H获取帮助信息")
                continue
    else:
        print("用户名或者密码输入错误请重新输入")
        count += 1
        if count == 3:
            locktime = time.time()
            locktime = json.dumps(locktime)
            with open('block_user.log', 'w')as f, open('time.log', 'w')as f1:
                f.write(username)
                f1.write(locktime)
                f.closed
                f1.closed
