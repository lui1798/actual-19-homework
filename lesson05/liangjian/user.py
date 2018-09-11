#encoding: utf-8
#导入模块
import time
import getpass
import json
import math
import logging





#定义常量
LOCK_FILE = "lock"
LOCK_DURATION = 30

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "123456"

MAX_LOGIN_TIMES = 3
USER_FILE = "user.json"

USER_INFO_NUM = 4

TABLE_TPL = '{id:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
TABLE_SPLIT_LINE = 64
TABLE_TITLE = {"id" : "id", "name" : "name", "age" : "age", "tel" : "tel" , "address": "address"}

PAGE_SIZE = 2

#日志logging
logging.basicConfig(
    filename = "admin.log",
    filemode = 'a',
    format = "[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s",
    level = logging.DEBUG
)




def is_unlock():
    lock_time = 0
    try:
        fhandler = open(LOCK_FILE, "r")
        cxt = fhandler.read()
        fhandler.close()
        lock_time = float(cxt)
    except Exception as e:
        pass

    return time.time() - lock_time > LOCK_DURATION


def login():
    is_login = False

    for i in range(MAX_LOGIN_TIMES):
        username = input("请输入用户名:")
        password = getpass.getpass("请输入密码:")

        if ADMIN_USERNAME == username and ADMIN_PASSWORD == password:
            is_login = True
            break

        # 注意最会一次登陆
        if MAX_LOGIN_TIMES - 1 == i:
            print("登陆失败, 锁定用户")
        else:
            print("登陆失败, 请重新输入用户名, 密码")

    return is_login


def get_users():
    users = []
    try:
        fhandler = open(USER_FILE, "r")
        cxt = fhandler.read()
        fhandler.close()
        users = json.loads(cxt)
    except Exception as e:
        pass
    return users


def add_user(users):
    text = input("请依次输入用户信息(用户名, 年龄, 电话号码, 地址), 信息使用空格分割:")
    user = text.split()
    if len(user) != USER_INFO_NUM:
        print("输入数据不正确")
    else:
        name, age, tel, address = user
        has_error = False
        if not age.isdigit():
            print("年龄输入有问题")
            has_error = True

        if not tel.isdigit():
            print("电话号码有问题")
            has_error = True

        if not has_error:
            #生成id
            uid = max([x.get("id") for x in users] + [0]) + 1
            users.append({
                "id" : uid,
                "name" : name,
                "age" : int(age),
                "tel" : tel,
                "address" : address
            })
            print("添加用户成功")
            logging.debug(' add user success!')
    return users


def del_user(users):
    text = input("请输入要删除的ID: ")
    if text.isdigit():
        uid = int(text)
        for user in users:
            if uid == user.get("id"):
                users.remove(user)
                print("删除用户成功")
                logging.debug(' delet user success!')
                break

            else:
                print("输入ID错误")
                logging.debug('vaild id')
    else:
        print("输入ID错误")
        logging.debug('vaild id')
    return users


def modify(users):
    text = input("请输入修改用户ID:")
    is_exists = False
    uid = 0
    if text.isdigit():
        uid = int(text)
        for user in users:
            if uid == user.get("id"):
                print("更新用户信息:" + json.dumps(user))
                is_exists = True
                break

    if is_exists:
        text = input("请依次输入用户信息(用户名, 年龄, 电话号码, 地址), 信息使用空格分割:")
        user = text.split()
        if len(user) != USER_INFO_NUM:
            print("输入数据不正确")
        else:
            name, age, tel, address = user
            has_error = False
            if not age.isdigit():
                has_error = True
                print("输入的年龄不正确")

            if not tel.isdigit():
                has_error = True
                print("输入的电话不正确")

            if not has_error:
                for user in users:
                    if uid == user.get("id"):
                        #  直接更新 user
                        user["name"] = name
                        user["age"] = age
                        user["tel"] = tel
                        user["address"] = address
                        print("更新成功")
                        logging.debug('update success')
                        break
    else:
        print("输出ID错误")
        logging.debug('vaild id')

    return users


def save_users(users):
    fhandler = open(USER_FILE, "w")
    fhandler.write(json.dumps(users))
    fhandler.close()
    print("存储用户信息成功")


def print_users(users):
    print('-' * TABLE_SPLIT_LINE)
    print(TABLE_TPL.format(**TABLE_TITLE)) # TABLE_TPL.format(id="id", name="name", age="age", tel="tel", address="address")
    print('-' * TABLE_SPLIT_LINE)
    for user in users:
        print(TABLE_TPL.format(**user))
    print('-' * TABLE_SPLIT_LINE)


def query_user(users):
    users_find = []
    text = input("请输入查询的字符串:")
    for user in users:
        if text == '' or user.get("name").find(text) != -1 or \
            user.get("tel").find(text) != -1 or \
            user.get("address").find(text) != -1:
            users_find.append(user)

    users_find_count = len(users_find)
    if users_find_count == 0:
        print("无数据")
    elif users_find_count <= PAGE_SIZE:
       print_users(users_find)
    else:
        max_page = math.ceil(users_find_count / PAGE_SIZE)
        while True:
            text_page_num = input("共有{0}页, 请输入查询页码(1 ~ {0}): ".format(max_page))
            if text_page_num.isdigit() and int(text_page_num) <= max_page:
                page_num = int(text_page_num)
                print_users(users_find[(page_num - 1) * PAGE_SIZE : page_num * PAGE_SIZE])
            else:
                print("输入页码错误")
                break


def operate(users):
    while True:
        op = input("请输入操作(add,modify,delete,query,save,exit):")
        if op == "add":
            users = add_user(users)
        elif op == "modify":
            users = modify(users)
        elif op == "delete":
            users = del_user(users)
        elif op == "query":
            query_user(users)
        elif op == "save":
            save_users(users)
        elif op == "exit":
            save_users(users)
            break
        else:
            print("输入参数错误")


def lock_user():
    fhandler = open(LOCK_FILE, "w")
    fhandler.write(str(time.time()))
    fhandler.close()


def main():
    #1. 判断是否锁定
    if not is_unlock():
        print("用户被锁定, 请稍后再试")
        return
    #2. 登陆
    if login():
        #3. 登陆成功
        #3.1 加载用户数据
        users = get_users()
        #3.2 操作
        operate(users)
    else:
        #4. 登陆失败, 锁定用户
        lock_user()



main()
