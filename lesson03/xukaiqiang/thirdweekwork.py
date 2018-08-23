#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 上午1:34
# @Author  : iteemo
# @File    : s7.py

import os
import json
import time


class Userdisplay(object):

    def __init__(self):
        # 判断登陆次数变量
        self.count = 0
        self.userinfonum = 0
        self.userauth = {
            "name": "admin",
            "password": "123456"
        }
        self.logref = False
        self.useaction = [
            ["1", "add", "ADD", "添加用户"],
            ["2", "del", "DEL", "删除用户"],
            ["3", "update", "UPDATE", "更新用户"],
            ["4", "list", "LIST", "查看用户"],
            ["5", "find", "FIND", "查找用户"],
            ["6", "quit", "exit", "QUIT", "EXIT", "退出系统"]
        ]
        self.usertableinfo = self.usertable()
        # 用户条数变量
        self.lenusernum = len(self.usertableinfo)
        # 最大uid变量
        if self.usertableinfo:
            self.maxuserkeynum = max(self.usertableinfo)
        else:
            self.maxuserkeynum = 0
        self.blusernamedict = self.blockUserinfo()
        self.nowtime = time.time()

    # 初始化用户表
    def usertable(self):
        userinfo_log = os.path.exists("userinfo.log")
        if userinfo_log:
            with open("userinfo.log", "r")as f:
                # for i in f:
                usertableinfo = json.loads(f.read().strip())
        else:
            usertableinfo = {}
            self.maxuserkeynum = 0
        return usertableinfo
        # except Exception as e:
        usertableinfo = {}
        # print("usertab", e)

    # return usertableinfo

    # 锁定用户,写入锁定文件
    def blockUser(self, username, locktime):
        blockuserdict = {
            username: locktime
        }
        blockuser = json.dumps(blockuserdict)
        with open("block_user.log", "a+") as f:
            f.write(blockuser)

    # 讲锁定用户反序列化为一个字典
    def blockUserinfo(self):
        try:
            with open("block_user.log", "r")as f:
                blusernamedict = json.loads(f.read())
        except Exception as e:
            blusernamedict = {}
        return blusernamedict

    def deleteuser(self, deluid):
        deluid = int(deluid)
        print(self.usertableinfo)
        if deluid in self.usertableinfo:
            self.usertableinfo.pop(deluid)
            print("\033[31muid为: %s 的用户已经删除\033[0m" % (deluid))
        else:
            print("\033[31muid:%s 不存在\033[0m" % (deluid))

    def useradd(self, userid, userinfo):
        pass

    def listuser(self):
        print("\033[31m*\033[0m" * 50)
        print("uid\t""name\t"    "age\t"     "tel\t"     "address")
        print("\033[31m*\033[0m" * 50)
        for k, v in self.usertableinfo.items():
            uid = k
            name = v["name"]
            age = v["age"]
            tel = v["tel"]
            address = v["address"]
            print("{0}\t{1}\t{2}\t{3}\t{4}".format(uid, name, age, tel, address))
        print("\033[31m*\033[0m" * 50)

    def finduser(self, finduserinfo):
        for k, v in self.usertableinfo.items():
            for m, n in v.items():
                if finduserinfo == n:
                    print(v)

    def updateuser(self, upuid):
        if upuid in self.usertableinfo:
            updateuserinfo = input("请输入要更新的用户信息")
            updateuserinfolist = updateuserinfo.split()
            self.usertableinfo[upuid] = {"name": updateuserinfolist[0], "age": updateuserinfolist[1],
                                         "tel": updateuserinfolist[2], "address": updateuserinfolist[3]}

        else:
            print("\033[31m你输入的uid你不存在\033[0m")

    def helpuser(self):
        print(self.useaction)

    def userauthinfo(self):
        while self.count < 3:
            if self.logref:
                break
            username = input("\033[32mPlease your name:\033[0m").strip()
            password = input("\033[32mPlease input your password:\033[0m").strip()

            if username in self.blusernamedict:
                judgetime = int(self.nowtime - self.blusernamedict[username])
                if judgetime > 120:
                    with open("block_user.log", "w")as f:
                        f.truncate()
                        f.closed
                else:
                    print("\033[31m%s被禁止登陆,目前禁止时间为:%sS\033[0m" % (username, judgetime))
                    self.logref = True
                    break
                break
            if username == self.userauth["name"] and password == self.userauth["password"]:
                print("欢迎你")
                print(
                    """\033[32m请输入你的操作(可以输入字母或者数字):\n1.add or ADD or 添加用户\n2.del or DEL or 删除用户\n3.update or UPDATE or 更新用户\n4.list or LIST  or 查看用户\n5.find or FIND or 查找用户\n6.quit or exit or 退出系统\n7.help or h or 帮助信息\033[0m""")
                while True:
                    # action = input("\033[32m请输入操作指令(按h即可显示帮助信息):\033[0m")
                    action = input("请输入操作指令(按h即可显示帮助信息):")
                    if action in self.useaction[0]:
                        adduser = input("\033[32m请输入用户:姓名 年龄 电话 地址:\033[0m")
                        adduserlist = adduser.split()
                        if len(adduserlist) != 4:
                            print("\033[31m不符合输入规则,请重新输入\033[0m")
                            continue
                        else:
                            name = adduserlist[0]
                            age = adduserlist[1]
                            tel = adduserlist[2]
                            address = adduserlist[3]

                            # try:

                            lennum = len(self.usertableinfo)
                        if lennum:
                            tmpuid = 0
                            for k,v in self.usertableinfo.items():
                                k = int(k)
                                if k > tmpuid:
                                    tmpuid = k

                            # uid = max(int(self.usertableinfo.keys()))
                            # uid = int(uid)
                            uid = tmpuid
                            maxuid = uid + 1
                            self.usertableinfo[maxuid] = {"name": name, "age": age, "tel": tel, "address": address}
                            print(self.usertableinfo)
                            print(self.lenusernum)
                            continue
                        else:
                            uid = 0
                            self.usertableinfo[uid] = {"name": name, "age": age, "tel": tel, "address": address}
                            # except Exception as e:
                            # maxuid = self.maxuserkeynum
                            # self.usertableinfo[maxuid] = {"name": name, "age": age, "tel": tel, "address": address}
                            # print(self.usertableinfo, "i am else111111")
                            # lennum = len(self.usertableinfo)
                            # print(lennum, "iam lennum")
                        # print("e", e)
                        #     continue
                    elif action in self.useaction[1]:
                        deluid = input("\033[31m请输入要删除用户的UID:\033[0m")
                        self.deleteuser(deluid)

                    elif action in self.useaction[2]:
                        upuid = input("\033[32m请输入要更新用户的uid:\033[0m")
                        self.updateuser(upuid)
                    elif action in self.useaction[3]:
                        self.listuser()
                    elif action in self.useaction[4]:
                        finduserinfo = input("\033[32m请输出你要查找的信息,如姓名,年龄,电话,地址等\n\033[0m:")
                        self.finduser(finduserinfo)
                    elif action in self.useaction[5]:
                        userinfo = self.usertableinfo
                        with open("userinfo.log", "w")as f:
                            userinfo = json.dumps(userinfo)
                            f.write(userinfo)
                            f.closed
                        self.logref = True
                        break

                    else:
                        self.helpuser()

            else:
                print("\033[31m用户名密码输入错误,请重新输入\033[0m")
                self.count += 1
                if self.count == 3:
                    locktime = time.time()
                    self.blockUser(username, locktime)


if __name__ == '__main__':
    demouserlogin = Userdisplay()
    demouserlogin.userauthinfo()
