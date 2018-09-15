#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: ZhouGui
# @Date  : 2018/9/9
# @Description : 配置文件
import os
import configparser

BASEDIR = os.path.dirname(os.path.abspath(__file__))
INIFILE = os.path.join(BASEDIR, 'conf.ini')


def ReadConfigFile(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(INIFILE, encoding='utf-8')
    if not config.sections():
        return 'conf.ini file is empty'
    if not config.has_section(section):
        return 'section {} not found'.format(section)
    if not key:
        return config.items(section)
    else:
        return config[section][key]
