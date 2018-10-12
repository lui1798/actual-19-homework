# 用户信息管理系统
# 可以实现以下功能：
# 1、账户1天内只能登陆失败3次，超过失败次数则锁定
# 2、变量从配置文件中获取
# 3、密码进行密文输入
# 4、对用户信息的增删改查操作。查看可以分页展示，并导出csv文件和html文件 功能
# 5、对数据进行存储到数据库，方便以后读取
# 6、打印追加日志到 error.log 里，并按天切割

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = caozhi
# 最后更新时间 2018-10-12
# version:5.1

import json
import time
import datetime
import pickle
import requests
import math
import base64
import logging
import getpass
import configparser
import pymysql
import os
import xlwt,xlrd
import jinja2
import prettytable
import output_log
import login_def
import operate


def main():
    if is_login:
        output_log.log_log('debug','登陆成功')
        print('=' * 70)
        print('''
    \033[31m欢迎来到某某信息管理系统 \033[0m
    ''')
        print('=' * 70)
        break_flag = 0

        while 1:
            if break_flag:
                break
            print('''
     执行操作的序号:
     1、 插入一个用户信息.
     2、 查询当前用户信息.
     3、 更新某个用户信息.
     4、 删掉某个用户信息.
     5、 退出系统.
                ''')
            # 输入对用户信息的操作 按数据库逻辑实现,id 为主键
            action = input('\033[34m请输入需要执行操作的序号: \033[0m').strip()
 
            dict = {'1':operate.insert, '2': operate.select, '3':operate.update, '4':operate.delete, '5':operate.exit_system}
            break_flag = dict.get(action, operate.other_action)()


if __name__ == '__main__':
    is_login = login_def.login_def()
    main()
