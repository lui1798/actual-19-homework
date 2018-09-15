#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/9/16 上午1:10
# Author        : Yuhao.Wang
# FileName      : main.py
# Description   : 
#

from mdlock import is_lock,is_unlock,lock_login
from login import login
from mdop import op_users
from mdlog import log



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