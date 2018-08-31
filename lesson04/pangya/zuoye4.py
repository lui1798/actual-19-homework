# encoding: utf-8
# 定义常量
LOCK_DURATION = 30
LOGIN_INFO = ('admin', 'admin')
is_login = False
MAX_TIMES = 3
USER_FILE = "user_message.txt"
LOCK_TIME = "lock_time.txt"
USER_INFO_NUM = 4  # 定义用户列表的信息类型个数
TABLE_TPL = '{id:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
TABLE_SPLIT_LINE = 64
TABLE_TITLE = {"id": "id", "name": "name", "age": "age", "tel": "tel", "address": "address"}
PAGE_SIZE = 6
# 导入模块
import json, datetime, os, math


# 定义函数
def lock_flag():
    lock_flag = False
    if os.path.exists(LOCK_TIME) == True:
        fd = open(LOCK_TIME, 'r')
        membuf = fd.read()
        lock_time_str = membuf
        fd.close()
        lock_time = datetime.datetime.strptime(lock_time_str, "%Y-%m-%d %H:%M:%S")
        interval = datetime.datetime.now() - lock_time
        if interval.days < 1:
            lock_flag = True
    return lock_flag


def is_login():
    count = MAX_TIMES
    is_login = False
    while count > 0:
        username = input("请输入用户名:")
        password = input("请输入密码:")
        if username == LOGIN_INFO[0]:
            if password == LOGIN_INFO[1]:
                is_login = True
                break
            else:
                print("\033[31m你输入的密码错误!\033[0m")
                count -= 1
        else:
            print("\033[31m你输入的用户名错误!\033[0m")
    if count == 0:
        print("\033[31m你的账号已被锁\033[0m")
        lock_time = datetime.datetime.now()
        lock_time_str = lock_time.strftime("%Y-%m-%d %H:%M:%S")
        # data3 = json.dumps(lock_time_str)
        fd = open('lock_time.txt', 'w')
        fd.write(lock_time_str)
        fd.close()
    return is_login


def get_users():
    userinfo = []
    if os.path.exists(USER_FILE) == True:
        fd = open(USER_FILE, 'r')
        membuf = fd.read()
        fd.close()
        userinfo = json.loads(membuf)
    return userinfo


def add_users(userinfo):
    body = input("请输入你要添加用户的名字、电话、地址和年龄,并以空格隔开，（如wangli 18822888888 beijing 11）：")
    user_list = body.split(' ')
    if len(user_list) != USER_INFO_NUM:
        print("\033[31m你添加的用户信息格式错误\033[0m")
    else:
        name, tel, address, age = user_list
        has_error = False
        if not tel.isdigit():
            print("\033[31m你输入的电话号码不是数字\033[0m")
            has_error = True
        elif not age.isdigit():
            print("\033[31m你输入的年龄不是数字\033[0m")
            has_error = True
        if not has_error:
            uid = max([x.get("id") for x in userinfo] + [0]) + 1  # 生成id
            userinfo.append({
                "id": uid,
                "name": name,
                "tel": int(tel),
                "address": address,
                "age": int(age)
            })
            print("\033[32m添加用户成功\033[0m")
            return userinfo


def delete_users(userinfo):
    text = input("请输入你要删除用户的ID：")
    if text.isdigit():
        uid = int(text)
        for user in userinfo:
            if uid == user.get("id"):
                userinfo.remove(user)
                print("\033[32m用户{}删除成功\033[0m".format(uid))
                break
        else:
            print("\033[31m输入错误\033[0m")
    else:
        print("\033[31m输入错误\033[0m")
    return userinfo


def update_users(userinfo):
    text = input("请输入修改用户ID:")
    is_exists = False
    uid = 0
    if text.isdigit():
        uid = int(text)
        for user in userinfo:
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
                print("\033[31m输入的年龄不正确,请输入正确的年龄\033[0m")
            if not tel.isdigit():
                has_error = True
                print("\033[31m输入的电话不正确，请输入正确的电话\033[0m")
            if not has_error:
                for user in userinfo:
                    if uid == user.get("id"):
                        user["name"] = name
                        user["age"] = age
                        user["tel"] = tel
                        user["address"] = address
                        print("\033[32m更新成功\033[0m")
                        break
    else:
        print("\033[31m输出ID错误\033[0m")
    return userinfo


