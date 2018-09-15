#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: ZhouGui
# @Date  : 2018/9/9
# @Description : 程序入口函数
import login
import lock
import operate


def main():
    if not lock.is_unlock():
        print("\033[1;31m 用户被锁定，请稍后重试\033[0m")
        return
    if login.login():
        users = operate.get_users()
        operate.operate(users)
    else:
        lock.lock_user()


if __name__ == '__main__':
    main()
