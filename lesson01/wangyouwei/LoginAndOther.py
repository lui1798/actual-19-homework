#!/usr/bin/env python
# -*- coding: utf-8 -*-
password_list={'admin':'weiwei','wywmir':'weiwei2009'}
userlist = [  # list
    (1, 'monkey1', '132xxxx', 'beijing'),   # tuple
    (2, 'shuaige123', '139xxxx', 'shanghai'),
    (3, 'xaioyue2', '135xxxx', 'zhengzhou'),
]
Tries=3
while Tries > 0:
    loginname=raw_input('LoginName:')
    password=raw_input('PassWord:')
    if loginname in password_list.keys() and password_list[loginname]== password:
        op = raw_input('please input action:')
        break

    elif Tries-1==0:
        print ('用户被锁定')
        pass
        break
    else:
        print ('用户名或密码错误，还有{}次机会'.format(Tries-1))
        Tries -= 1
if op == 'list':
    print (userlist)