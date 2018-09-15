#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/9/10 下午11:54
# @File    : log.py
# @Software: PyCharm

import logging
from modulefile import ReadConfig



def log():
    logfile = ReadConfig('config.ini', 'LOG', 'LOGFILE')
    logging.basicConfig(level=logging.DEBUG,
        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
        filename=logfile,
        filemode='a')