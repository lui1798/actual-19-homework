#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/9/11 上午12:00
# @File    : modeulelogin.py
# @Software: PyCharm


import getpass
import logging
import requests
import json
from modulefile import ReadConfig


max_login_times = ReadConfig('config.ini', 'LOCK', 'LOCKTIMES')
ADMIN_USERNAME = ReadConfig('config.ini', 'USER', 'USERNAME')


'''
显示登录信息
'''
def login():
    is_login = False

    for i in range(int(max_login_times)):
        username = input("Please input administrator account: ")
        TOKEN = getpass.getpass("Please input your login Token:")
        headers = {'Authorization': 'token ' + TOKEN}

        req = requests.get('https://api.github.com/user', headers=headers)
        userinfo = json.dumps(req.json(), indent=4)
        djson = json.loads(userinfo)

        if TOKEN == 'xxxxxxxxx' and djson['login'] == username:
            is_login = True
            logging.info('administrator login success.')
            break

        if int(max_login_times) - 1 == i:
            lockstr = "Sorry.Your account has been locked! Please try again after 24 hours!"
            print("\033[31m{}\033[0m".format(lockstr.center(50, '*')))
        else:
            print("\033[31m{}\033[0m".format("You just have three chances,Please try again!"))

    return is_login
