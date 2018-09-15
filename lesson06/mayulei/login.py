import time
import datetime
import logging

password_list = ['1','1']
# lock_len =24*60*60
lock_len =10
count = 3

'''登录'''

def login(count):
    try:
        lock_flag = False
        while count > 0:

            login = input('请输入用户名:')
            password = input('请输入密码:')

            if count - 1 == 0 and lock_flag == False:
                lock_flag = True
                print('\033[31m输入用户名密码错误3次，用户被锁定\033[0m')
                logging.warning('输入用户名密码错误3次，用户被锁定')
                lock_time = int(time.time())

            elif count - 1 == 0:
                wait_time = int(time.time()) - lock_time
                if int(time.time())-lock_time > lock_len:
                    count = 2
                    lock_flag = False
                    if login == password_list[0]  and password == password_list[1]:
                        break
                    else:
                        print('\033[31m用户名或密码错误，还有{}次机会\033[0m'.format(count))
                        logging.warning('用户名或密码错误，还有{}次机会'.format(count))
                    continue

                else:
                    print('\033[31m用户被锁定,请{}秒后再输入\033[0m'.format(lock_len-wait_time))
                    logging.warning('用户被锁定,请{}秒后再输入'.format(lock_len-wait_time))
            elif login == password_list[0]  and password == password_list[1]:
                break
            else:
                print('\033[31m用户名或密码错误，还有{}次机会\033[0m'.format(count - 1))
                logging.warning('用户名或密码错误，还有{}次机会'.format(count - 1))
                count -= 1
    finally:
        print('\033[32m用户登陆成功\033[0m')
        logging.info('用户登陆成功')