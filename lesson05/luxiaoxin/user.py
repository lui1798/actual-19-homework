#encoding: utf-8
#-----导入模块--------
import time
import json
import getpass
import logging

#-----定义公用常量-------
#管理员登录锁定文件和时长30s
LOCK_FILE = 'lock'
LOCK_INTERVAL = 30
#系统管理员用户名密码
ADMIN_NAME = 'admin'
ADMIN_PASSWD = '51@reboot'
#最大登录次数
MAX_LOGIN_COUNT = 3
#用户信息存储文件
USER_FILE = 'user.json'
#用户信息长度
USER_INFO_NUM = 4
#打印用户信息格式
TABLE_TPL = '|{id:^10}|{name:^10}|{age:^5}|{tel:^15}|{address:^20}|'
TABLE_TITLE = {"id" : "id", "name" : "name", "age" : "age", "tel" : "tel" , "address": "address"}
TITLE = TABLE_TPL.format(**TABLE_TITLE)
TABLE_SPLIT_LINE = '-' * (len(TITLE))
PAGE_SIZE = 2
#系统日志配置选项
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s'
LOG_FILENAME = 'system.log'
LOG_FILEMODE = 'a'
LOG_ENCODING = 'utf-8'

#------定义公共变量-------
users = []
user_find = []

#--------定义功能函数-------
#初始化log实例
def init_log():
    logger = logging.getLogger('log')
    logger.setLevel(LOG_LEVEL)
    fhandler = logging.FileHandler(LOG_FILENAME, encoding=LOG_ENCODING)
    fhandler.setLevel(LOG_LEVEL)
    fhandler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(fhandler)
    return logger

