import os
import time
import datetime


LOGIN_DB = ('admin', '123456')
MAX_LOGIN_FAILED_COUNT = 3
LOCK_FILE = 'lock.db'
LOCK_INTERVAL_SECOND = 1 * 24 * 3600
USERINFO_DB = []


def println(msg):
    cur_datetime = datetime.datetime.now()
    output = "{} {}".format(cur_datetime, msg)
    print(output)


def dump():
    pass


def load():
    pass


def login():
    _cnt = MAX_LOGIN_FAILED_COUNT
    while _cnt != 0:
        username = input("please input your username: ")
        password = input("please input your password: ")
        if username == LOGIN_DB[0] and password == LOGIN_DB[1]:
            return '', True
        else:
            _cnt -= 1
            errmsg = "Login failed, You have {} change, please try again.".format(_cnt)
            println(errmsg)
    return 'Too many login failures', False


def lock():
    fd = open(LOCK_FILE, 'w')
    fd.write(str(int(time.time())))
    fd.close()


'''获取登录用户的状态'''
def get_state():
    '''
    if True, user normal, else user lock.
    '''
    if os.path.exists(LOCK_FILE):
        fd = open(LOCK_FILE, 'r')
        up_timestamp = fd.read()
        fd.close()
        if int(time.time()) - int(up_timestamp) >= LOCK_INTERVAL_SECOND:
            return '', True
        else:
            return 'User is lock.', False
    else:
        return '', True


def add():
    body = input('please input user info: ')



def delete():
    pass


def update():
    pass


def find():
    pass


def list():
    pass


def operate():
    op = input('please input your op command: ')
    if op == 'add':
        add()
    elif op == 'delete':
        pass




def main():
    state_msg, ok = get_state()
    if ok:
        login_msg, ok = login()
        if ok:
            operate()
        else:
            println(login_msg)
            lock()
    else:
        println(state_msg)





if __name__ == '__main__':
    main()