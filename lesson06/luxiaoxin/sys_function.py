#encoding: utf-8
#-----导入内置模块--------
import time
import json
#-----导入开源模块--------
import getpass
import requests
#-----导入自定义模块--------
import db
import utils


#-----定义公用常量-------
#管理员登录锁定时长30s
LOCK_INTERVAL = 30
#系统管理员用户名和密码，以及Github登录验证的token
ADMIN_NAME = 'admin'
ADMIN_PASSWD = '51@reboot'
TOKEN = "c689caf486079b574fef94a3802591db48cf6de5"
HEADERS = {'Authorization': 'token ' + TOKEN}
HEADERS_ERROR = {'Authorization': 'token '}
#最大登录次数
MAX_LOGIN_COUNT = 3
#用户信息
USER_TITLE = ('id','name','age','tel','address')
#用户信息存储文件
#USER_FILE = 'user.json'
#导出Excel文件名
OUTPUT_FILE = 'mgt1.xls'
#用户信息长度
USER_INFO_NUM = 4
#打印用户信息格式
TABLE_TPL = '|{id:^10}|{name:^10}|{age:^5}|{tel:^15}|{address:^20}|'
TABLE_TITLE = {"id" : "id", "name" : "name", "age" : "age", "tel" : "tel" , "address": "address"}
TITLE = TABLE_TPL.format(**TABLE_TITLE)
TABLE_SPLIT_LINE = '-' * (len(TITLE))
PAGE_SIZE = 2

#------定义公共变量-------
users = []
user_find = []

#--------定义系统功能函数-------
#检查是否被锁定函数
def is_unlock():
    lock_time = 0
    LOCK_FILE = utils.ReadConfigFile('conf.ini', 'LOG', 'LOGFILE')

    try:
        cxt = utils.ReadFile(LOCK_FILE)
        lock_time = float(cxt)
    except Exception as e:
        pass

    is_unlock = time.time() - lock_time > LOCK_INTERVAL

    if not is_unlock:
        utils.warn_info('锁定用户尝试登录')

    return is_unlock


#锁定管理员账号
def lock_admin():
    lock_init_time = time.time()
    LOCK_FILE = utils.ReadConfigFile('conf.ini', 'LOG', 'LOGFILE')
    utils.WriteFile(LOCK_FILE,lock_init_time)

#判断登录函数
def login():
    is_login = False

    for i in range(MAX_LOGIN_COUNT):
        username = input('请输入用户名:')
        password = getpass.getpass('请输入密码:')

        if username == ADMIN_NAME and password == ADMIN_PASSWD:
            req = requests.get('https://api.github.com/user', headers=HEADERS)
        else:
            req = requests.get('https://api.github.com/user', headers=HEADERS_ERROR)

        if req.ok:
            utils.success_info("管理员登陆成功！")
            print('欢迎管理员登录系统')
            is_login = True
            break
        if MAX_LOGIN_COUNT -1 > i:
            utils.warn_info("管理员用户名或密码有误，错误信息{0}{1}".format(req.status_code, req.reason))
            print('请重新输入用户名,密码!')
        else:
            utils.warn_info("管理员输入的密码错误三次，账号锁定。")
            print('登录失败，锁定用户')
    return is_login

