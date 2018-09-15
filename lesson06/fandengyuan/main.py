#Author：fandy
'''
1. 支持Github(Token)登录认证方式；
2. 支持配置文件管理方式；
3. 支持导出Excel(仅支持导出功能即可)；
4. 存储方式改成MySQL(实现增删改查)；
'''
#导入模块
import json
import time
import math
import sys
import requests
import xlwt
import configparser
import pymysql

#常量
CONF_FILE = 'conf.ini'
SECTION = 'LOCKS'
LOCK_FILE = 'lock'
lock_time = 20

Max_Retry = 3
USER_INFO_NUM = 4
PAGE_SIZE = 2

#公共变量
user = []

#配置文件
def ReadConfig(CONF_FILE,SECTION,LOCK_FILE):
    config = configparser.ConfigParser()
    config.read(CONF_FILE)
    if not config.sections():
        conf_flag = False
    if LOCK_FILE in config[SECTION]:
        conf_flag = True
    else:
        conf_flag = False

    return conf_flag

#判断用户是否已锁定
def Is_Unlock():
    lock_start_time = 0
    while ReadConfig(CONF_FILE,SECTION,LOCK_FILE):
        fhandler = open(LOCK_FILE,'r')
        cxt = fhandler.read()
        fhandler.close()
        lock_start_time = float(cxt)
    else:
        is_unlock = False
    is_unlock = time.time() - lock_start_time > lock_time

    return is_unlock

#定义登录函数
def Is_Login():
    if Is_Unlock():
        is_login = False
        for i in range(Max_Retry):
            TOKEN = "e8a3c99145c2debb147f56f3779bafe35dced66b"
            headers = {'Authorization': 'token' + TOKEN}
            req = requests.get('https://api.github.com/user', headers=headers)
            if "401" in str(req):
                is_login = True
                break
            if Max_Retry - 1 == i:
                print('登录失败，账户锁定')
            else:
                print('登录失败，请重新输入,剩余尝试次数{}'.format(Max_Retry - 1))
            is_login = False

    return is_login

#获取用户列表
def Get_Users():
    if Is_Login():
        userinfo = []
        conn = pymysql.connect(host='172.25.8.62', user='noc618', password='noc8*8', database='MyDB', port=3306)
        cursor = conn.cursor()
        find_sql = '''select * from userlist;'''
        cursor.execute(find_sql)
        for x in cursor.fetchall():
            userinfo.append(x)
        cursor.close()
        conn.close()

    return userinfo

#增
def Add(userinfo):
    text = input('请依次输入用户信息（用户名，年龄，电话，地址），信息使用空格分隔:')
    user = text.split()
    if len(user) != USER_INFO_NUM:
        print('输入数据不正确')
    else:
        name, age, tel, address = user
        has_error = False
        if not age.isdigit():
            print('年龄输入格式错误')
            has_error = True
        if not tel.isdigit():
            print('电话格式输入错误')
            has_error = True
        if not has_error:
            uid = max([x.get('id') for x in userinfo] + [0]) + 1
            userinfo.append({"id": uid, "name": name, "age": int(age), "tel": int(tel), "address": address})
            conn = pymysql.connect(host='172.25.8.62', user='noc618', password='noc8*8', database='MyDB', port=3306)
            cursor = conn.cursor()
            add_sql = '''insert into userlist(id,name,age,tel,address) values(%s,%s,%s,%s,%s);'''.format(id,name,age,tel,address)
            cursor.execute(add_sql)
            conn.commit()
            cursor.close()
            conn.close()
            print('用户添加成功')

        return userinfo
#删
def Delete(userinfo):
    text = input('请输入要删除的ID:')
    if text.isdigit():
        uid = int(text)
        for user in userinfo:
            if uid == user.get("id"):
                userinfo.remove(user)
                conn = pymysql.connect(host='172.25.8.62', user='noc618', password='noc8*8', database='MyDB', port=3306)
                cursor = conn.cursor()
                delete_sql = '''delete from userlist where id=%s;'''.format(uid)
                cursor.execute(delete_sql)
                conn.commit()
                cursor.close()
                conn.close()
                print('删除成功')
                break
        else:
            print('查无此人')
    else:
        print('输入格式错误')

    return userinfo

