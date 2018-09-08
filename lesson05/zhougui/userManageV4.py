#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : userManageV3.py
# @Author: ZhouGui
# @Date  : 2018/8/28
import logging
import math
import json
import time

# 定义常量
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

USER_FILE = "user.json"
LOCK_FILE = "time.json"
LOCK_DURATION = 3
USER_INFO_NUM = 4

TABLE_TPL = '{id:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
TABLE_SPLIT_LINE = 64
TABLE_TITLE = {"id": "id", "name": "name", "age": "age", "tel": "tel", "address": "address"}
PAGE_SIZE = 5

# 定义日志
logger = logging.getLogger()
fh = logging.FileHandler('./usermange.log', encoding='utf-8')
fm = logging.Formatter('[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
fh.setFormatter(fm)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


def is_unlock():
    beforeTime = 0
    try:
        fhandler = open(LOCK_FILE)
        cxt = fhandler.read()
        fhandler.close()
        beforeTime = float(cxt)
    except Exception as  e:
        pass
    return time.time() - beforeTime > LOCK_DURATION


def login():
    is_login = False
    LOGIN_COUNT = 0  # 登录次数
    while LOGIN_COUNT < 3:
        username = input("Please input your username:")
        password = input("Please input your password:")
        if username.strip() == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            logging.debug('用户{}登录成功'.format(username))
            is_login = True
            break
        else:
            print("\033[1;31m 登陆失败, 请重新输入用户名, 密码\033[0m")
            logging.warning('用户{}登录失败'.format(username))
        LOGIN_COUNT += 1
    else:
        print("\033[1;31m 登陆失败, 锁定用户\033[0m")
        logging.warning('用户{}登录失败，已经被锁定'.format(username))

    return is_login


def get_users():
    users = []
    try:
        fhandler = open(USER_FILE)
        cxt = fhandler.read()
        fhandler.close()
        users = json.loads(cxt)
    except Exception as e:
        pass
    return users


def add_user(users):
    text = input("请依次输入用户名，年龄，电话号码，地址, 信息使用空格分割:")
    user = text.split()
    if len(user) != USER_INFO_NUM:
        print("\033[1;31m 输入的用户信息有误\033[0m")
        logging.warning('用户信息输入有误')
    else:
        name, age, tel, address = user
        has_Error = False
        if not age.isdigit():
            print("\033[1;31m 年龄输入有误\033[0m")
            logging.warning('年龄输入有误')
            has_Error = True
        if not tel.isdigit():
            print("\033[1;31m 电话号码输入有误\033[0m")
            logging.warning('电话号码输入有误')
            has_Error = True
        if not has_Error:
            uid = max([x.get("id") for x in users] + [0]) + 1
            users.append({
                "id": uid,
                "name": name,
                "age": int(age),
                "tel": tel,
                "address": address
            })
            print("\033[32m用户添加成功\033[0m")
            logging.debug('用户{}添加成功,age:{},tel:{},address:{}'.format(name, age, tel, address))
    return users


def del_user(users):
    text = int(input("请输入删除用户的ID："))
    if text in [x['id'] for x in users]:
        for x in users:
            if x['id'] == text:
                users.remove(x)
                logging.debug('删除用户{}成功'.format(x['name']))
    else:
        print("\033[31m 用户ID不存在\033[0m")
        logging.warning('删除用户ID不存在')
    return users


def change_user(users):
    text = int(input("请输入修改用户ID："))
    if text in [x['id'] for x in users]:
        for x in users:
            if x['id'] == text:
                mod = input("Please choice your mod [name|age|tel|address]:")  # 需要修改的信息字段
                modmessage = x
                if mod == "name":
                    message = input("Please input your message:")  # 输入的修改内容
                    modmessage['name'] = message
                    logging.debug('name修改为{}'.format(message))
                    break
                elif mod == "age":
                    message = input("Please input your message:")
                    if message.isdigit() == False:
                        print("\033[1;31m 年龄输入有误\033[0m")
                    modmessage['age'] = message
                    logging.debug('age修改为{}'.format(message))
                    break
                elif mod == "tel":
                    message = input("Please input your message:")
                    if message.isdigit() == False:
                        print("\033[1;31m 电话号码输入有误\033[0m")
                    modmessage['tel'] = message
                    logging.debug('tel修改为{}'.format(message))
                    break
                elif mod == "address":
                    message = input("Please input your message:")
                    modmessage['address'] = message
                    logging.debug('address修改为{}'.format(message))
                    break
                else:
                    print("invalid option.")
    else:
        print("\033[31m 用户ID不存在\033[0m")
        logging.warning('修改用户ID不存在')
    return users


def print_users(users):
    print('-' * TABLE_SPLIT_LINE)
    print(TABLE_TPL.format(**TABLE_TITLE))
    print('-' * TABLE_SPLIT_LINE)
    for user in users:
        print(TABLE_TPL.format(**user))
    print('-' * TABLE_SPLIT_LINE)


def query_user(users):
    users_find = []
    text = input("请输入查询的字符串:")
    for user in users:
        if text == '' or user.get("name").find(text) != -1 or \
                        user.get("tel").find(text) != -1 or \
                        user.get("address").find(text) != -1:
            users_find.append(user)

    users_find_count = len(users_find)
    if users_find_count == 0:
        print("\033[1;31m 无数据\033[0m")
    elif users_find_count <= PAGE_SIZE:
        print_users(users_find)
    else:
        max_page = math.ceil(users_find_count / PAGE_SIZE)
        while True:
            text_page_num = input("共有{0}页, 请输入查询页码(1 ~ {0}): ".format(max_page))
            if text_page_num.isdigit() and int(text_page_num) <= max_page:
                page_num = int(text_page_num)
                print_users(users_find[(page_num - 1) * PAGE_SIZE: page_num * PAGE_SIZE])
            else:
                print("\033[1;31m 输入页码错误\033[0m")
                break


def list_user(users):
    if len(users) == 0:
        try:
            userFile = open(USER_FILE)
            userFileJson = userFile.read()
            userInfo = json.loads(userFileJson)  # 读取上次保存的用户信息
            userFile.close()
        except FileNotFoundError as e:
            pass
    else:
        print_users(users)


def lock_user():
    fhandler = open(LOCK_FILE, "w")
    fhandler.write(str(time.time()))
    fhandler.close()


def save_users(users):
    fhandler = open(USER_FILE, "w")
    fhandler.write(json.dumps(users))
    fhandler.close()
    print("\033[1;32m 存储用户信息成功\033[0m")


def operate(users):
    while True:
        op = input("Please input your option [add|del|update|list|find|exit]:")
        if op == "add":
            users = add_user(users)
        elif op == "del":
            del_user(users)
        elif op == "update":
            change_user(users)
        elif op == "list":
            list_user(users)
        elif op == "find":
            query_user(users)
        elif op == "exit":
            save_users(users)
            break
        else:
            print("\033[1;31m 输入参数有误\033[0m")


def main():
    if not is_unlock():
        print("\033[1;31m 用户被锁定，请稍后重试\033[0m")
        return
    if login():
        users = get_users()
        operate(users)
    else:
        lock_user()


main()
