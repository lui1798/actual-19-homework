#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/9/15 下午11:05
# Author        : Yuhao.Wang
# FileName      : mdlock.py
# Description   : 
#

import logging
import time
from mdconfig import ReadConfig

'''
    获取配置
'''
lock_file = ReadConfig('config.ini', 'LOCK', 'LOCKFILE')
lock_duration = ReadConfig('config.ini', 'LOCK', 'LOCKDURATION')

'''
    判断锁定
'''

def is_unlock():
    lock_time = 0

    with open(lock_file,'r') as lock_f:
        lock_time = float(lock_f.read())

    return time.time() - lock_time > lock_duration

'''
    上锁
'''

def is_lock(username):
    lock_cur_time = time.time()
    with open(lock_file,'w') as lock_f:
        lock_f.write(lock_cur_time)
    print("\033[31m{}\033[0m".format("Sorry.Your account has been locked! Please try again after 24 hours!"))
    logging.warning("%s has been locked at %s", username, lock_cur_time)


def lock_login():
    print("\033[31m{}\033[0m".format("Sorry.Your account has been locked! Please try again after 24 hours!"))
    logging.warning('User has been locked. Try to login again.')