#装修器函数，将操作日志保存到日志
def log_info(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = init_log()
            if level == "debug":
                logger.debug(*args, **kwargs)
            elif level == "warn":
                logger.warn(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 成功时提示信息
@log_info(level="debug")
def success_info(info):
    print('\033[32m{}\033[0m'.format(info))

# 错误或警告时提示信息
@log_info(level="warn")
def warn_info(info):
    print('\033[31m{}\033[0m'.format(info))


#检查是否被锁定函数
def is_unlock():
    lock_time = 0

    try:
        fhandler = open(LOCK_FILE, 'at+')
        fhandler.seek(0)
        cxt = fhandler.read()
        fhandler.close()
        lock_time = float(cxt)
    except Exception as e:
        pass

    is_unlock = time.time() - lock_time > LOCK_INTERVAL

    if not is_unlock:
        warn_info('锁定用户尝试登录')

    return is_unlock

#判断登录函数
def login():
    is_login = False

    for i in range(MAX_LOGIN_COUNT):
        username = input('请输入用户名:')
        password = getpass.getpass('请输入密码:')

        if username == ADMIN_NAME and password == ADMIN_PASSWD:
            success_info("管理员登陆成功！")
            print('欢迎管理员登录系统')
            is_login = True
            break
        if MAX_LOGIN_COUNT -1 > i:
            warn_info("管理员输入的密码有误，重新输入。")
            print('请重新输入用户名,密码!')
        else:
            warn_info("管理员输入的密码错误三次，账号锁定。")
            print('登录失败，锁定用户')
    return is_login

#读取用户数据函数
def get_user():
    users = []
    try:
        fhandler = open(USER_FILE, 'at+')
        fhandler.seek(0)
        txt = fhandler.read()
        fhandler.close()
        users = json.loads(txt)

    except Exception as e:
        print('用户数据不存在')

    return users

#用户信息打印函数
def print_data(users):
    user_find = users
    max_page = 0

    user_find_count = len(user_find)
    if user_find_count == 0:
        print('无数据')
        return
    elif user_find_count <= PAGE_SIZE:
        print(TABLE_SPLIT_LINE)
        print(TABLE_TPL.format(**TABLE_TITLE))
        print(TABLE_SPLIT_LINE)
        for user in user_find:
            print(TABLE_TPL.format(**user))
        print(TABLE_SPLIT_LINE)
    else:
        max_page = user_find_count // PAGE_SIZE
        if user_find_count % PAGE_SIZE:
            max_page += 1

    if max_page > 1:
        while True:
            PAGE_NUB = input('共有{0}页，请输入要显示的页码1~{0}:'.format(max_page))
            if PAGE_NUB.isdigit() and int(PAGE_NUB) <= max_page:
                print(TABLE_SPLIT_LINE)
                print(TABLE_TPL.format(**TABLE_TITLE))
                print(TABLE_SPLIT_LINE)
                for user in user_find[(int(PAGE_NUB)-1)*PAGE_SIZE : int(PAGE_NUB)*PAGE_SIZE]:
                    print(TABLE_TPL.format(**user))
                print(TABLE_SPLIT_LINE)
            else:
                print('输入页码有误')
                break

#添加用户函数
def add_user(users):
    text = input('请数据用户信息(用户名，年龄， 电话号码， 地址)，信息使用空格分隔:')
    user = text.split()
    user_find = []
    users = users

    if len(user) != USER_INFO_NUM:
        warn_info("添加用户，输入用户信息格式错误！")
        print('用户数据格式不对，请重新输入！')
    else:
        name, age, tel, address = user
        has_error = False
        if not age.isdigit():
            warn_info("添加用户，输入年龄格式错误！")
            print('用户数据格式不对，请重新输入！')
            has_error = True

        if  not tel.isdigit():
            warn_info("添加用户，输入电话号码格式错误！")
            print('用户数据格式不对，请重新输入！')
            has_error = True

        if not has_error:
            try:
                uid = max([x.get('id') for x in users] + [0]) + 1
            except Exception as e:
                uid = 1
            users.append({'id': uid,'name': name, 'age': int(age),'tel': tel,'address': address})
            print('用户添加成功!')
            success_info("添加用户{0}信息成功。".format(name))
            user_find.append({'id': uid,'name': name, 'age': int(age),'tel': tel,'address': address})
            print_data(user_find)
            return users


#更改用户函数
def  modify_user(users):
    text = input('请输入用户ID:')
    users = users

    if text.isdigit():
        uid = int(text)
        for user in users:
            if user.get('id') == uid:
                text1 = input('请输入需要更新的用户信息(用户名，年龄， 电话号码， 地址)，信息使用空格分隔:')
                user =text1.split()

                if len(user) != USER_INFO_NUM:
                    warn_info("修改用户信息，输入用户信息格式错误！")
                    print('用户数据格式不对，请重新输入！')
                else:
                    name, age, tel, address = user
                    has_error = False
                    print(name, age, tel, address)

                if not age.isdigit():
                    warn_info("修改用户信息，输入年龄格式错误！")
                    print('用户数据格式不对，请重新输入！')
                    has_error = True

                if  not tel.isdigit():
                    warn_info("修改用户信息，输入电话号码格式错误！")
                    print('用户数据格式不对，请重新输入！')
                    has_error = True

                if not has_error:
                    for x in users:
                        if x.get('id') == uid:
                            x['name'], x['age'], x['tel'], x['address'] = user
                    success_info("修改用户{0}信息成功。".format(user[0]))
                    print('用户信息修改成功')
                    #打印修改用户的信息
                    for x in users:
                        if x.get('id') == uid:
                            user_find.append(x)

                    print_data(user_find)
                    return users
    else:
        warn_info("修改用户信息，用户信息不存在！")
        print('用户ID错误')

#查询用户信息函数
def query_user(users):
    text = input('请输入需要查询的字符:')
    users = users
    user_find = []
    max_page = 0

    for user in users:
        if user == '' or \
            user.get('name').find(text) != -1 or \
            user.get('tel').find(text) != -1 or \
            user.get('address').find(text) != -1:
            user_find.append(user)

    return user_find

#删除用户函数
def delete_user(users):
    text = input('请输入要删除的ID:')
    users = users

    if text.isdigit():
        uid = int(text)
        for user in users:
            if user.get('id') == uid:
                print(user)
                success_info("删除用户{0}信息成功。".format(user['name']))
                users.remove(user)
                print('用户删除成功')
                break
        else:
            warn_info("删除用户，用户ID不存在！")
            print('用户ID错误')
    else:
        warn_info("删除用户，用户ID输入错误！")
        print('用户ID错误')

    return users

#信息保存函数
def save_data(filename, users=[]):
    if filename == USER_FILE:
        fhandler = open(USER_FILE, 'w')
        fhandler.write(json.dumps(users))
        fhandler.close()
        success_info("保存用户信息成功！")
    elif filename == LOCK_FILE:
        fhandler = open(LOCK_FILE, 'w')
        fhandler.write(str(time.time()))
        fhandler.close()
        success_info("保存管理员锁定信息成功！")

#系统操作函数
def operate(users):
     while True:
        op = input('请输入操作(list/add/modify/query/delete/save/exit):').strip()
        if op == 'list':
            user_find = users
            print_data(user_find)
        elif op == 'add':
            users = add_user(users)
        elif op == 'modify':
            users = modify_user(users)
        elif op == 'query':
            user_find = query_user(users)
            print_data(user_find)
        elif op == 'delete':
            users = delete_user(users)
        elif op == 'save':
           save_data(USER_FILE, users)
           print('已成功保存用户数据')
        elif op == 'exit':
            save_data(USER_FILE, users)
            print('成功退出，已自动保存数据')
            break
        else:
            warn_info("输入操作指令错误！")
            print('输入操作指令有误，请重新输入')

#系统主程序函数
def main():
    #1、检查是否锁定
    if is_unlock():
        #2、登录
        if login():
            #3、加载用户数据
            users = get_user()
            #4、进行操作
            operate(users)
        else:
            save_data(LOCK_FILE)

#运行主程序函数
if __name__ == '__main__':
    main()
