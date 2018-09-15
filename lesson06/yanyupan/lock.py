import os
import time
import config
from utils.file import *
from utils.print_msg import *


# 锁定用户函数
def LockUser():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    try:
        lock_options, ok = config.ReadConfig(os.path.join(BASEDIR, 'conf.ini'), 'LOCK')
    except Exception as e:
        return

    LOCK_FILE = lock_options['lock_file']

    current_time = str(time.time())
    Write_File(LOCK_FILE, current_time, '')


# 判断是否被锁定函数
def IsUnlock():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    try:
        lock_options, ok = config.ReadConfig(os.path.join(BASEDIR, 'conf.ini'), 'LOCK')
    except Exception as e:
        return

    LOCK_FILE = lock_options['lock_file']
    LOCK_DURATION = float(lock_options['lock_duration'])

    lock_time = 0
    res = Read_File(LOCK_FILE)
    try:
        lock_time = float(res)
    except Exception as e:
        pass

    if time.time() - lock_time > LOCK_DURATION:
        return True
    else:
        lt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(Read_File(LOCK_FILE)) + LOCK_DURATION))
        WarnMsg("用户被锁定，锁定至：{}，请过后再试！".format(lt))
        return