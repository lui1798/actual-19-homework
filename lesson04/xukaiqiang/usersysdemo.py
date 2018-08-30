#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 下午3:33
# @Author  : iteemo
# @File    : userdemo2.py
import getpass
import time
import json
import math

class usersystem():
    def __init__(self):
        # 锁定文件,锁定时间,用户文件
        self.LOCK_FILE = "lock"
        self.LOCK_DURATION = 30
        self.USER_FILE = "user.json"
        # 用户名密码
        self.ADMIN_USERNAME = "admin"
        self.ADMIN_PASSWORD = "123456"

        # 用户登陆次数
        self.MAX_LOGIN_TIMES = 3
        # 用户输入字段
        self.USER_INFO_NUM = 4
        # 打印变量
        self.TABLE_TPL = '{id:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
        self.TABLE_SPLIT_LINE = 64
        self.TABLE_TITLE = {"id": "id", "name": "name", "age": "age", "tel": "tel", "address": "address"}
        # 每页的数量
        self.PAGE_SIZE = 2

    def checklock(self):
        # 设定锁定时间变量,如果锁定文件不存在则锁定时间为0,checklock返回true,就是为锁定
        lock_time = 0
        try:
            fhandler = open(self.LOCK_FILE, "r")
            cxt = fhandler.read()
            fhandler.close()
            lock_time = float(cxt)
        except Exception as e:
            # print(e)
            pass
        return time.time() - lock_time > self.LOCK_DURATION

    # 定义登陆方法
    def islogin(self):
        # 定义登陆状态
        is_login = False
        for i in range(self.MAX_LOGIN_TIMES):
            username = input("请输入用户名:")
            password = getpass.getpass("请输入密码:")

            if self.ADMIN_USERNAME == username and self.ADMIN_PASSWORD == password:
                is_login = True
                break

            # 注意最会一次登陆
            if self.MAX_LOGIN_TIMES - 1 == i:
                print("登陆失败, 锁定用户")
            else:
                print("登陆失败, 请重新输入用户名, 密码")
        return is_login

    def get_users(self):
        users = []
        try:
            fhandler = open(self.USER_FILE, "r")
            cxt = fhandler.read()
            fhandler.close()
            users = json.loads(cxt)
        except Exception as e:
            pass
        return users

    # 定义添加用户的方法
    def adduser(self,users):
        text = input("请依次输入用户信息(用户名, 年龄, 电话号码, 地址), 信息使用空格分割:")
        user = text.split()
        if len(user) != self.USER_INFO_NUM:
            print("输入数据不正确")
        else:
            # name, age, tel, address = user[0], user[1], user[2], user[3]
            name, age, tel, address = user
            has_error = False
            if not age.isdigit():
                print("年龄输入有问题")
                has_error = True

            if not tel.isdigit():
                print("电话号码有问题")
                has_error = True

            if not has_error:
                # 生成id
                uid = max([x.get("id") for x in users] + [0]) + 1
                users.append({
                    "id": uid,
                    "name": name,
                    "age": int(age),
                    "tel": tel,
                    "address": address
                })
                print("添加用户成功")
                print(users)
            return users

    # 定义删除用户方法
    def deluser(self,users):
        text = input("请输入删除用户的ID:")
        if text.isdigit():
            uid = int(text)
            for user in users:
                if uid == user.get("id"):
                    users.remove(user)
                    print("删除用户成功")
                    break
            else:
                print("输入ID错误")
        else:
            print("输入ID错误")
        return users

    # 定义修改用户方法
    def modifyuser(self,users):
        text = input("请输入修改用户ID:")
        is_exists = False
        uid = 0
        if text.isdigit():
            uid = int(text)
            for user in users:
                if uid == user.get("id"):
                    print("更新用户信息:" + json.dumps(user))
                    is_exists = True
                    break

        if is_exists:
            text = input("请依次输入用户信息(用户名, 年龄, 电话号码, 地址), 信息使用空格分割:")
            user = text.split()
            if len(user) != self.USER_INFO_NUM:
                print("输入数据不正确")
            else:
                name, age, tel, address = user
                has_error = False
                if not age.isdigit():
                    has_error = True
                    print("输入的年龄不正确")

                if not tel.isdigit():
                    has_error = True
                    print("输入的电话不正确")

                if not has_error:
                    for user in users:
                        if uid == user.get("id"):
                            user.update({
                                "name": name,
                                "age": int(age),
                                "tel": tel,
                                "address": address
                            })
                            print("更新成功")
                            break
        else:
            print("输出ID错误")

        return users

    # 打印用户方法
    def print_users(self,users):
        print('-' * self.TABLE_SPLIT_LINE)
        print(self.TABLE_TPL.format(
            **self.TABLE_TITLE))  # TABLE_TPL.format(id="id", name="name", age="age", tel="tel", address="address")
        print('-' * self.TABLE_SPLIT_LINE)
        for user in users:
            print(self.TABLE_TPL.format(**user))
        print('-' * self.TABLE_SPLIT_LINE)

    # 定义查询用户方法
    def listuser(self,users):
        text = input("请输入查询的字符串:")
        # 查询结果输出
        users_find = []
        for user in users:
            if text == '' or user.get("name").find(text) != -1 or \
                    user.get("tel").find(text) != -1 or \
                    user.get("address").find(text) != -1:
                users_find.append(user)
        # 查询结果数量
        users_find_count = len(users_find)
        if users_find_count == 0:
            print("无数据")
        elif users_find_count <= self.PAGE_SIZE:
            self.print_users(users_find)
        else:
            # 查询结果向上取整
            max_page = math.ceil(users_find_count / self.PAGE_SIZE)

            while True:
                text_page_num = input("共有{0}页, 请输入查询页码(1 ~ {0}): ".format(max_page))
                if text_page_num.isdigit() and int(text_page_num) <= max_page:
                    page_num = int(text_page_num)
                    print(self.TABLE_TPL.format(
                        **self.TABLE_TITLE))  # TABLE_TPL.format(id="id", name="name", age="age", tel="tel", address="address")
                    print('-' * self.TABLE_SPLIT_LINE)
                    for user in users_find[(page_num - 1) * self.PAGE_SIZE: page_num * self.PAGE_SIZE]:
                        print(self.TABLE_TPL.format(**user))
                else:
                    print("输入页码错误")
                    break
        return users

    # 保存用户方法:
    def backuser(self,users):
        fhandler = open(self.USER_FILE, "w")
        fhandler.write(json.dumps(users))
        fhandler.close()
        print("存储用户信息成功")

    # 定义用户锁定方法
    def lock_user(self):
        fhandler = open(self.LOCK_FILE, "w")
        fhandler.write(str(time.time()))
        fhandler.close()

    def operate(self,users):
        while True:
            op = input("请输入操作(add,modify,delete,query,save,exit):")
            if op == "add":
                users = self.adduser(users)
            elif op == "modify":
                users = self.modifyuser(users)
            elif op == "delete":
                users = self.deluser(users)
            elif op == "query":
                self.listuser(users)
            elif op == "save":
                self.backuser(users)
            elif op == "exit":
                self.backuser(users)
                break
            else:
                print("输入参数错误")
    def main(self):
        # if __name__ == '__main__':
        # 1. 判断是否锁定
        if not self.checklock():
            print("用户被锁定, 请稍后再试")
            return

        # 2. 登陆
        if self.islogin():
            # 3. 登陆成功
            # 3.1 加载用户数据
            users = self.get_users()
            # 3.2 操作
            self.operate(users)
        else:
            # 4. 登陆失败, 锁定用户
            self.lock_user()


iteemo = usersystem()
iteemo.main()