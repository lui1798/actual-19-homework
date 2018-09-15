
import json
import math
import time
import requests
import pymysql
import configparser


LOCK_FILE = 'lock'
USERS_FILE = 'user.json'

USERNAME = 'admin'
PASSWORD = 'admin'

MAX_LOGIN_TIMES = 3
MAX_LOCK_TIME = 30
USER_LENGTH = 4
PAGE_SIZE = 3

TABLE_TEMPLATE = '{num:>5}|{name:>8}|{age:>5}|{tel:>15}|{city:>10}'
TABLE_LINE = 47
TABLE_TITLE = {'num': 'number', 'name': 'name', 'age': 'age', 'tel': 'telephone', 'city': 'city'}

users = []


def lock():
    is_lock = False
    try:
        fd = open('lock')
        cxt = float(fd.read())
        fd.close()
        is_lock = time.time() - cxt < MAX_LOCK_TIME
    except Exception as e:
        pass
    return is_lock


def login_yz():
    response = requests.get('https://github.com/login')
    response.encoding = 'utf-8'
    result = response.text
    return response


def login():
    is_login = False
    print('''
           ======================================
           
                 欢迎进入员工管理系统，请登录
                 
           ======================================
           ''')
    for i in range(MAX_LOGIN_TIMES):
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if username == USERNAME and password == PASSWORD:
            is_login = True
            break
        if MAX_LOGIN_TIMES - i == 1:
            fd = open('file', 'w')
            fd.write(str(time.time()))
            fd.close()
            print('错误次数过多，账户已锁定，请30秒之后再试。')
        else:
            print('用户名或密码错误，请重新输入')
    return is_login


# def get_users():
#     users = []
#     try:
#         fhander = open(USERS_FILE, 'r')
#         users = json.loads(fhander.read())
#         fhander.close()
#     except Exception as e:
#         pass
#     return users

def get_users():
    users = []
    conn = pymysql.Connect(host='127.0.0.1', user='root', password='', database='lesson6', port=3306)
    sql = 'select * from user_info;'
    cursor_1 = conn.cursor()
    cursor_1.execute(sql)
    for user in cursor_1.fetchall():
        users.append(user)
    cursor_1.close()
    conn.close()
    return users


def get_config(filename, section, key):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return '空的配置文件', False
    if key in config[section]:
        return config[section][key], True
    else:
        return '', False


def add_user(users):
    adduser = input('请输入要增加的用户信息(姓名，年龄，电话，城市)并用空格键分隔开：')
    if len(adduser.split()) == 4:
        name, age, tel, city = adduser.split()
        if not age.isdigit():
            print('年龄输入有误')
        if not tel.isdigit() or len(tel) != 11:
            print('电话输入有误')
        else:
            #get_users()
            #num = max([user['num'] for user in users]+[0]) + 1
            num = len(users)
            #users.append(
            #{'num': num, 'name': name, 'age': age, 'tel': tel, 'city': city}
            #    )
            conn = pymysql.Connect(host='127.0.0.1', user='root', password='', database='zhangjinqi', port=3306)
            add_sql = '''
                insert into user_info(num,name,age,tel,city) values("%s","%s","%s","%s","%s");
                ''' % (num, name, age, tel, city)
            cursor = conn.cursor()
            cursor.execute(add_sql)
            conn.commit()
            cursor.close()
            conn.close()
            
            print('已成功添加用户信息')
            #save_(users)
            print(users)
    else:
        print('用户信息输入有误，请重新输入')
    return users


def del_user(users):
    del_num = input('请输入要删除的用户序号')
    if del_num.isdigit():
        if int(del_num) <= max([user['num'] for user in users]):
            #users.remove(users[int(del_num)])
            conn = pymysql.Connect(
                host='127.0.0.1', user='root', password='', database='user_info', port=3306
            )
            cursor = conn.cursor()
            del_sql = "delete from user_info where uid='%s'" % (int(del_num))
            cursor.excute(del_sql)
            conn.commit()
            cursor.close()
            conn.close()
            print('已成功删除该用户')
            print(users[int(del_num) - 1])
        else:
            print('用户不存在')
    else:
        print('序号输入有误')
    #return users


