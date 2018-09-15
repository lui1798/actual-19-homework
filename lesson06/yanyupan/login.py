import os
import getpass
import config
from utils.print_msg import *
from utils.hash import *


# 登录函数
def Login():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    try:
        login_options, ok = config.ReadConfig(os.path.join(BASEDIR, 'conf.ini'), 'LOGIN')
    except Exception as e:
        return

    MAX_LOGIN_TIMES = float(login_options['max_login_times'])
    ADMIN_NAME = login_options['admin_name']
    ADMIN_PWD = login_options['admin_pwd']


    is_login = False
    count = 1
    while count <= MAX_LOGIN_TIMES:
        username = InputMsg("请输入管理员用户名：")
        if username == ADMIN_NAME:
            count = 1
            while count <= MAX_LOGIN_TIMES:
                # password = InputMsg("请输入管理员密码：")
                password = getpass.getpass("请输入管理员密码：")
                if hash(password) == ADMIN_PWD:
                    SuccMsg("你已经登陆成功！")
                    is_login = True
                    return is_login
                else:
                    WarnMsg("你输入的密码有误，请重新输入！")
                    count += 1
        else:
            WarnMsg("你输入的用户名错误，请重新输入！")
            count += 1

    WarnMsg("你输入错误已经超过三次，账号被锁定！")
    is_login = False
    return is_login
