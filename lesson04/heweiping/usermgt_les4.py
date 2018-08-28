#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2018/8/26 0026
# @Author    : Roger
# @File      : usermgt_les4.py
# @Software  : PyCharm
# @Desc      :

import time
import getpass
import json
import math
import string

# 需要涉及到3个文件：
# lock：校验是否在锁定时间
# user.py：程序主文件
# user.json:存储用户信息
# 大写字母的变量为不可变变量，小写字母为可变变量
# 定义常量
LOCK_FILE = 'lock'
# 定义登录失败间隔
LOCK_DURATION = 30

# 定义登录名用户
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

# 定义每30秒最多登录次数
MAX_LOGIN_TIMES = 3
USER_FILE = 'user.json'

# 定义需要输入多少字段
USER_INFO_NUM = 4

# 定义输出格式
TABLE_TPL = '{id:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
TABLE_SPLIT_LINE = 64
TABLE_TITLE = {'id': 'id', 'name': 'name', 'age': 'age', 'tel': 'tel', 'address': 'address'}

# 定义每页显示多少行
PAGE_SIZE = 10


# 定义公共的变量
# users = []


# 1. 检查是否被锁定
def is_unlock():
    lock_time = 0
    try:
        fhandler = open(LOCK_FILE, 'r')
        cxt = fhandler.read()
        fhandler.close()
        lock_time = float(cxt)
    except Exception as e:
        print(e)
    # 判断是否被锁定
    lock_status = time.time() - lock_time > LOCK_DURATION
    return (lock_status)


# 2. 未被锁定, 则登录
def is_login():
    if is_unlock():
        login_status = False

        for i in range(MAX_LOGIN_TIMES):
            username = input('请输入用户名:').strip()
            password = input('请输入密码:').strip()
            # getpass无法在pycharm调试
            # password = getpass.getpass('请输入密码:')
            if ADMIN_USERNAME == username and ADMIN_PASSWORD == password:
                login_status = True
                break

            # 登陆失败，取最新的失败时间写入锁定文件
            if MAX_LOGIN_TIMES - 1 == i:
                print('登陆失败, 锁定用户')
                fhandler = open(LOCK_FILE, 'w')
                fhandler.write(str(time.time()))
                fhandler.close()
                exit()
            else:
                print('登陆失败, 请重新输入用户名, 密码')
                fhandler = open(LOCK_FILE, 'w')
                fhandler.write(str(time.time()))
                fhandler.close()

    else:
        print('已经被锁定, 请稍后再试')
        login_status = False
    return login_status


def load_user():
    users = []
    if is_login():
        print('登录成功')
        # 3. 登录完成, 加载用户
        try:
            fhandler = open(USER_FILE, 'r')
            cxt = fhandler.read()
            fhandler.close()
            users = json.loads(cxt)
            return users
        except Exception as e:
            print(e)
    # 登录失败，退出系统
    else:
        exit()


def check_age(age):
    has_error = False
    if not age.isdigit() or int(age) not in range(100):
        print('年龄输入有问题：必须是纯数字，范围在1～100')
        has_error = True
    return has_error


def check_tel(tel):
    has_error = False
    if not tel.isdigit() or not tel.startswith('1') or len(tel) != 13:
        print('手机号码有问题：必须是纯数字，长度为13，以1开头')
        has_error = True
    return has_error


def check_other(address):
    has_error = False
    if address[0] not in string.ascii_letters:
        print('姓名或者地址必须以字母开头')
        has_error = True
    return has_error


def check_name(name, users):
    has_error = False
    namelist = []
    for user in users:
        namelist.append(user['name'])
    if not check_other(name) and name in namelist:
        print('用户已存在')
        has_error = True
    return has_error


