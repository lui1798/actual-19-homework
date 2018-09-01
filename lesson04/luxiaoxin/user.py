#encoding: utf-8
#导入模块
import time
import getpass
import json


#定义公用常量
LOCK_FILE = 'lock'
LOCK_INTERVAL = 30

ADMIN_NAME = 'admin'
ADMIN_PASSWD = '51@reboot'
MAX_LOGIN_COUNT = 3

USER_FILE = 'user.json'
USER_INFO_NUM = 4

TABLE_TPL = '|{id:^10}|{name:^10}|{age:^5}|{tel:^15}|{address:^20}|'
TABLE_TITLE = {"id" : "id", "name" : "name", "age" : "age", "tel" : "tel" , "address": "address"}
TITLE = TABLE_TPL.format(**TABLE_TITLE)
TABLE_SPLIT_LINE = '-' * (len(TITLE))
PAGE_SIZE = 2
#定义公共变量
users = []
user_find = []

#定义函数
#1、检查是否被锁定函数
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

    return time.time() - lock_time > LOCK_INTERVAL

#2、登录函数
def login():
    is_login = False

    for i in range(MAX_LOGIN_COUNT):
        username = input('请输入用户名:')
        password = getpass.getpass('请输入密码:')

        if username == ADMIN_NAME and password == ADMIN_PASSWD:
            is_login = True
            break
        if MAX_LOGIN_COUNT -1 > i:
                print('请重新输入用户名,密码!')
        else:
                print('登录失败，锁定用户')
    return is_login

#3、读取用户数据函数
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

#4、添加用户函数
def add_user(users):
    text = input('请数据用户信息(用户名，年龄， 电话号码， 地址)，信息使用空格分隔:')
    user = text.split()
    user_find = []
    users = users

    if len(user) != USER_INFO_NUM:
        print('用户数据格式不对，请重新输入！')
    else:
        name, age, tel, address = user
        has_error = False
        if not age.isdigit():
            print('年龄格式不对，请重新输入！')
            has_error = True

        if  not tel.isdigit():
            print('电话号码格式不对，请重新输入！')
            has_error = True

        if not has_error:
            try:
                uid = max([x.get('id') for x in users] + [0]) + 1
            except Exception as e:
                uid = 1
            users.append({'id': uid,'name': name, 'age': int(age),'tel': tel,'address': address})
            print('用户添加成功')
            user_find.append({'id': uid,'name': name, 'age': int(age),'tel': tel,'address': address})
            print_data(user_find)
            return users


#5、更改用户函数
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
                    print('用户数据格式不对，请重新输入！')
                else:
                    name, age, tel, address = user
                    has_error = False
                    print(name, age, tel, address)

                if not age.isdigit():
                    print('年龄格式不对，请重新输入！')
                    has_error = True

                if  not tel.isdigit():
                    print('电话号码格式不对，请重新输入！')
                    has_error = True

                if not has_error:
                    for x in users:
                        if x.get('id') == uid:
                            x['name'], x['age'], x['tel'], x['address'] = user
                    print('用户信息修改成功')
                    #打印修改用户的信息
                    for x in users:
                        if x.get('id') == uid:
                            user_find.append(x)

                    print_data(user_find)
                    return users
    else:
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
                users.remove(user)
                print('用户删除成功')
                break
        else:
            print('用户ID不存在')
    else:
        print('用户ID错误')

    return users

#信息保存函数
def save_data(filename, users=[]):
    if filename == USER_FILE:
        fhandler = open(USER_FILE, 'w')
        fhandler.write(json.dumps(users))
        fhandler.close()
    elif filename == LOCK_FILE:
        fhandler = open(LOCK_FILE, 'w')
        fhandler.write(str(time.time()))
        fhandler.close()

#系统主程序函数
def main():
    #1、检查是否锁定
    if is_unlock():
        #2、登录
        if login():
            #3、加载用户数据
            users = get_user()
            #4、进行操作
            while True:
                op = input('请输入操作(list/add/modify/query/delete/save/exit):')
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
                    print('输入操作指令有误，请重新输入')

        else:
            save_data(LOCK_FILE)

main()
