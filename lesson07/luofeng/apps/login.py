import os
from apps.utils.msg import *
from apps.utils.http import Get, GetAuth
import time
from apps.utils.file import *
from apps.utils.msg import *
import sys


# 锁定用户函数
def LockUser():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    lock_options, ok = ReadConfigFile(os.path.join(BASEDIR, '..', 'conf.ini'), 'LOCK')

    if not ok:
        errmsg = lock_options
        WarnMsg(errmsg)
        sys.exit()

    LOCK_FILE = lock_options.get('lock_file')

    current_time = str(time.time())
    WriteFile(LOCK_FILE, current_time)


# 判断是否被锁定函数
def IsLock():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    lock_options, ok = ReadConfigFile(os.path.join(BASEDIR, '..', 'conf.ini'), 'LOCK')

    if not ok:
        errmsg = lock_options
        WarnMsg(errmsg)
        sys.exit(1)

    LOCK_FILE = lock_options.get('lock_file')
    LOCK_DURATION = float(lock_options.get('lock_duration'))

    lock_time = 0
    res, ok = ReadFile(LOCK_FILE)

    try:
        lock_time = float(res)
    except Exception as e:
        pass

    if time.time() - lock_time > LOCK_DURATION:
        return False
    else:
        lt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(ReadFile(LOCK_FILE)[0]) + LOCK_DURATION))
        WarnMsg("用户被锁定，锁定至：{}，请过后再试！".format(lt))
        return True


def Auth_login_token(url, token):
    headers = {'Authorization': 'Token {}'.format(token)}
    return Get(url, headers=headers)


def Auth_login_passwd(url, username, password):
    return GetAuth(url, username, password)


# 登录函数
def Login():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    auth_info, ok = ReadConfigFile(os.path.join(BASEDIR, '..', 'conf.ini'), 'AUTH')
    if not ok:
        errmsg = auth_info
        WarnMsg(errmsg)
        return False

    MAX_LOGIN_TIMES = float(auth_info.get('max_login_times'))

    is_login = False
    count = 1
    while count <= MAX_LOGIN_TIMES:
        if auth_info.get('auth_method_for_token') == '1':
            # 测试token: 218f44a13dd981c96ef3dcbedc6fa576a067039c
            token = InputMsg("请输入你github账号的token: ")
            msg, ok = Auth_login_token(auth_info.get('url'), token)
        else:
            username = InputMsg("请输入你github的账号: ")
            password = InputMsg("你输入你github的密码{}: ".format(username))
            msg, ok = Auth_login_passwd(auth_info.get('url'), username, password)

        if ok:
            SuccMsg("认证成功！")
            is_login = True
            return is_login
        else:
            if count == MAX_LOGIN_TIMES:
                WarnMsg("认证失败，失败超过三次，被锁定！")
            else:
                WarnMsg("认证失败，请重试！")
            count += 1
    LockUser()
    is_login = False
    return is_login