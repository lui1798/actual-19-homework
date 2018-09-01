# 本次作业函数实现。

import json
import time
import math

LOGINFO = ('admin', '51reboot')  # 登陆用户名密码
LOCK_FILE = "lock"
USER_FILE = "user.json"
USER_INFO_NUM = 4
MAX_LOGINTIMES = 3  # count  次数限制3次，连续3次密码错误，第二天后再登
LOCK_DURATION = 30  # 锁定时间限定
PAGE_SIZE = 5

# 格式化输出
TABLE_TPL = '{userid:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
TABLE_SPLIT_LINE = 64
TABLE_TITLE = {"userid": "userid", "name": "name", "age": "age", "tel": "tel", "address": "address"}

# 登录成功界面
login_sucess = '''\033[32m
-----------------------------------
登录成功！本用户管理系统可以执行以下操作：
    1. 添加用户(add)
    2. 删除用户(delete)
    3. 更新用户(update)
    4. 查询用户(list)
    5. 按关键字搜索用户(find)
    6. 退出登录（exit）
-----------------------------------
\033[0m'''


# 1. 检查是否被锁定

def is_unlock():
    lock_time = 0
    try:
        fd = open(LOCK_FILE, 'r')
        cxt = fd.read()
        # print(cxt)
        fd.close()
        lock_time = float(cxt)
    except Exception as e:
        print(e)
    return time.time() - lock_time > LOCK_DURATION


# 锁定用户，存当前时间
def lock_user():
    fhandler = open(LOCK_FILE, "w")
    fhandler.write(str(time.time()))
    fhandler.close()


# 获取用户信息
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


# 实现增操作，将输入信息转为字典格式存储在列表中
def user_add(users):
    userinfo_input = input('\033[0;34m请输入用户信息(格式name age tel address):\033[0m')
    userinfo_list = userinfo_input.split(' ')
    # print(userinfo_dic)
    if len(userinfo_list) != 4:
        print('\033[0;31m未按格式要求输入!\033[0m')
    else:
        name, age, tel, address = userinfo_list
        if not age.isdigit() or not tel.isdigit():
            print('\033[0;31m输入年龄或电话不对!\033[0m')
        else:
            # 不重复则添加，重复则报错
            userinfo_dic = {
                'userid': ' ',
                'name': name,
                'age': age,
                'tel': tel,
                'address': address
            }
            same_flag = False
            for x in users:
                if list(x.values())[1:] == list(userinfo_dic.values())[1:]:
                    same_flag = True
            if not same_flag:
                uids = [x.get('userid') for x in users]
                new_id = max(uids) + 1
                userinfo_dic['userid'] = new_id
                users.append(userinfo_dic)
                print('\033[0;33m添加成功，可以通过list查看！\033[0m')
            else:
                print('\033[0;33m用户已存在，请重新添加！\033[0m')
    return users


# 实现删操作
def user_delete(users):
    if len(users) == 0:
        print('\033[0;31m用户信息列表为空，不能删除!\033[0m')
    else:
        uid = input('\033[0;34m请输入用户ID:\033[0m')
        if uid.isdigit():
            uid = int(uid)
            if uid in [x['userid'] for x in users]:
                for x in users:
                    if x['userid'] == uid:
                        users.remove(x)
            else:
                print('\033[0;33m用户ID不存在，请通过搜索找到用户ID再尝试删除！\033[0m')
        else:
            print('\033[0;33m输入ID错误!\033[0m')
    return users


# 实现更新操作
def user_update(users):
    text = input('\033[0;34m请输入要更新的用户ID：\033[0m')
    is_exists = False
    if text.isdigit():
        uid = int(text)
        for user in users:
            if uid == user.get("userid"):
                print('\033[0;34m要更新的内容：{}\033[0m'.format(user))
                is_exists = True
                break
    if is_exists:
        text = input('\033[0;34m请输入要更新的内容（格式name age tel address)，以空格分割：\033[0m')
        user = text.split(' ')
        if len(user) != 4:
            print('\033[0;33m输入数据不正确033[0m')
        else:
            name, age, tel, address = user
            has_error = False
            if not age.isdigit() or not tel.isdigit():
                print('\033[0;33m年龄或电话输入有问题033[0m')
                has_error = True
            if not has_error:
                for user in users:
                    if uid == user.get('userid'):
                        users.remove(user)
                        users.append({
                            'userid': uid,
                            'name': name,
                            'age': int(age),
                            'tel': tel,
                            'address': address
                        })
            print('\033[0;33m更新用户成功！\033[0m')


