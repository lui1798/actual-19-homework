# encoding:utf-8
import time

LOCK_FILE = "lock"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123"
MAX_LOGIN_TIME = 3
is_login=False

for i in range(MAX_LOGIN_TIME):
    username = input("pls 输入用户名")
    passwrod = input("pls 输入密码")

    if ADMIN_USERNAME == username and ADMIN_PASSWORD == passwrod:
        is_login = True
        break
    else:
        # 注意最后一次登录
        if MAX_LOGIN_TIME - 1 == i:
            print("登录失败，锁定了")
        else:
            print("登录失败，请重输入")

if is_login:
    print("登录成功")
else:
    fhandler = open("LOCK_FILE", "w")
    fhandler.write(str(time.time()))  #登录失败写入时间戳到文件
    fhandler.close()
    print("登录失败,已记录时间戳到文件")
