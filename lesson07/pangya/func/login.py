# 定义常量
MAX_TIMES = 3
LOCK_TIME = "lock_time.txt"


#导入模块
import sys
import file
import requests
import os
import datetime
import json


def is_login():
    token_value = input("请输入token认证码：")
    is_login = False
    headers = {'Authorization': 'token ' + token_value}
    req = requests.get('https://api.github.com/user', headers=headers)
    if req.status_code==200:
        is_login = True
    return is_login

def lock_flag():
    lock_flag = False
    lock_time_file,flag=file.ReadConfigFile('config.ini', 'DB', 'LOCKFILE')
    if os.path.exists(lock_time_file) == True:
        lock_time_str=file.ReadFile(lock_time_file)
        lock_time = datetime.datetime.strptime(lock_time_str, "%Y-%m-%d %H:%M:%S")
        interval = datetime.datetime.now() - lock_time
        if interval.days < 1:
            lock_flag = True
    return lock_flag

def lock_user():
    lock_time = datetime.datetime.now()
    lock_time_str = lock_time.strftime("%Y-%m-%d %H:%M:%S")
    # fd = open('config/lock_time.txt', 'w')
    # message = json.dumps(lock_time_str)
    # fd.write(message)
    # fd.close()
    file.WriteFile(file.ReadConfigFile('config.ini', 'DB', 'LOCKFILE')[0], lock_time_str)