# 4. 操作add,modify,delete,query,save,exit
def add_user(users):
    name = input('请输入姓名:').strip()
    age = input('请输入年龄:').strip()
    tel = input('请输入手机号码:').strip()
    address = input('请输入城市:').strip()
    age_has_error = check_age(age)
    tel_has_error = check_tel(tel)
    name_has_error = check_name(name, users)
    add_has_error = check_other(address)

    if not age_has_error and not tel_has_error and not name_has_error and not add_has_error:
        # 生成id
        uid = max([x.get('id') for x in users] + [0]) + 1
        users.append({
            'id': uid,
            'name': name,
            'age': int(age),
            'tel': tel,
            'address': address
        })
        print('添加成功')
    else:
        print('添加失败')
    return users


def modify_user(users):
    text = input('请输入修改用户ID:')
    is_exists = False
    uid = 0
    nameflag = True
    if text.isdigit():
        uid = int(text)
        for user in users:
            if uid == user.get('id'):
                print('更新用户信息:' + json.dumps(user))
                is_exists = True
                break
    if is_exists:
        name = input('请输入姓名:').strip()
        age = input('请输入年龄:').strip()
        tel = input('请输入手机号码:').strip()
        address = input('请输入城市:').strip()
        age_has_error = check_age(age)
        tel_has_error = check_tel(tel)
        name_has_error = check_name(name, users)
        add_has_error = check_other(address)

        if not age_has_error and not tel_has_error and not name_has_error and not add_has_error:
            for user in users:
                if uid == user.get('id'):
                    user['name'] = name
                    user['age'] = int(age)
                    user['tel'] = tel
                    user['address'] = address
                    print('更新成功')
                    break
    else:
        print('输出ID错误')
    return users


def del_user(users):
    text = input('请输入删除用户的ID:')
    if text.isdigit():
        uid = int(text)
        for user in users:
            if uid == user.get('id'):
                users.remove(user)
                print('删除用户成功')
                break
        else:
            print('输入ID错误')
    else:
        print('输入ID错误')
    return users


def query_user(users):
    text = input('请输入查询的字符串:')
    users_find = []
    for user in users:
        if text == '' or user.get('name').find(text) != -1 or \
                        user.get('tel').find(text) != -1 or \
                        user.get('address').find(text) != -1:
            users_find.append(user)

    users_find_count = len(users_find)
    if users_find_count == 0:
        print('无数据')
        # 格式化输出
    elif users_find_count <= PAGE_SIZE:
        print(TABLE_TPL.format(
            **TABLE_TITLE))  # TABLE_TPL.format(id='id', name='name', age='age', tel='tel', address='address')
        print('-' * TABLE_SPLIT_LINE)
        for user in users_find:
            print(TABLE_TPL.format(**user))
        print('-' * TABLE_SPLIT_LINE)
    else:
        # ceil是向上取整，定义最大页数
        max_page = int(math.ceil(users_find_count / PAGE_SIZE))

        while True:
            text_page_num = input('共有{0}页, 请输入查询页码(1 ~ {0}): '.format(max_page))
            if text_page_num.isdigit() and int(text_page_num) <= max_page:
                page_num = int(text_page_num)
                print(TABLE_TPL.format(
                    **TABLE_TITLE))  # TABLE_TPL.format(id='id', name='name', age='age', tel='tel', address='address')
                print('-' * TABLE_SPLIT_LINE)
                for user in users_find[(page_num - 1) * PAGE_SIZE: page_num * PAGE_SIZE]:
                    print(TABLE_TPL.format(**user))
                print('-' * TABLE_SPLIT_LINE)
            else:
                print('输入页码错误,退出查询')
                break


def save_user(users):
    fhandler = open(USER_FILE, 'w')
    fhandler.write(json.dumps(users))
    fhandler.close()
    print('存储用户信息成功')


def main():
    users = load_user()
    while True:
        op = input('请输入操作(add,modify,delete,query,save,exit):')
        if op == 'add':
            users = add_user(users)
        elif op == 'modify':
            users = modify_user(users)
        elif op == 'delete':
            users = del_user(users)
        elif op == 'query':
            query_user(users)
        elif op == 'save':
            save_user(users)
        elif op == 'exit':
            save_user(users)
            break
        else:
            print('输入错误')


if __name__ == '__main__':
    main()
