#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/9/15 下午11:34
# Author        : Yuhao.Wang
# FileName      : mdlog.py
# Description   : 
#

import logging
from mdconfig import ReadConfig

def log():
    log_file = ReadConfig('config.ini', 'LOG', 'LOGFILE')
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
        filename=log_file,
        filemode='a'
    )