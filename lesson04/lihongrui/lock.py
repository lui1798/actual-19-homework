# 导入模块
import time
import getpass
import json
import math

# 定义常量
LOCK_FILE = "lock"
LOCK_FW = 30
Admin_User = 'admin'
Admin_Pass = "123"

Max_denglu = 3
User_DB = "user.json"

USER_INFO_NUM = 4

TAB_TPL = '{id:>10} |{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
TAB_LINE = 64
BIAOTOU = {"id": "id", "name": "name", "age": "age", "tel": "tel", "address": "address"}

PAGE_SIZE = 2


def is_unlock():
    lock_time = 0
    try:
        f = open(LOCK_FILE, "r")  # 以读方式打开锁文件
        cxt = f.read()
        f.close()
        lock_time = float(cxt)
    except Exception as e:
        pass
    return time.time() - lock_time > LOCK_FW


def login():
    is_login = False

    for i in range(Max_denglu):
        username = input("输入用户名")
        password = getpass.getpass("输入密码")

        if Admin_User == username and Admin_Pass == password:
            is_login = True
            break

        if Max_denglu - 1 == i:
            print("用户锁定")
        else:
            print("请重新登陆")
    return is_login


def get_users():
    users=[]
    try:
        f = open(User_DB, "r")
        cxt = f.read()
        f.close()
        users=json.load(cxt)
        lock_time = float(cxt)
    except Exception as e:
        pass
    return users


def add_user(users):
    text = input("请输入用户名, 年龄, 电话号码, 地址 用空格分隔")
    user = text.split()
    if len(user) != USER_INFO_NUM:  # 如果用户输入的内容不是4个
        print("输入的格式不对或内容不全")
    else:
        name, age, tel, address = user
        has_error = False
        if not age.isdigit():
            print("年龄不是数字类型")
            has_error = True
        if not tel.isdigit():
            print("电话号码不是数字类型")
            has_error = True
        if not has_error:
            # 生成id
            uid = max([x.get("id") for x in users] + [0]) + 1
            user.append({
                "id": uid,
                "name": name,
                "age": int(age),
                "tel": tel,
                "address": address
            })
            print("添加用户成功")
    return users


def save_users(users):
    f = open(User_DB, 'w')
    f.write(json.dumps(users))
    f.close()
    print("保存用户信息成功")


def print_users(users):
    print('_' * TAB_LINE)
    print(TAB_TPL.format(**BIAOTOU))
    print('_' * TAB_LINE)
    for user in users:
        print(TAB_TPL.format(**user))
    print('_' * TAB_LINE)


def query_user(users):
    user_find = []
    text = input("你要查什么")
    for user in users:
        if text == '' or user.get('name').find(text) != -1 or \
                user.get('tel').find(text) != -1 or \
                user.get("address").find(text) != -1:
            user_find.append(user)

    user_find_count = len(user_find)
    if user_find_count == 0:
        print("啥都没查，确定输入内容了吗")
    elif user_find_count <= PAGE_SIZE:
        print(user_find)
    else:
        max_page = math.ceil(user_find_count / PAGE_SIZE)
        while True:
            text_page_num = input("共{0}页,请输入查询的页码-{0}".format(max_page))
            if text_page_num.isdigit() and int(text_page_num) <= max_page:
                page_num = int(text_page_num)
                print_users(user_find[(page_num - 1) * PAGE_SIZE:page_num * PAGE_SIZE])
            else:
                print("输入的页码错误")
                break


def operate(users):
    while True:
        op=input("输入操作(add modify delete query save exit)")
        if op =="add":
            users=add_user(users)
        elif op =="modify":
            pass
        elif op =="delete":
            pass
        elif op =="query":
            query_user(users)
        elif op =="save":
            save_users(users)
        elif op =="exit":
            save_users(users)
            break
        else:
            print_users("输入的参数不对")


def lock_user():
    f=open(LOCK_FILE,"w")
    f.write(str(time.time()))
    f.close()



def main():
    if not is_unlock():
        print("用户锁定")
        return
    if login():
        users=get_users()
        operate(users)
    else:
        lock_user()

main()


















