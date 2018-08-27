# encoding: utf-8
# 导入模块
import time, getpass, json, math
from config import LOCK_FILE, LOCK_DURATION, ADMIN_USERNAME, ADMIN_PASSWORD, MAX_LOGIN_TIMES, USER_FILE, USER_INFO_NUM, \
    TABLE_TPL, TABLE_SPLIT_LINE, TABLE_TITLE, PAGE_SIZE


#   打印操作提示方法
def print_info(content):
    print("\033[1;31;40m%s\033[0m" % content)


#   判断账号是否锁定方法
def is_unlock():
    lock_time = 0
    try:
        fhandler = open(LOCK_FILE, "r")
        cxt = fhandler.read()
        if cxt == '':
            fhandler.close()
            return True
        else:
            fhandler.close()
            lock_time = float(cxt)
    except Exception as e:
        print(e)

    return time.time() - lock_time > LOCK_DURATION


def lock():
    fhandler = open(LOCK_FILE, "w+")
    fhandler.write(str(time.time()))
    fhandler.close()


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
            print_info("登陆失败, 锁定用户")
        else:
            print_info("登陆失败, 请重新输入用户名, 密码")

    return is_login


def get_users():
    users = []
    try:
        fhandler = open(USER_FILE, "r")
        cxt = fhandler.read()
        fhandler.close()
        users = json.loads(cxt)
    except Exception as e:
        print(e)
    return users


def add(users):
    text = input("请依次输入用户信息(用户名, 年龄, 电话号码, 地址), 信息使用空格分割:")
    user = text.split()
    if len(user) != USER_INFO_NUM:
        print_info("输入数据不正确")
    else:
        name, age, tel, address = user
        has_error = False
        if not age.isdigit():
            print_info("年龄输入有问题")
            has_error = True

        if not tel.isdigit():
            print("电话号码有问题")
            has_error = True

        if not has_error:
            # 生成id
            uid = max([x.get("id") for x in users] + [0]) + 1
            users.append({
                "id": uid,
                "name": name,
                "age": int(age),
                "tel": tel,
                "address": address
            })
            print_info("添加用户成功")


def query(users):
    text = input("请输入查询的字符串:")
    users_find = []
    for user in users:
        if text == '' or user.get("name").find(text) != -1 or \
                        user.get("tel").find(text) != -1 or \
                        user.get("address").find(text) != -1:
            users_find.append(user)

    users_find_count = len(users_find)
    if users_find_count == 0:
        print_info("无数据")
    elif users_find_count <= PAGE_SIZE:
        print(TABLE_TPL.format(
            **TABLE_TITLE))  # TABLE_TPL.format(id="id", name="name", age="age", tel="tel", address="address")
        print('-' * TABLE_SPLIT_LINE)
        for user in users_find:
            print(TABLE_TPL.format(**user))
    else:
        max_page = math.ceil(users_find_count / PAGE_SIZE)

        while True:
            text_page_num = input("共有{0}页, 请输入查询页码(1 ~ {0})//退出查看请输入q: ".format(max_page))
            if text_page_num.isdigit() and int(text_page_num) <= max_page:
                page_num = int(text_page_num)
                print(TABLE_TPL.format(
                    **TABLE_TITLE))  # TABLE_TPL.format(id="id", name="name", age="age", tel="tel", address="address")
                print('-' * TABLE_SPLIT_LINE)
                for user in users_find[(page_num - 1) * PAGE_SIZE: page_num * PAGE_SIZE]:
                    print(TABLE_TPL.format(**user))
            elif text_page_num == 'q':
                break
            else:
                print("输入页码错误")
                break


def modify(users):
    text = input("请输入修改用户ID:")
    is_exists = False
    uid = 0
    if text.isdigit():
        uid = int(text)
        for user in users:
            if uid == user.get("id"):
                print_info("更新用户信息:" + json.dumps(user))
                is_exists = True
                break

    if is_exists:
        text = input("请依次输入用户信息(用户名, 年龄, 电话号码, 地址), 信息使用空格分割:")
        user = text.split()
        if len(user) != USER_INFO_NUM:
            print_info("输入数据不正确")
        else:
            name, age, tel, address = user
            has_error = False
            if not age.isdigit():
                has_error = True
                print_info("输入的年龄不正确")

            if not tel.isdigit():
                has_error = True
                print_info("输入的电话不正确")

            if not has_error:
                for user in users:
                    if uid == user.get("id"):
                        user["name"] = name
                        user["age"] = age
                        user["tel"] = tel
                        user["address"] = address
                        print_info("更新成功")
                        break
    else:
        print_info("输出ID错误")


def delete(users):
    text = input("请输入删除用户的ID:")
    if text.isdigit():
        uid = int(text)
        for user in users:
            if uid == user.get("id"):
                confirm = input('请确认是否真的要删除？确认y，取消n')
                if confirm == 'y':
                    users.remove(user)
                    print_info("删除用户成功")
                    break
                else:
                    print_info('已取消删除！')
                    break
        else:
            print_info("输入ID错误")
    else:
        print_info("输入ID错误")


def save(users):
    fhandler = open(USER_FILE, "w")
    fhandler.write(json.dumps(users))
    fhandler.close()


def operate(users):
    while True:
        op = input("请输入操作(add,modify,delete,query,save,exit):")
        if op == "add":
            add(users)
        elif op == "modify":
            modify(users)
        elif op == "delete":
            delete(users)
        elif op == "query":
            query(users)
        elif op == "save":
            save(users)
            print("存储用户信息成功")
        elif op == "exit":
            save(users)
            print_info("退出程序, 自动存储用户信息")
            break
        else:
            print_info("输入错误")


# 主函数
def main():
    #   判断是否锁定
    if is_unlock():
        #   判断是否登录成功
        if login():
            print_info("登录成功")
            # 3. 登录完成, 加载用户
            users = get_users()
            # 4. 操作add,modify,delete,query,save,exit
            operate(users)

        else:
            lock()  # 锁定用户
    else:
        print_info("已经被锁定, 请稍后再试")

main()