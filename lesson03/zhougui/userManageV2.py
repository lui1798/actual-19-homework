#! /usr/bin/python
# -*- coding: utf-8 -*-
# @File  : userMange2.py
# @Author: ZhouGui
# @Date  : 2018/8/20
import datetime
import time
import json

try:
    fd2 = open('./time.txt')
    beforeTime = json.load(fd2)  # 读取错误输入密码时间
    fd2.close()
except FileNotFoundError:
    beforeTime = "1971-01-01 00:00:00"

nowTime = datetime.datetime.now().strftime('%F %T')  # 获取当前时间

startTime = time.mktime(time.strptime("{}".format(beforeTime), '%Y-%m-%d %H:%M:%S'))
endTime = time.mktime(time.strptime("{}".format(nowTime), '%Y-%m-%d %H:%M:%S'))
workTime = int((endTime - startTime) / (60 * 60))  # 获取间隔时长
if workTime > 24:
    count = 0  # 登录次数
    userInfo = []  # 用户列表
    adminInfo = ('admin', 'admin123')  # 管理员登录用户
    while count < 3:
        username = input("Please input your username:")
        password = input("Please input your password:")
        if username.strip() == adminInfo[0] and password.strip() == adminInfo[1]:
            print("\033[1;32m 欢迎使用员工系统\033[0m")
            while True:
                flag = False
                tmp_user = {}
                op = input("Please input your option [add|del|update|list|find|exit]:")
                if op == "add":
                    tmp_user['name'] = input("Please input your name:")
                    tmp_user['age'] = input("Please input  your age:")
                    tmp_user['tel'] = input("Please input your tel:")
                    tmp_user['address'] = input("Please input your address:")
                    if len(userInfo) == 0:
                        tmp_user['id'] = 1
                        userInfo.append(tmp_user)
                    else:
                        uids = [int(x['id']) for x in userInfo]
                        new_id = max(uids) + 1
                        tmp_user['id'] = new_id
                        userInfo.append(tmp_user)
                    print("\033[32m用户添加成功\033[0m")
                elif op == "del":
                    uid = int(input("请输入删除用户的ID："))
                    if uid in [x['id'] for x in userInfo]:
                        for x in userInfo:
                            if x['id'] == uid:
                                userInfo.remove(x)
                    else:
                        print("\033[31m 用户ID不存在\033[0m")
                elif op == "update":
                    uid = int(input("请输入用户ID："))
                    if uid in [x['id'] for x in userInfo]:
                        for x in userInfo:
                            if x['id'] == uid:
                                mod = input("Please choice your mod [name|age|tel|address]:")  # 需要修改的信息字段
                                modmessage = x
                                if mod == "name":
                                    message = input("Please input your message:")  # 输入的修改内容
                                    modmessage['name'] = message
                                    break
                                elif mod == "age":
                                    message = input("Please input your message:")
                                    if message.isdigit() == False:
                                        print("请输入整数")
                                    modmessage['age'] = message
                                    break
                                elif mod == "tel":
                                    message = input("Please input your message:")
                                    if message.isdigit() == False:
                                        print("请输入整数")
                                    modmessage['tel'] = message
                                    break
                                elif mod == "address":
                                    message = input("Please input your message:")
                                    modmessage['address'] = message
                                    break
                                else:
                                    print("invalid option.")
                    else:
                        print("\033[31m 用户ID不存在\033[0m")
                elif op == "list":
                    if len(userInfo) == 0:
                        try:
                            userFile = open('./user.txt')
                            userFileJson = userFile.read()
                            userInfo = json.loads(userFileJson)  # 读取上次保存的用户信息
                            userFile.close()
                        except FileNotFoundError:
                            print("No such file or directory")
                    for i in ['name', 'age', 'tel', 'address', 'UserID']:
                        print("{:<15}".format(i), end=' ')
                    print('')
                    for x in userInfo:
                        for k, v in x.items():
                            print("{:<15}".format(v), end=' ')
                        print('')
                elif op == "find":
                    uid = int(input("请输入用户ID: "))
                    if uid in [x['id'] for x in userInfo]:
                        for x in userInfo:
                            if x['id'] == uid:
                                for i in ['name', 'age', 'tel', 'address', 'UserID']:
                                    print("{:<15}".format(i), end=' ')
                                print('')
                                for k, v in x.items():
                                    print("{:<15}".format(v), end=' ')
                                print('')
                    else:
                        print("\033[31m 用户ID不存在\033[0m")
                elif op == "exit":
                    print("欢迎下次使用员工系统")
                    userFile = open('./user.txt', 'w')
                    userFileJson = json.dumps(userInfo)
                    userFile.write(userFileJson)  # 保存用户信息
                    userFile.close()
                    flag = True
                    count = 0
                    break
                else:
                    print("invalid option")
        count += 1
    else:
        errorTime = datetime.datetime.now().strftime('%F %T')
        errorTimeJson = json.dumps(errorTime)
        fd = open('./time.txt', 'w')
        fd.write(errorTimeJson)  # 保存三次错误输入密码时间
        fd.close()
        print("\033[1;31m 对不起，您已连续三次错误输入密码，请24小时后使用\033[0m")
else:
    print("\033[1;31m 对不起，您已连续三次错误输入密码，请24小时后使用\033[0m")
