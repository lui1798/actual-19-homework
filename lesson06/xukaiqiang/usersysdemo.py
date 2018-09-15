#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 下午3:33
# @Author  : iteemo
# @File    : userdemo2.py
import getpass
import time
import json
import math
import xlwt
from dbtool import mysqlutils
from githublogin import Githublogin

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
        with open("db_config.json", "r") as file:
            self.db_param = json.load(file)
        self.db = mysqlutils(**self.db_param)
        self.filename = "user.csv"
        self.mygit = Githublogin()
        # self.gitstat = self.mygit.isLogin()

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
        # if self.gitstat:
        #     print("登陆github成功")
        #     is_login =True
        # return is_login

        for i in range(self.MAX_LOGIN_TIMES):
            mail = input("请输入github登陆邮箱:")
            password = getpass.getpass("请输入密码:")

            gitstat = self.mygit.isLogin(mail,password)
            # print(gitstat)
            # if self.ADMIN_USERNAME == mail and self.ADMIN_PASSWORD == password:
            if gitstat:
                is_login = True
                print("登陆Github成功,请在用户系统进行操作!")
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
            users = self.db.queryall("select * from myuser")
        except Exception as e:
            print(e)
        return users

    # 定义添加用户的方法
    def adduser(self,users):
        text = input("请依次输入用户信息(用户名, 年龄, 电话号码, 地址), 信息使用空格分割:")
        user = text.split()
        if len(user) != self.USER_INFO_NUM:
            print("输入数据不正确")
        else:
            # name, age, tel, address = user[0], user[1], user[2], user[3]
            sql_str = "insert into myuser(name , age, tel, address) values (%s, %s, %s,%s)"
            has_error = False
            if not user[1].isdigit():
                print("年龄输入有问题")
                has_error = True

            if not user[2].isdigit():
                print("电话号码有问题")
                has_error = True

            if not has_error:
                print("插入数据:", self.db.insertone(sql_str, user))
                users = self.db.queryone("select * from myuser where name = %s", (user[0]))
                print("添加用户成功")
                print(users)
            return users

    # 定义删除用户方法
    def deluser(self,users):
        text = input("请输入删除用户的ID:")
        if text.isdigit():
            uid = int(text)
            delref = self.db.execute("delete from myuser where id = %s", uid)
            if delref:
                print("删除用户成功")
            else:
                print("输入ID错误")
        else:
            print("输入ID错误")
        return users

    # 定义修改用户方法
    def modifyuser(self,users):
        text = input("请输入修改用户ID:")
        is_exists = False

        uid = self.db.queryone("select id from myuser where id = %s", text)
        if uid:
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
                    print(user,uid)
                    print(self.db.execute("update myuser set name = %s, age = %s, tel = %s, address = %s where id = %s;", (user[0], user[1], user[2], user[3], uid)))

                    users = self.db.queryone("select * from myuser where name = %s", (user[0]))
                    print("更新成功")
                    print(users)
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
        text = input("请输入查询用户姓名:")
        text = text.strip()
        # 查询结果输出
        users_find = []
        users = self.db.queryone("select * from myuser where name = %s", (text))
        if users:
            # for user in users:
            #     if text in user.get("name"):
            #         users_find.append(user)
            print(users)
        else:
            print("用户不存在")


    # 保存用户方法:
    def backuser(self,filename,users):
        workbook = xlwt.Workbook(encoding='utf-8')
        booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

        for i in range(len(users)):
            j = 0
            for k in users[i]:
                booksheet.write(i + 1, j, users[i][k])
                j += 1
        workbook.save(self.filename)




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
                self.backuser(self.filename,users)
            elif op == "exit":
                self.backuser(self.filename, users)
                break
            else:
                print("输入参数错误")
    def main(self):
        # if __name__ == '__main__':
        # 1. 判断是否锁定
        dbntable = self.db.queryone("select count(*) from testuser")
        if dbntable == None:
            sql = '''
                        CREATE TABLE `testusers1` (
                      `id` int(11) NOT NULL AUTO_INCREMENT,
                      `name` varchar(50) DEFAULT NULL,
                      `age` int(11) DEFAULT NULL,
                      `tel` varchar(11) DEFAULT NULL,
                      `address` varchar(80) DEFAULT NULL,
                      PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
                    '''
            self.db.execute(sql)
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