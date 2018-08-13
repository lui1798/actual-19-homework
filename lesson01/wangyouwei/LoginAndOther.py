#!/usr/bin/env python
# -*- coding: utf-8 -*-
password_list={'admin':'weiwei','wywmir':'weiwei2009'}
system_user_info=
Tries=3
while Tries > 0:
    loginname=raw_input('LoginName:')
    password=raw_input('PassWord:')
    if loginname in password_list.keys():
        if password_list[loginname]== password:
            pass
    elif Tries >1:
        print ('用户名或密码错误，还有{}次机会'.format(Tries-1))
        Tries -= 1
    elif Tries-1==0:
        print ('用户被锁定')
        pass
        break