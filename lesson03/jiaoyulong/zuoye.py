#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 下午10:53
# @Author  : jiaoyulong
# @Site    :
# @File    : user_manage.py
# @Software: PyCharm

import sys, json, time, datetime


# 定义循环次数和认证用户名和密码
count = 3

# 定义登录成功后提示信息
succ_msg = '''\033[32m
-------------------------------
欢迎登录用户系统，请选择对应的操作选项
-------------------------------
    1. 增加用户信息(add)
    2. 删除用户信息(delete)
    3. 更新用户信息(update)
    4. 查询用户信息(find)
    5. 退出用户管理系统(exit)
-------------------------------
\033[0m'''

# 获取用户名和密码
# data = {'user': 'admin', 'password': 123456, 'is_locked': False, 'locked_at': None}
#
# f = open('user_info.txt', 'w')
# f.write(json.dumps(data))

f = open('user_info.txt', 'r')
res = f.readlines()
user_info = json.loads(res[0])
cur_time = time.time()


def is_locked():
    if user_info['is_locked'] == True and user_info['locked_at'] > cur_time:
        return False
    else:
        return True

while is_locked():
    if count > 0:
        try:
            username = input("please enter your username: ")
            password = int(input("please enter your password: ").strip())
            while count > 0:
                # 判断登录用户和密码
                if username == user_info['user'] and password == user_info['password']:
                    print(succ_msg)
                    op = input("请输入要操作的选项(输入序列号)").strip()
                    if op == '1':
                        name = input("请输入姓名：").strip()
                        address = input("请输入地址：").strip()
                        age = int(input("请输入年龄：").strip())
                        data = {'name': name, 'address': address, 'age': age}
                        print(data)
                        f = open('user_list.txt', 'a')
                        f.write(json.dumps(data) + '\n')
                        print('添加成功')
                        f.close()
                        continue

                    elif op == '2':
                        f = open('user_list.txt', 'r')
                        res = f.readlines()
                        for i in res:
                            print(i)
                        try:
                            idx = int(input('输入要删除的序列号'))
                            res.remove(idx)
                        except:
                            print('索引错误！')

                    elif op == '3':
                        print('update')
                    elif op == '4':
                        print('find')
                    elif op == '5':
                        print('exit')
                    else:
                        print('请输入正确的操作序列')



                else:
                    count -= 1
                    if count == 0:
                        break
                    else:
                        print('密码错误，你还有%s次机会' % count)
                        break
        except:
            print('请输入合法字符')
    else:
        print('密码错误3次，今天没机会了！')
        locked_at = time.time() + (60 * 60 * 24)
        data = {'user': 'admin', 'password': 123456, 'is_locked': True, 'locked_at': locked_at}
        f = open('user_info.txt', 'w')
        f.write(json.dumps(data))
        f.close()
        exit()



# 用户登录