def update_user(users):
    update_num = input('请输入想要更新的用户序号')
    if update_num.isdigit():
        if int(update_num) <= max([user['num'] for user in users]):
            print('users[int(update_num)]')
            update_user = input('请依次输入更新后的用户信息，并按空格键分隔开：')
            if len(update_user.split()) == 4:
                name, age, tel, city = update_user.split()
                if not age.isdigit():
                    print('年龄输入有误')
                if tel.isdigit() is False or len(tel) != 11:
                    print('电话输入有误')
                else:
                    num = update_num
                    #users[num].update(
                    #    {'num': num, 'name': name, 'age': age, 'tel': tel, 'city': city}
                    #)
                    conn = pymysql.Connect(
                        host='127.0.0.1', user='root', password='', database='lesson6', port=3306
                    )
                    cursor = conn.cursor()
                    update_sql = "update user_info set num=%s, name=%s, age=%s, tel=%s, city=%s where num=%s" % (num, name, age, tel, city, num)
                    cursor.excute(update_sql)
                    conn.commit()
                    cursor.close()
                    conn.close()

                    print('已成功更新用户信息')
            else:
                print('您输入的用户信息有误')
        else:
            print('没有此序号的用户')
    else:
        print('输入有误')
    #return users


def list_user(users):
    find_users = []
    find_text = input('请输入要查询的内容：')
    for user in users:

        if find_text == '' \
        or user.get('name').find(find_text) != -1 \
        or user.get('age').find(find_text) != -1 \
        or user.get('tel').find(find_text) != -1 \
        or user.get('city').find(find_text) != -1:
            find_users.append(user)
    if len(find_users) <= PAGE_SIZE:
        print('-'*TABLE_LINE)
        print(TABLE_TEMPLATE.format(**TABLE_TITLE))
        print('-'*TABLE_LINE)
        for user in find_users:
            print(TABLE_TEMPLATE.format(**user))
        print('-' * TABLE_LINE)
    else:
        while True:
            find_page = input('共查询到{0}页信息，请输入1-{0}页数查询：'.format(math.ceil(len(find_users)/PAGE_SIZE)))
            if find_page.isdigit() is True and int(find_page) <= len(find_users):
                print('-'*TABLE_LINE)
                print(TABLE_TEMPLATE.format(**TABLE_TITLE))
                print('-' * TABLE_LINE)
                for user in find_users[PAGE_SIZE*(int(find_page)-1):PAGE_SIZE*(int(find_page))]:
                    print(TABLE_TEMPLATE.format(**user))
                print('-' * TABLE_LINE)
            else:
                print('输入的页码有误，请重新输入')


# def save_(users):
#     fhander = open('user.json', 'w')
#     fhander.write(json.dumps(users))
#     fhander.close()
#     print('保存成功')


def exit_(users):
    # fhander = open('USER_FILE', 'w')
    # fhander.write(json.dumps(users))
    # fhander.close()
    #print('已保存数据并推出')
    print('''
        ======================================

                        再见
                     good-bye!

        ======================================
               ''')
    exit()


def operate(users):
    while True:
        op = input("请输入操作(add,delete,update,query,save,exit):")
        if op == "add":
            add_user(get_users())
        elif op == "delete":
            del_user(get_users())
        elif op == "update":
            update_user(get_users())
        elif op == "query":
            list_user(get_users())
        #elif op == "save":
            #save_(users)
        elif op == "exit":
            exit_(users)
            break
        else:
            print("输入参数错误")


def main():
    if lock():
        print('用户已锁定，请30s后再登陆')
    else:
        if login():
            operate(users)

main()













