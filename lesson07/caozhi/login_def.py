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

config = configparser.ConfigParser()
config.read('conf.ini')

my_name = config['CONF']['my_name']
MAX_LOGIN_TIMES = config['CONF']['MAX_LOGIN_TIMES']
PAGE_LIST = int(config['CONF']['page_list'])
lock_time = int(config['LOCK']['lock_time'])
break_flag = 0
has_error = 0

def login_def():
    now_time = time.time()
    lasttime = float(config['LOCK']['lasttime'])
    count = int(config['LOCK']['count'])
    usermessage = {'count': count, 'lasttime': lasttime}
    usermessage['lasttime'] = now_time
    config.set("LOCK", "lasttime", str(now_time))
    config.write(open('conf.ini', "w"))

    drop = now_time - lasttime

    # 判断是否大于1天

    if int(drop) > lock_time:
        usermessage['count'] = MAX_LOGIN_TIMES

    count = int(usermessage.get('count'))
    is_login = 0
    for i in range(count):
        TOKEN = getpass.getpass('\033[33m 请输入你的TOKEN(5775cbe26a3a3b153a3be6e68b9925e8db10557e): \033[0m').strip()
        headers = {'Authorization': 'token ' + TOKEN}
        #user_name = input('\033[33m 请输入你的姓名: \033[0m').strip()
        #password = getpass.getpass('\033[33m 请输入你的密码: \033[0m').strip()

        req = requests.get('https://api.github.com/user', headers=headers)
        output_log.log_log('info', json.dumps(req.json()))
        output_log.log_log('info', req.url)
        res = req.json()

        #if user_name == usermessage['name'] and password == usermessage['passwd']:
        if res.get("login",None) == my_name:
            print('\033[32m login success ---> 登陆成功 \033[0m')
            is_login = 1
            break
        else:
            count -= 1
            usermessage['count'] = count
            config.set("LOCK", "count", str(count))
            config.write(open('conf.ini', "w"))
            print('用户信息错误，登陆失败，还有 %d 次机会' % count)
            output_log.log_log('warn', '用户信息错误，登陆失败')

    else:
        print('\033[31m请在 60秒后(为调试方便，使用60s，可自定义调整)重试， 或者联系我...\033[0m')
        output_log.log_log('warn', '用户信息错误，登陆失败，已锁定')
    return is_login

