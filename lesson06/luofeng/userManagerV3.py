#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 上午10:06
# @Author  : LuoFeng
# @Site    : 
# @File    : userManage_v2.py
# @Software: PyCharm

# 导入模块
import time
import json
import math
from utils import DB

# 定义常量
LOCK_FILE = "lock"
LOCK_DURATION = 30

MAX_LOGIN_COUNT = 3
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'reboot@123'

USER_FILE = 'user.json'
USER_INFO_NUM = 4

PAGE_SIZE = 2
TABLE_TPL = '|{uid:^5}|{name:^10}|{age:^5}|{tel:^15}|{address:^20}|'
TABLE_SPLIT_LINE = 61
TABLE_TITLE = {"uid": "uid", "name": "name", "age": "age", "tel": "tel", "address": "address"}

# 提示对用户数据进行增删改查
succ_msg = '''\033[32m
-------------------------------
欢迎登录用户系统，请选择对应的操作选项
-------------------------------
    1. 增加用户信息(add)
    2. 删除用户信息(delete)
    3. 更新用户信息(update)
    4. 查询用户信息(query)
    5. 保存用户信息(save)
    6. 退出用户管理系统(exit)
-------------------------------
\033[0m'''

# 每页展示的页数
PAGE_SIZE = 2

# 判断用户是否锁定
def is_unlock():
    lock_time = 0
    try:
        fhandler = open(LOCK_FILE, 'r')
        cxt = fhandler.read()
        fhandler.close()
        lock_time = float(cxt)
    except Exception as e:
        print(e)
        pass

    last_time = time.time() - lock_time > LOCK_DURATION
    return last_time

# 用户登录
def login():
    chk_flag = False

    for x in range(MAX_LOGIN_COUNT):
        username = input("请输入用户名:")
        password = input("请输入密码:")

        if ADMIN_USERNAME == username and ADMIN_PASSWORD == password:
            chk_flag = True
            break

        # 注意最后一次登录
        if MAX_LOGIN_COUNT - 1 == x:
            print("登陆失败, 锁定用户")
        else:
            print("登陆失败, 请重新输入用户名, 密码")

    return chk_flag

# 锁定用户
def lock_user():
    fhander = open(LOCK_FILE, 'w')
    fhander.write(str(time.time() + LOCK_DURATION))
    fhander.close()

# 登录成功，从文件获取用户数据
def get_users():
    users = []
    try:
        fhander = open(USER_FILE, 'r')
        cxt = fhander.read()
        users = json.loads(cxt)
        fhander.close()
    except Exception as e:
        print(e)
        pass

    return users

# 登录成功，打印用户信息
def print_users(users):
    print('-' * TABLE_SPLIT_LINE)
    print(TABLE_TPL.format(**TABLE_TITLE))
    print('-' * TABLE_SPLIT_LINE)
    for user in users:
        print(TABLE_TPL.format(**user))
    print('-' * TABLE_SPLIT_LINE)

# 增加用户信息
def add_user(users):
    text = input("请依次输入用户信息，用户名，年龄，电话号码，地址，以空格分隔: ")
    user = text.split()

    if len(user) != USER_INFO_NUM:
        print("\033[31m输入有误，请按格式要求输入!!!\033[0m")

    else:
        name, age, tel, address = user
        has_error = False
        if not age.isdigit():
            print("\033[31m年龄输入有误，请重新输入!!!\033[0m")
            has_error = True

        if not tel.isdigit():
            print("\033[31m电话号码输入有误，请重新输入!!!\033[0m")
            has_error = True

        if not has_error:
            # 生产用户id
            uid = max([x.get("uid") for x in users] + [0]) + 1
            print(uid)
            users.append({
                "uid": uid,
                "name": name,
                "age": int(age),
                "tel": tel,
                "address": address
            })
            print("\033[32m用户{}被成功添加\033[0m".format(name))

