import json
import time
import datetime
import pickle
import requests
import math
import base64
import logging
import getpass
import configparser
import pymysql
import os
import xlwt,xlrd
import jinja2
import prettytable


config = configparser.ConfigParser()
config.read('conf.ini')

LOGFILE = config['LOG']['LOGFILE'] + '.' + str(datetime.date.today())

# 定义日志等级和输出信息

def log_log(level='debug',action='message'):
    logging.basicConfig(level=logging.DEBUG,
                format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                datefmt='%Y-%m-%d %I:%M:%S %p',
                filename=LOGFILE,
                filemode='a'
                )

    if level == 'debug':
        logging.debug(action)
    elif level == 'info':
        logging.info(action)
    elif level == 'warn':
        logging.warn(action)
    elif level == 'error':
        logging.error(action)
    else:
        logging.critical(action)

