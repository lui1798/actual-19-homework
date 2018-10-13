#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : login.py
# @Author: ZhouGui
# @Date  : 2018/9/9
# @Description : 用户登录操作
import time
import logging
import requests
import getpass
from utils import config

LOGFILE = config.ReadConfigFile('conf.ini', 'LOG', key='LOGFILE')
logger = logging.getLogger()
fh = logging.FileHandler(LOGFILE, encoding='utf-8')
fm = logging.Formatter('[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
fh.setFormatter(fm)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


def login():
    is_login = False
    LOGIN_COUNT = 0  # 登录次数
    while LOGIN_COUNT < 3:
        username = input("Please input your github username:")
        password = getpass.getpass("Please input your github password:")
        req = requests.get('https://api.github.com/', auth=('{}'.format(username), '{}'.format(password)))
        if req.status_code == 200 and username.strip() and password.strip():
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
