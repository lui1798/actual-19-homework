#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/8/26 下午8:31
# Author        : Yuhao.Wang
# FileName      : wyh_hmw_user_system_v2_dic_list.py
# Description   : 
#
import time
import json
ADMIN_USER = 'admin'
ADMIN_PASS = '123'
LOCK_FILE='user.lock'
USER_FILE='user.json'
LOCK_DURATION = 10

TABLE_TPL = '{id:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
TABLE_SPLIT_LINE = 64
TABLE_TITLE = {"id" : "id", "name" : "name", "age" : "age", "tel" : "tel" , "address": "address"}

PAGE_SIZE = 2

def is_unlock():
    with open(LOCK_FILE,'r') as lockf:
        lock_str = lockf.read()
        if lock_str:
            lock_time = float(lock_str)
            now_time = time.time()
        return now_time - lock_time > LOCK_DURATION

def is_login():
    count = 3
    while True:
        username = input('请输入您的用户名:').strip()
        password = input('请输入您的密码:').strip()
        if username == ADMIN_USER and password == ADMIN_PASS:
            print('欢迎你,%s' % ADMIN_USER)
            return True
        else:
            count -= 1
            print('三次输入错误,用户被锁定') if count == 0 else print('用户名或密码错误,请重新输入!')
            return False

def lock_user():
    with open(LOCK_FILE,'w') as lockf:
        lockf.write(time.time())
        return True

def load_user():
    users = []
    with open(USER_FILE,'r') as userf:
        data = userf.read()
    try:
        users = json.loads(data)
        return users
    except Exception as e:
        print(e)

def user_add(users):
    while True:
        text = input('请依次输入用户名,年龄,电话,地址,信息之间用空格分割:').strip()
        user = text.split()
        user_template = ['name','age','tel','adress','id']
        if len(user) == 4:
            name,age,tel,address = user
            has_err = False
            if not age.isdigit() or not tel.isdigit():
                print('输入的年龄或电话不为数字!')
                continue
            else:
                uid = max([ x['id'] for x in users ] + [0]) + 1
                user.append(uid)
                user_dic = dict(zip(user_template,user))
                users.append(user_dic)
                print('添加用户成功!')
                return users
        else:
            print('输入错误!')


def user_del(users):
    while True:
        del_uid = input('请输入您要删除的用户ID:')
        if del_uid.isdigit():
            del_uid = int(del_uid)
            for user in users:
                if user['id'] == del_uid:
                    users.remove(user)
                    return True
            else:
                print('所删除的用户不存在!')
        else:
            print('请输入数字!')

def user_modi(users):
    while True:
        mo_uid = input('请输入您要修改的用户ID:')
        if mo_uid.isdigit():
            mo_uid = int(mo_uid)
            for user in users:
                if user['id'] == mo_uid:
                    while True:
                        text = input('请依次输入用户名,年龄,电话,地址,信息之间用空格分割:').strip()
                        user_list = text.split()
                        user_template = ['name', 'age', 'tel', 'adress', 'id']
                        if len(user_list) == 4:
                            name, age, tel, address = user
                            has_err = False
                            if not age.isdigit() or not tel.isdigit():
                                print('输入的年龄或电话不为数字!')
                                continue
                            else:
                                user.append(mo_uid)
                                user_dic = dict(zip(user_template, user_list))
                                users.append(user_dic)
                                print('添加用户成功!')
                                return users
                        else:
                            print('输入错误!')

        else:
            print('请输入数字!')
    pass
def user_find(users):
    while True:
        find_users = []
        keyword = input('请输入您所需要查找的关键字:')
        for user in users:
            if keyword in user['name'] or keyword in user['tel'] or keyword in user['address']:
                find_users.append(user)
                return find_users

def print_users(users):
    print('-' * TABLE_SPLIT_LINE)
    print(TABLE_TPL.format(**TABLE_TITLE))
    print('-' * TABLE_SPLIT_LINE)
    for user in users:
        print(TABLE_TPL.format(**user))
    print('-' * TABLE_SPLIT_LINE)



def save_users(users):
    with open(USER_FILE,'w') as savef:
        savef.write(users)
        return True
    print('保存完毕!')


def operator(users):
    while True:
        oper_list = ['用户添加','用户删除','用户查询','用户修改','保存修改','退出系统']
        op = input('''
        请输入的操作编号:
        [1].{}
        [2].{}
        [3].{}
        [4].{}
        [5].{}
        [6].{}
        '''.format(*oper_list))
        if op == '1':
            print('进入用户添加操作页面')
            user_add(users)
        elif op == '2':
            print('进入用户删除操作页面')
            user_del(users)
        elif op == '3':
            print('进入用户查询操作页面')
            user_find(users)
        elif op == '4':
            print('进入用户修改操作页面')
            user_modi(users)
        elif op == '5':
            print('正在保存修改...')
        elif op == '6':
            exit()


def main():
    #1.判断锁
    #2.用户登录
    #3.获取数据
    #4.用户操作
    if is_unlock():
        if is_login():
            #加载数据
            users = load_user()
            #用户操作
            operator(users)
        else:
            #锁定用户
            lock_user()
    else:
        print('用户被锁定,请稍后再试!')


main()