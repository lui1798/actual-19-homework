import requests
import time
import utils
import DB
import math
import logging

USERINFO = 'USERINFO'  # mysqls数据库默认存在表USERINFO

logging.basicConfig(
    filename="/var/log/mgt.lg",
    filemode='a',
    format="[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s",
    level=logging.DEBUG,
)

# INFO级别以上的输出到控制台
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# github认证
# TOKEN = "0075844e71051dd19138ecf0e54179e1ad38601c"
def Github_auth(TOKEN):
    headers = {'Authorization': 'token ' + TOKEN}
    req = requests.get('http://api.github.com/user', headers=headers)
    return req.status_code


# 判断用户是否锁定

def is_unlock(CONFIGFILE, DB, LOCKFILE, LOCK_DURATION):
    lock_time = 0
    try:
        msg, flag = utils.ReadConfigFile(CONFIGFILE, DB, LOCKFILE)
        if flag:
            cxt = utils.ReadFile(msg)
            lock_time = float(cxt)
    except Exception as e:
        print(e)
        logging.warning(e)
    return time.time() - lock_time > LOCK_DURATION


'----锁定用户，存当前时间-------'


def lock_user(CONFIGFILE, DB, LOCKFILE):
    msg, flag = utils.ReadConfigFile(CONFIGFILE, DB, LOCKFILE)
    # print(msg)
    if flag:
        utils.WriteFile(msg, str(time.time()))


'-----实现增操作,新增用户存入mysql-----'


def user_add(CONFIGFILE2):
    userinfo_input = input('\033[0;34m请输入用户信息(格式name age tel address):\033[0m')
    userinfo_list = userinfo_input.split(' ')
    if len(userinfo_list) != 4:
        # print('\033[0;31m未按格式要求输入!\033[0m')
        logging.warning("输入格式不对！")
    else:
        name, age, tel, address = userinfo_list
        if not age.isdigit() or not tel.isdigit():
            # print('\033[0;31m输入年龄或电话不对!\033[0m')
            logging.warning("输入年龄或电话不对！.")
        else:
            # 不重复则添加
            insert_sql = '''INSERT INTO {}(name,age,tel,address) values('{}',{},{},'{}') ON DUPLICATE KEY UPDATE name='{}',age={},tel={},address='{}';
;'''.format(USERINFO, name, age, tel, address, name, age, tel, address)
            msg, ok = DB.Insert(CONFIGFILE2, insert_sql)
            if ok:
                # print('增加用户成功！')
                logging.info('增加用户成功！')
            else:
                # print(msg)
                logging.debug(msg)


'--------实现删操作-------------'


def user_delete(CONFIGFILE2):
    uid = input('\033[0;34m请输入用户ID:\033[0m')
    if uid.isdigit():
        uid = int(uid)
        try:
            selet_sql = 'select uid from {} where uid={};'.format(USERINFO, uid)
            users, ok = DB.Select(CONFIGFILE2, selet_sql)
            if len(users) == 0 and not ok:
                print('此用户id不存在')
            else:
                delet_sql = 'delete from {} where uid ={};'.format(USERINFO, uid)
                msg, ok = DB.Delete(CONFIGFILE2, delet_sql)
                if ok:
                    # print('删除用户成功')
                    logging.info('删除用户成功！')
                else:
                    # print(msg)
                    logging.debug(msg)
        except Exception as e:
            print(e)
            # logging.warning(e)
    else:
        print('\033[0;33m输入ID错误!\033[0m')
        # logging.warning("输入用户ID错误！")


'--------------实现更新操作--------------'


def user_update(CONFIGFILE2):
    uid = input('\033[0;34m请输入要更新的用户ID：\033[0m')
    is_exists = False
    if uid.isdigit():
        uid = int(uid)
        selet_sql = 'select * from {} where uid={};'.format(USERINFO, uid)
        users, ok = DB.Select(CONFIGFILE2, selet_sql)

        if len(users) != 0 and ok:
            print('\033[0;34m要更新的内容为：{}\033[0m'.format(users))
            is_exists = True
    if is_exists:
        text = input('\033[0;34m请输入要更新的内容（格式name age tel address)，以空格分割：\033[0m')
        user = text.split(' ')
        if len(user) != 4:
            print('输入数据不正确!')
            # logging.warning("输入更新内容不正确！.")
        else:
            name, age, tel, address = user
            has_error = False
            if not age.isdigit() or not tel.isdigit():
                print('\033[0;33m年龄或电话输入有问题033[0m')
                # logging.warning("年龄或电话输入有问题！")
                has_error = True
            if not has_error:
                update_sql = '''update {} set name='{}',age={},tel={},address='{}' where uid={};'''.format(USERINFO,
                                                                                                           name, age,
                                                                                                           tel, address,
                                                                                                           uid)
                msg, ok = DB.Update(CONFIGFILE2, update_sql)
                if ok:
                    # print('\033[0;33m更新用户成功！\033[0m')
                    logging.info("更新用户成功!")
                    # logging.debug("成功更新用户信息!")
                else:
                    print(msg)


'----------用户搜索--------------'


def user_query(CONFIGFILE2, *TABLE_FORMAT):
    text = input("\033[0;34m请输入要查找的内容：\033[0m")
    if text.isdigit():
        query_sql = ''' select * from {} where uid={}  or age= {} or tel ={};'''.format(USERINFO, text, text, text)
    else:
        query_sql = ''' select * from {} where name='{}' or address ='{}';'''.format(USERINFO, text, text)
    # print(query_sql)
    users_find, ok = DB.Select(CONFIGFILE2, query_sql)
    if ok:
        userinfo = []
        keys = ['uid', 'name', 'age', 'tel', 'address']
        for x in users_find:
            userinfo.append(dict(zip(keys, list(x))))
        user_print(userinfo, *TABLE_FORMAT)
        # print(userinfo)
    else:
        # print('查询失败!')
        logging.info("查询失败!")


def user_list(CONFIGFILE2):
    list_sql = ''' select * from {};'''.format(USERINFO)
    users_find, ok = DB.Select(CONFIGFILE2, list_sql)
    return users_find, ok


# 格式化输出用户信息
def user_print(users, *TABLE_FORMAT):
    print(TABLE_FORMAT[0].format(
        **TABLE_FORMAT[2]))  # TABLE_TPL.format(id="id", name="name", age="age", tel="tel", address="address")
    print('-' * TABLE_FORMAT[1])
    for user in users:
        print(TABLE_FORMAT[0].format(**user))


# 实现翻页操作
def page_updown(users, page_count, PAGE_SIZE, *TABLE_FORMAT):
    count1 = 1
    while count1 <= page_count:
        print('\033[0;33m第 {} 页 ， 共 {} 页 \033[0m'.format(count1, page_count))
        count2 = (count1 - 1) * PAGE_SIZE
        userinfo_list_page = users[count2:count2 + PAGE_SIZE]
        user_print(userinfo_list_page, *TABLE_FORMAT)
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


# 分页显示所有用户；
def user_page(users, PAGE_SIZE, *TABLE_FORMAT):
    if len(users) == 0:
        print('\033[0;31m当前用户列表信息为空！\033[0m')
    else:
        userinfo_len = len(users)
        # 计算页数
        page_count = math.ceil(userinfo_len / PAGE_SIZE)
        # print(page_count)
        if page_count == 1:
            print('\033[0;33m第1页，共1页：\033[0m')
            user_print(users, *TABLE_FORMAT)
        else:
            # page_count = math.ceil(userinfo_len / PAGE_SIZE)
            page_updown(users, page_count, PAGE_SIZE,*TABLE_FORMAT)