#改
def Modify(userinfo):
    text = input('请输入要更新的用户ID:')
    is_exits = False
    if text.isdigit():
        uid = int(text)
        for user in userinfo:
            if uid == user.get("id"):
                print("更新信息:" + json.dumps(user))
                is_exits = True
                break
    if is_exits:
        text = input('请输入要更新的用户信息(用户名 年龄 电话 地址):')
        up_user = text.split()
        if len(up_user) != USER_INFO_NUM:
            print('输入数据不正确')
        else:
            name, age, tel, address = up_user
            has_error = False
            if not age.isdigit():
                print('年龄输入格式错误')
                has_error = True
            if not tel.isdigit():
                print('电话格式输入错误')
                has_error = True
            if not has_error:
                for user in userinfo:
                    if uid == user.get("id"):
                        user["name"] = name
                        user["age"] = age
                        user["tel"] = tel
                        user["address"] = address
                        conn = pymysql.connect(host='172.25.8.62', user='noc618', password='noc8*8', database='MyDB',port=3306)
                        cursor = conn.cursor()
                        update_sql = '''update userlist set name=%s,age=%s,tel=%s,address=%s where id=%s;'''.format(name,age,tel,address,uid)
                        cursor.execute(update_sql)
                        conn.commit()
                        cursor.close()
                        conn.close()
                        print('更新成功')
                        break
    else:
        print('输入ID错误')

    return userinfo

#查
def Query(userinfo):
    TABLE_TPL = '{id:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
    TABLE_TITLE = {'id': 'id', 'name': 'name', 'age': 'age', 'tel': 'tel', 'address': 'address'}
    text = input('请输入查询的字符串:')
    users_find = []
    for user in userinfo:
        if text == '' or user.get("name").find(text) != -1 or \
                user.get("tel").find(text) != -1 or \
                user.get("address").find(text) != -1:
            users_find.append(user)
    users_find_count = len(users_find)
    if users_find_count == 0:
        print("无数据")
    elif users_find_count <= PAGE_SIZE:
        print(TABLE_TPL.format(**TABLE_TITLE))
        for user in users_find:
            print(TABLE_TPL.format(**user))
    else:
        max_page = math.ceil(users_find_count / PAGE_SIZE)
        while True:
            text_page_num = input("共有{0}页，请输入要查询的页码（1—{0}）：".format(max_page))
            if text_page_num.isdigit() and int(text_page_num) <= max_page:
                page_num = int(text_page_num)
                print(TABLE_TPL.format(**TABLE_TITLE))
                print('-' * 65)
                for user in users_find[(page_num - 1) * PAGE_SIZE: page_num * PAGE_SIZE]:
                    print(TABLE_TPL.format(**user))
            elif text_page_num == "quit":
                print('退出query')
                break
            else:
                print('页码错误')
                break

    return userinfo

#保存
def Save(userinfo):
    fhandler = open(userinfo, 'w')
    fhandler.write(json.dumps(userinfo))
    fhandler.close()
    print('正在保存所做修改')
    for i in range(20):
        sys.stdout.write("-")
        sys.stdout.flush()
        time.sleep(0.1)
    print('\n存储成功')

    return userinfo

#退出
def Exit(userinfo):
    fhandler = open(userinfo, 'w')
    fhandler.write(json.dumps(userinfo))
    fhandler.close()
    print('正在保存所做修改')
    for i in range(20):
        sys.stdout.write("-")
        sys.stdout.flush()
        time.sleep(0.1)
    print('\n退出程序，已自动存储所做修改')

    return userinfo

#定义执行函数
def op(userinfo):
    while True:
        op = input('请输入要执行的操作(1.增加add，2.删除delete，3.修改modify，4.查询query，5.保存save，6.退出exit):')
        if op == 'add' or op == '1':
            userinfo = Add(userinfo)
        elif op == 'delete' or op == '2':
            userinfo = Delete(userinfo)
        elif op == 'modify' or op == '3':
            userinfo = Modify(userinfo)
        elif op == 'query' or op == '4':
            userinfo = Query(userinfo)
        elif op == 'save' or op == '5':
            userinfo = Save(userinfo)
        elif op == 'exit' or op == '6':
            userinfo = Exit(userinfo)
            break
        else:
            print('输入错误，无此选项')

#锁定账户
def Lock_user():
    if not Is_Login():
        fhandler = open(LOCK_FILE,'w')
        fhandler.write(str(time.time()))
        fhandler.close()

#导出表格
def Excel(userinfo):
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')
    fd = open(userinfo,'r')
    result = fd.read()
    op = json.loads(result)
    fd.close()
    title = []
    for k in op[0]:
        title.append(k)
    for i,item in enumerate(title):
        sheet.write(0,i,item)
        n = 0
        for user_dic in op:
            n = n + 1
            sheet.write(n,i,user_dic.get(item))
    book.save('user.xls')

def main(*args):
    if Is_Login():
        print('登陆成功')
        userinfo = Get_Users()
        op(userinfo)
        Excel(userinfo)
    else:
        Lock_user()

if __name__ == '__main__':
    main()
