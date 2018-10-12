#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/9/10 下午11:57
# @File    : lock.py
# @Software: PyCharm

import logging
import time
from modulefile import ReadConfig



'''
设置常量
'''

lock_duration = 30
lockfile = ReadConfig('config.ini', 'LOCK', 'LOCKFILE')


'''
判断是否锁定
'''
def is_unlock():

    lock_time = 0

    try:
        locktime_file = open(lockfile,"r")
        hander = locktime_file.read()
        locktime_file.close()
        lock_time = float(hander)
    except FileNotFoundError:
        logging.warning('lock_file not found.')
    except:
        pass

    return time.time() - lock_time > lock_duration

'''
写入锁定时间
'''
def is_lock():
    lockwritetime = open(lockfile, 'w')
    lockwritetime.write(str(time.time()))
    lockwritetime.close()
    logging.warning('User has been locked.')


'''
输出锁定信息
'''
def lock_login():
    print("\033[31m{}\033[0m".format("Sorry.Your account has been locked! Please try again after 24 hours!"))
    logging.warning('User has been locked. Try to login again.')