#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : lock.py
# @Author: ZhouGui
# @Date  : 2018/9/10
# @Description :判断锁文件
import time
from utils import config

LOCK_FILE = config.ReadConfigFile('conf.ini', 'LOG', key='LOCKFILE')
LOCK_DURATION = 60


def is_unlock():
    beforeTime = 0
    try:
        fhandler = open(LOCK_FILE)
        cxt = fhandler.read()
        fhandler.close()
        beforeTime = float(cxt)
    except Exception as  e:
        pass
    return time.time() - beforeTime > LOCK_DURATION


def lock_user():
    fhandler = open(LOCK_FILE, "w")
    fhandler.write(str(time.time()))
    fhandler.close()
