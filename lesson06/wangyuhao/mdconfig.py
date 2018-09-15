#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/9/15 下午11:01
# Author        : Yuhao.Wang
# FileName      : mdconfig.py
# Description   : 
#
'''
    主要是configparser模块的应用,
    用法:
        获取某个区域的某个key

'''
import configparser

def ReadConfig(filename, section, key):
    config = configparser.ConfigParser()
    config.read(filename)

    if key in config[section]:
        return config[section][key]
