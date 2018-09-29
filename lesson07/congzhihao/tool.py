'''
工具函数
'''
import hashlib
import configparser
import time
import json
import getpass


'''读ini文件'''
def ReadConfigFile(filename,section,key):
    cp = configparser.ConfigParser()
    cp.read(filename)
    return (cp[section][key])

'''对str生成hash md5'''
def GenHashmd5(s):
    hash5 = hashlib.md5(s.encode("utf-8"))
    return hash5.hexdigest()


def login(user,password,max_times):
    #登陆用户名及密码检验，如果输入三次错误返回falseaaa
    login_times = 0
    while True:
        user_name = input("please input username:")
        user_password = getpass.getpass("please input password:")
        if user_name.strip() == user and GenHashmd5(user_password.strip()) == password:
            return True
        else:
            print("用户或密码输入错误！")
            login_times = login_times +1
            print("还有{}次机会！！！".format(max_times - login_times))
        if login_times == max_times:
            print("用户锁定中，请稍后再试！")
            return False

def login_lock(conf_file):
    #锁定用户
    login_time = time.time()
    lock_file = ReadConfigFile(conf_file,"LOCK","LOCKFILE")
    ff = open(lock_file,"w")
    ff.write(json.dumps(login_time))
    ff.close()


def lock_check(conf_file,lock_time):
    #检查用户是否锁定
    lock_file = ReadConfigFile(conf_file, "LOCK", "LOCKFILE")
    ff = open(lock_file,"r")
    membu = ff.read()
    unlock_time = float(json.loads(membu)) + lock_time
    ff.close()
    if time.time() > unlock_time:
        return True
    else:
        return False




