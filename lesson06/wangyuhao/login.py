#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/9/15 下午11:39
# Author        : Yuhao.Wang
# FileName      : login.py
# Description   : 
#
import getpass
import logging
import requests
import json
from mdconfig import ReadConfig

lock_times = ReadConfig('config.ini', 'LOCK', 'LOCKTIMES')
admin_user = ReadConfig('config.ini', 'USER', 'USERNAME')

'''

'''

def login():
    is_login = False

    for i in range(1, int(lock_times)):
        user_name = input("pls input admin username: ".strip())
        TOCKEN = getpass.getpass("pls input your tocken: ".strip())
        headers = {
            "Authorization": "tocken" + TOCKEN
        }

        req = requests.get('https://api.github.com/user', headers=headers)
        userinfo = json.dumps(req.json(), indent=4)
        djson = json.loads(userinfo)

        if TOCKEN == 'xxxxxxxxx' and djson['login'] == admin_user:
            is_login = True
            logging.info("admin login success!")
            break

        if i == lock_times:
            lockstr = "Sorry.Your account has been locked! Please try again after 24 hours!"
            print("\033[31m{}\033[0m".format(lockstr.center(50, '*')))
        else:
            print("\033[31m{}\033[0m".format("You just have three chances,Please try again!"))

    return is_login
