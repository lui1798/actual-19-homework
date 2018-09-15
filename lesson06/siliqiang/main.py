#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : taurusslq
# @Time    : 2018/8/26
# @File    : lesson-4.py
# @Software: PyCharm



from modulelock import is_lock,is_unlock,lock_login
from modulelogin import login
from moduleop import op_users
from modulelog import log



'''
主函数
'''
def main():

    log()

    if not is_unlock():
        lock_login()
        return
    if login():
        op_users()
    else:
        is_lock()

if __name__ == "__main__":
    main()