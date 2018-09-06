# -*- coding: utf-8 -*-
# 引入模块
import time, json, math, getpass, logging

'''
---------------------------------
            常量部分
---------------------------------
'''
# 用户锁定相关:锁定存储文件，锁定时长
LOCK_FILE = "lock"
LOCK_DURATION = 30
# LOCK_DURATION = 24 * 60 * 60

# 管理员账号密码
ADMIN_NAME = "admin"
ADMIN_PWD = "111111"

# 最大输入错误次数
MAX_LOGIN_TIMES = 3

# 用户信息存储文件
USER_FILE = 'user.json'

# 输入用户信息长度
USER_INFO_NUM = 4
# 分页大小
PAGE_SIZE = 2

# 显示表格样式
TABLE_TPL = '|{id:^10}|{name:^10}|{age:^5}|{tel:^15}|{address:^20}|'
TABLE_SPLIT_LINE = 66
TABLE_TITLE = {"id": "id", "name": "name", "age": "age", "tel": "tel", "address": "address"}

# 日志配置项
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s'
LOG_FILENAME = 'usermanage.log'
LOG_FILEMODE = 'a'
LOG_ENCODING = 'utf-8'


# 解决中文乱码问题
# 1> 通过实例化并设置相关项
logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter(LOG_FORMAT)
fh = logging.FileHandler(LOG_FILENAME, encoding=LOG_ENCODING)
fh.setLevel(logging.DEBUG)
# fh.setFormatter(formatter)
fh.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(fh)

# 2> 修改FileHandler类
'''
    找到FileHandler类修改：
    def __init__(self, filename, mode='a', encoding=None, delay=False):
    为：
    def __init__(self, filename, mode='a', encoding='utf-8', delay=False):
    最后如下所示：
    class FileHandler(StreamHandler):
    """
    A handler class which writes formatted logging records to disk files.
    """
    def __init__(self, filename, mode='a', encoding='utf-8', delay=False):
    最后用logging.basicConfig进行设置即可
'''
# logging.basicConfig(
#     # level=logging.DEBUG,
#     # format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
#     # filename='login.log',
#     # filemode='a'
#     level=LOG_LEVEL,
#     format=LOG_FORMAT,
#     filename=LOG_FILENAME,
#     filemode=LOG_FILEMODE
# )
# logging.basicConfig()

'''
---------------------------------
            函数部分
---------------------------------
'''
# 读文件函数
def read_file(fname):
    data = ''
    try:
        fhandler = open(fname, 'r')
        data = fhandler.read()
        fhandler.close()
    except Exception as e:
        pass
    return data


# 写文件函数，参数：fname文件参数/data写入的数据/ser是否进行系列化
def write_file(fname, data, ser):
    fhandler = open(fname, 'w')
    if ser == 'json':
        fhandler.write(json.dumps(data))
    else:
        fhandler.write(data)
    fhandler.close()


# 显示提示信息函数，参数：msg要显示的信息/status成功或失败的状态
# def print_msg(msg, status):
#     if status == 'success':
#         print('\033[34m{}\033[0m'.format(msg))
#     if status == 'error':
#         print('\033[31m{}\033[0m'.format(msg))