def list_users(userinfo):
    TABLE_TPL = '{id:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'  # id | name | age | tel | address
    TABLE_SPLIT_LINE = 64
    TABLE_TITLE = {"id": "id", "name": "name", "age": "age", "tel": "tel", "address": "address"}
    text = input("请输入要搜索的信息，直接回车查看全部用户信息:")
    users_find = []
    for user in userinfo:
        if text == '' or user.get("name").find(text) != -1 or \
                        str(user.get("tel")).find(text) != -1 or \
                        user.get("address").find(text) != -1 or \
                        str(user.get("age")).find(text) != -1:
            users_find.append(user)
    users_find_count = len(users_find)
    if users_find_count == 0:
        print("\033[31m没有相关信息\033[0m")
    elif users_find_count <= PAGE_SIZE:
        print(TABLE_TPL.format(
                **TABLE_TITLE))  # TABLE_TPL.format(id="id", name="name", age="age", tel="tel", address="address")
        print('-' * TABLE_SPLIT_LINE)
        for user in users_find:
            print(TABLE_TPL.format(**user))
    else:
        max_page = math.ceil(users_find_count / PAGE_SIZE)
        op1 = ""
        while True:
            text_page_num = input("共有{0}页, 请输入查询页码(1 ~ {0}),退出查看按Q/q键:".format(max_page))
            if text_page_num.isdigit() and int(text_page_num) <= max_page:
                page_num = int(text_page_num)
                print(TABLE_TPL.format(
                        **TABLE_TITLE))  # TABLE_TPL.format(id="id", name="name", age="age", tel="tel", address="address")
                print('-' * TABLE_SPLIT_LINE)
                for user in users_find[(page_num - 1) * PAGE_SIZE: page_num * PAGE_SIZE]:
                    print(TABLE_TPL.format(**user))
            elif text_page_num.lower() == 'q':
                break
            else:
                print("\033[31m输入页码错误\033[0m")


def save_users(userinfo):
    fd = open(USER_FILE, 'w')
    fd.write(json.dumps(userinfo))
    fd.close()
    print("\033[32m用户信息保存成功\033[0m")


def operate(userinfo):
    while True:
        op = input("请输入你的操作选项（注：add:添加用户信息；delete：删除用户信息；update：更新用户信息；list：搜索相关信息列表；save：保存用户信息；exit：退出用户系统)\n：")
        if op == "add":
            userinfo = add_users(userinfo)
        elif op == "delete":
            userinfo = delete_users(userinfo)
        elif op == "update":
            userinfo = update_users(userinfo)
        elif op == "list":
            list_users(userinfo)
        elif op == "save":
            save_users(userinfo)
        elif op == "exit":
            op1 = input("你修改的用户信息未保存，保存输入y/Y，不保存按任意键：")
            if op1.lower() == 'y':
                save_users(userinfo)
            break
        else:
            print("\033[31m你输入的选项不存在\033[0m")


def lock_user():
    lock_time = datetime.datetime.now()
    lock_time_str = lock_time.strftime("%Y-%m-%d %H:%M:%S")
    fd = open(LOCK_TIME, 'w')
    fd.write(lock_time_str)
    fd.close()


def main():
    # 1.判断是否锁定
    if lock_flag():
        print("\033[31m你的账号已被锁,请1天后重试\033[0m")
        return  # 使函数退出
    # 2.登录
    if is_login():
        print("****************************")
        print("\033[33m欢迎进入用户管理系统\033[0m")
        # 3登陆成功
        # 3.1加载用户数据
        userinfo = get_users()
        # 3.2操作
        operate(userinfo)
    # 4登录失败，账号锁定
    else:
        lock_user()


main()