#读取用户数据函数
def get_user():
    user = {}
    users = []
    cnt, result = db.Select()
    if cnt == 0:
        print('用户数据不存在')
    else:
        for user_tuple in result:
            user_z = zip(USER_TITLE, user_tuple)
            for x in user_z:
                user[x[0]] = x[1]
            user_l = user.copy()
            users.append(user_l)
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
    users = users
    user_find = []

    text = input('请数据用户信息(用户名，年龄， 电话号码， 地址)，信息使用空格分隔:')
    user = text.split()

    if len(user) != USER_INFO_NUM:
        utils.warn_info("添加用户，输入用户信息格式错误！")
        print('用户数据格式不对，请重新输入！')
    else:
        name, age, tel, address = user
        has_error = False
        if not age.isdigit():
            utils.warn_info("添加用户，输入年龄格式错误！")
            print('用户数据格式不对，请重新输入！')
            has_error = True

        if  not tel.isdigit():
            utils.warn_info("添加用户，输入电话号码格式错误！")
            print('用户数据格式不对，请重新输入！')
            has_error = True

        if not has_error:
            try:
                uid = max([x.get('id') for x in users] + [0]) + 1
            except Exception as e:
                uid = 1
            cnt, result = db.Insert(uid, name, int(age), tel, address)
            #users.append({'id': uid,'name': name, 'age': int(age),'tel': tel,'address': address})
            if cnt != 0:
                print('用户添加成功!')
                utils.success_info("添加用户{0}信息成功。".format(name))
                user_find.append({'id': uid,'name': name, 'age': int(age),'tel': tel,'address': address})
                print_data(user_find)
            else:
                print(result)
            #return users


#更改用户函数
def  modify_user(users):
    users = users
    user_find = []
    has_error = True

    text = input('请输入用户ID:')
    users = get_user()


    if text.isdigit():
        uid = int(text)
        for user in users:
            if user.get('id') == uid:
                text1 = input('请输入需要更新的用户信息(用户名，年龄， 电话号码， 地址)，信息使用空格分隔:')
                user =text1.split()

                if len(user) != USER_INFO_NUM:
                    utils.warn_info("修改用户信息，输入用户信息格式错误！")
                    print('用户数据格式不对，请重新输入！')
                else:
                    name, age, tel, address = user
                    has_error = False

                    if not age.isdigit():
                        utils.warn_info("修改用户信息，输入年龄格式错误！")
                        print('用户数据格式不对，请重新输入！')
                        has_error = True

                    if  not tel.isdigit():
                        utils.warn_info("修改用户信息，输入电话号码格式错误！")
                        print('用户数据格式不对，请重新输入！')
                        has_error = True

                if not has_error:
                    for x in users:
                        if x.get('id') == uid:
                            x['name'], x['age'], x['tel'], x['address'] = user
                            cnt, result = db.Modify(x['name'], x['age'], x['tel'], x['address'], uid)
                            if cnt != 0:
                                utils.success_info("修改用户{0}信息成功。".format(user[0]))
                                print('用户信息修改成功')
                                #打印修改用户的信息
                                user_find.append(x)
                                print_data(user_find)
                            else:
                                print(result)
    else:
        utils.warn_info("修改用户信息，用户信息不存在！")
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

    print_data(user_find)


#删除用户函数
def delete_user():
    text = input('请输入要删除的ID:')
    #users = users

    if text.isdigit():
        uid = int(text)
        cnt,result = db.Delete(uid)

        if cnt != 0:
            utils.success_info("删除用户ID为{0}的用户信息成功。".format(uid))
            print('用户删除成功')
        else:
            print(result)
            utils.warn_info("删除用户，用户ID不存在！")
            print('用户ID错误')
        '''
        for user in users:
            if user.get('id') == uid:
                db.Delete(uid)
                utils.success_info("删除用户{0}信息成功。".format(user['name']))
                #users.remove(user)
                print('用户删除成功')
                break'''

    else:
        utils.warn_info("删除用户，用户ID输入错误！")
        print('用户ID错误')


#信息保存函数
'''
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
'''
#系统操作函数
def operate(users):
     while True:
        op = input('请输入操作(list/add/modify/query/delete/output/exit):').strip()
        users = get_user()
        if op == 'list':
            user_find = users
            print_data(user_find)
        elif op == 'add':
            add_user(users)
        elif op == 'modify':
            modify_user(users)
        elif op == 'query':
            query_user(users)
        elif op == 'delete':
            delete_user()
        elif op == 'output':
            utils.WriteExcel(OUTPUT_FILE, users)
            print('用户数据导出完毕！')
        elif op == 'exit':
            print('成功退出，已自动保存数据')
            break
        else:
            utils.warn_info("输入操作指令错误！")
            print('输入操作指令有误，请重新输入')