# 删除用户信息
def del_user(users):
    text = input("请输入用户UID: ").strip()
    has_error = False
    if text.isdigit() and len(text) != 0:
        uid = int(text)
        has_error = True

    if has_error:
        for user in users:
            if uid == user.get("uid"):
                users.remove(user)
                print("\033[32m用户{}删除成功\033[0m".format(user["name"]))
    else:
        print("\033[31m用户UID输入有误\033[0m")

# 查询用户信息
def query_user(users):
    users_query = []
    text = input("请输入查询的字符串: ")
    for user in users:
        if text == '' or user.get("name").find(text) != -1 or \
                user.get("tel").find(text) != -1 or \
                user.get("address").find(text) != -1:
            users_query.append(user)

    users_query_count = len(users_query)

    if users_query_count == 0:
        print("\033[31m无用户数据，查询失败!!!\033[0m")

    elif users_query_count <= PAGE_SIZE:
        print_users(users_query)

    else:
        max_page = math.ceil(users_query_count / PAGE_SIZE)
        while True:
            text_page_num = input("共有{0}页, 请输入查询页码(1 ~ {0}): ".format(max_page)).strip()
            if text_page_num.isdigit() and int(text_page_num) <= max_page:
                page_num = int(text_page_num)
                print_users(users_query[(page_num - 1) * PAGE_SIZE : page_num * PAGE_SIZE])

                if int(text_page_num) == max_page:
                    print("\033[32m用户信息查询完成\033[0m")
                    break
            else:
                print("\033[31m页码输入错误，页码范围1 ~ {}\033[0m".format(max_page))

# 更新用户信息
def update_user(users):
    text = input("请输入用户UID: ")
    is_exists = False
    uid = 0
    if text.isdigit():
        uid = int(text)
        for user in users:
            is_exists = True
            break

    if is_exists:
        text = input("请依次输入用户信息，格式用户名，年龄，手机号，地址，以空格分割: ")
        user = text.split()
        print(user)

        if len(user) != USER_INFO_NUM:
            print("\033[31m输入有误，请按格式要求输入!!!\033[0m")

        else:
            name, age, tel, address = user
            has_error = False
            if not age.isdigit():
                print("\033[31m年龄输入有误，请重新输入!!!\033[0m")
                has_error = True

            if not tel.isdigit():
                print("\033[31m电话号码输入有误，请重新输入!!!\033[0m")
                has_error = True

            if not has_error:
                for user in users:
                    if uid == user.get("uid"):
                        user['name'] = name
                        user['age'] = int(age)
                        user['tel'] = tel
                        user['address'] = address
                        print("\033[32m用户{}信息更新成功\033[0m".format(name))
                        break
    else:
        print("\033[31m用户UID输入有误033\0m")

# 保存用户信息
def save_user(users):
    fhandler = open(USER_FILE, 'w')
    fhandler.write(json.dumps(users))
    fhandler.close()
    print("\033[32m用户信息保存成功\033[0m")

# 登录成功后，对用户信息进行增删改查
def user_operate(users):
    print(succ_msg)
    while True:
        op = input("请输入操作: ")
        if op == "add":
            add_user(users)
            save_user(users)

        elif op == "delete":
            print_users(users)
            del_user(users)

        elif op == "update":
            print_users(users)
            update_user(users)

        elif op == "query":
            query_user(users)

        elif op == "save":
            save_user(users)

        elif op == "exit":
            save_user(users)
            break

        else:
            print("\033[31m输入有误，请重新输入!!!\033[0m")

def main():
    #判断用户是否被锁定
    if not is_unlock():
        print("用户被锁定，请稍后再试!!!")
        return

    if login():
        # 登录成功，从文件获取用户信息
        users = get_users()

        # 加载用户信息后，对用户信息进行增删改查操作
        user_operate(users)

    else:
        # 登录失败，锁定用户
        lock_user()

main()
