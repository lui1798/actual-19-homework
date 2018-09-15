#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/9/11 上午12:40
# @File    : modulefile.py
# @Software: PyCharm

import configparser

def ReadConfig(filename, section, key):
    config = configparser.ConfigParser()
    config.read(filename)

    if key in config[section]:
        return config[section][key]