# 格式化输出用户信息
def user_print(users):
    print(TABLE_TPL.format(
        **TABLE_TITLE))  # TABLE_TPL.format(id="id", name="name", age="age", tel="tel", address="address")
    print('-' * TABLE_SPLIT_LINE)
    for user in users:
        print(TABLE_TPL.format(**user))


def page_updown(users, page_count):
    count1 = 1
    while count1 <= page_count:
        print('\033[0;33m第 {} 页 ， 共 {} 页 \033[0m'.format(count1, page_count))
        count2 = (count1 - 1) * PAGE_SIZE
        userinfo_list_page = users[count2:count2 + PAGE_SIZE]
        user_print(userinfo_list_page)
        nextorback = input('\033[0;33m请输入up或down进行翻页,也可以选择exit退出翻页：\033[0m')
        if nextorback == 'down':
            count1 += 1
            if count1 == page_count + 1:
                print('\033[0;33m最后一页，请尝试返回！\033[0m')
                count1 = page_count
        elif nextorback == 'up':
            count1 -= 1
            if count1 == 0:
                count1 = 1
                print('\033[0;33m已返回首页，请尝试下翻！\033[0m')
        elif nextorback == 'exit':
            break
        else:
            print('\033[0;31m输入错误！\033[0m')


# 分页显示当前用户信息列表中存在的所有用户；
def user_list(users):
    if len(users) == 0:
        print('\033[0;31m当前用户列表信息为空！\033[0m')
    else:
        userinfo_len = len(users)
        # 计算页数
        page_count = math.ceil(userinfo_len / PAGE_SIZE)
        #print(page_count)
        if page_count == 1:
            print('\033[0;33m第1页，共1页：\033[0m')
            user_print(users)
        else:
            #page_count = math.ceil(userinfo_len / PAGE_SIZE)
            page_updown(users, page_count)


# 用户搜索
def user_query(users):
    users_find = []
    text = input('\033[0;34m请输入要查找的内容：\033[0m')
    for user in users:
        if text == ' ' or user.get('name').find(text) != -1 or \
                user.get('tel').find(text) != -1 or \
                user.get('address').find(text) != -1 or \
                str(user.get('age')) == text or \
                str(user.get('userid')) == text:
            users_find.append(user)
    user_list(users_find)


# 保存用户信息
def user_save(users):
    fhandler = open(USER_FILE, "w")
    fhandler.write(json.dumps(users))
    fhandler.close()



# 选择增删改查执行用户管理
def user_operate(users):
    exit_flag = False
    while not exit_flag:
        op = input('\033[0;34m请输入操作方式(add/delete/update/list/query/exit) :\033[0m')
        if op == 'add':
            user_add(users)
        elif op == 'delete':
            user_delete(users)
        elif op == 'update':
            user_update(users)
        elif op == 'list':
            user_list(users)
        elif op == 'query':
            user_query(users)
        elif op == 'exit':
            user_save(users)
            print("程序退出，自动保存用户！")
            exit_flag = True
            # break
        else:
            print('\033[0;31m无效输入!\033[0m')
    return exit_flag


def main():
    login_count = 0
    while True:
        username = input('\033[0;34m请输入用户名:\033[0m')
        password = input('\033[0;34m请输入密码:\033[0m')
        if username == LOGINFO[0]:
            if not is_unlock():
                print('\033[0;31m用户已锁定,请稍后再试\033[0m')
            else:
                while login_count < MAX_LOGINTIMES:
                    if password == LOGINFO[1]:
                        login_count = 0
                        print(login_sucess)
                        users = get_users()
                        if user_operate(users):
                            break
                    else:
                        login_count += 1
                        if login_count == MAX_LOGINTIMES:
                            print('\033[0;31m失败3次，用户锁定！\033[0m')
                            lock_user()
                            login_count = 0
                        else:
                            print('\033[0;31m登录失败，请重新输入!\033[0m')
                        break
        else:
            print('\033[0;31m此账户不存在，请检查输入或选择退出！\033[0m')
            exit_sys = input('\033[0;33m输入yes选择退出：\033[0m')
            if exit_sys == 'yes':
                break


main()