# 装修器函数，显示操作提示的同时将操作日志保存到日志文件
def log_msg(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "debug":
                logger.debug(*args, **kwargs)
                # logging.debug(*args, **kwargs)
            elif level == "warn":
                logger.warn(*args, **kwargs)
                # logging.warn(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator


# 成功时提示信息
@log_msg(level="debug")
def succ_msg(msg):
    print('\033[34m{}\033[0m'.format(msg))


# 错误或警告时提示信息
@log_msg(level="warn")
def warn_msg(msg):
    print('\033[31m{}\033[0m'.format(msg))


# 提示用户输入函数
def input_msg(msg):
    data = input("\033[33m{}\033[0m".format(msg)).strip()
    return data


# 显示用户信息函数
def print_users(users):
    print('-' * TABLE_SPLIT_LINE)
    print(TABLE_TPL.format(**TABLE_TITLE))
    print('-' * TABLE_SPLIT_LINE)
    for user in users:
        print(TABLE_TPL.format(**user))
    print('-' * TABLE_SPLIT_LINE)


# 锁定用户函数
def lock_user():
    current_time = str(time.time())
    write_file(LOCK_FILE, current_time, '')


# 判断是否被锁定函数
def is_unlock():
    lock_time = 0
    res = read_file(LOCK_FILE)
    try:
        lock_time = float(res)
    except Exception as e:
        # warn_msg(e)
        pass
    return time.time() - lock_time > LOCK_DURATION


# 登录函数
def login():
    is_login = False
    count = 1
    while count <= MAX_LOGIN_TIMES:
        username = input_msg("请输入管理员用户名：")
        if username == ADMIN_NAME:
            count = 1
            while count <= MAX_LOGIN_TIMES:
                # password = getpass.getpass("请输入管理员密码：")
                password = input_msg("请输入管理员密码：")
                if password == ADMIN_PWD:
                    succ_msg("你已经登陆成功！")
                    is_login = True
                    return is_login
                else:
                    warn_msg("你输入的密码有误，请重新输入！")
                    count += 1
        else:
            warn_msg("你输入的用户名错误，请重新输入！")
            count += 1

    warn_msg("你输入错误已经超过三次，账号被锁定！")
    return is_login


# 获取用户信息
def get_users():
    users = []
    data = read_file(USER_FILE)
    try:
        users = json.loads(data)
    except Exception as e:
        warn_msg(e)
        pass
    return users


# 增加用户信息函数
def add_user(users):
    user = input_msg("请输入你要增加的用户信息 [姓名 年龄 手机 地址，以空格格开]：").split()
    if len(user) != 4:
        warn_msg("你输入的信息有误！")
    else:
        name, age, tel, address = user
        has_error = False
        if not age.isdigit():
            warn_msg("输入的年龄错误，必须为数字！")
            has_error = True
        if not tel.isdigit():
            warn_msg("输入的电话号码错误，必须为数字！")
            has_error = True
        if not has_error:
            uid = max([x.get("id") for x in users] + [0]) + 1
            users.append({
                "id": uid,
                "name": name,
                "age": int(age),
                "tel": int(tel),
                "address": address
            })
            succ_msg("添加用户信息成功！")
    return users


# 删除用户信息函数
def del_user(users):
    has_error = False
    if len(users) == 0:
        succ_msg("暂无用户相关信息！")
    else:
        try:
            uid = int(input_msg("请输入你要删除的用户的ID: "))
        except Exception as e:
            warn_msg("输入的用户ID错误，必须为数字！")
            has_error = True
        if not has_error:
            is_remove = False
            for user in users:
                if uid == user.get("id"):
                    users.remove(user)
                    is_remove = True
            if is_remove:
                succ_msg("删除用户成功！")
            else:
                warn_msg("输入的用户ID不存在！")
    return users


# 修改用户信息函数
def modify_user(users):
    is_exists = False
    uid = input_msg("请输入你要修改的用户的ID：")
    if uid.isdigit():
        uid = int(uid)
        for user in users:
            if uid == user.get("id"):
                succ_msg("更新用户信息：" + json.dumps(user))
                is_exists = True
    if is_exists:
        user = input_msg("请输入你要增加的用户信息 [姓名 年龄 手机 地址，以空格格开]：").split()
        if len(user) != USER_INFO_NUM:
            warn_msg("你输入的信息有误！")
        else:
            name, age, tel, address = user
            has_error = False
            if not age.isdigit():
                has_error = True
                warn_msg("输入的年龄错误，必须为数字！")

            if not tel.isdigit():
                has_error = True
                warn_msg("输入的手机错误，必须为数字！")

            if not has_error:
                for user in users:
                    if uid == user.get('id'):
                        user["name"] = name
                        user["age"] = int(age)
                        user["tel"] = int(tel)
                        user["address"] = address
                        succ_msg("用户信息更新成功！")
    else:
        warn_msg("输入的用户ID不存在！")
    return users


# 查询用户信息函数
def query_user(users):
    users_find = []
    data = input_msg("请输入要查询的内容：")
    for user in users:
        if data == "" or user.get("name").find(data) != -1 \
            or user.get("address").find(data) != -1:
            users_find.append(user)

    users_find_count = len(users_find)
    if users_find_count == 0:
        succ_msg("暂无用户相关信息！")
    elif users_find_count <= PAGE_SIZE:
        print_users(users_find)
    else:
        max_page = math.ceil(users_find_count / PAGE_SIZE)
        while True:
            page_num = input_msg("用户信息共有{0}页，请输入查询页码[1 ~ {0}]，按q键则返回上级菜单:".format(max_page)).strip().lower()
            if page_num.isdigit() and int(page_num) <= max_page:
                page_num = int(page_num)
                print_users(users_find[(page_num - 1) * PAGE_SIZE : page_num * PAGE_SIZE])
            elif page_num == 'q':
                succ_msg("返回上级菜单！")
                break
            else:
                warn_msg("你输入的页码错误！")
                break


# 保存用户信息函数
def save_users(users):
    data = users
    write_file(USER_FILE, data, 'json')
    succ_msg("成功保存用户信息！")


# 选择操作函数
def operate(users):
    while True:
        op = input_msg("请输入相关操作[add, delete, modify, query, save, exit]：")
        if op == "add":
            users = add_user(users)
        elif op == "delete":
            users = del_user(users)
        elif op == "modify":
            users = modify_user(users)
        elif op == "query":
            query_user(users)
        elif op == "save":
            save_users(users)
        elif op == "exit":
            save_users(users)
            succ_msg("正在退出系统！")
            break
        else:
            warn_msg("不存在你输入的相关操作！")


# 主函数
def main():
    # 账号被锁定
    if not is_unlock():
        warn_msg("用户被锁定，请稍后再试！")
        return
    # 账号末被锁定且登录成功
    if login():
        # 获取用户信息
        users = get_users()
        # 选择相应操作对用户信息进行操作
        operate(users)
    # 账号被锁定
    else:
        lock_user()


# 执行主函数
if __name__ == '__main__':
    main()
