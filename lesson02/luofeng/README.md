### 用户登录
```
$ python3 user_manage.py
please enter your username: admin
please enter your password: 123344
登录失败，用户名或密码错误，还剩余2次机会，请重新输入!!!
please enter your username: admin
please enter your password: 2343
登录失败，用户名或密码错误，还剩余1次机会，请重新输入!!!
please enter your username: admin
please enter your password: 2343
用户登录失败，请15分钟后在尝试登录!!!i

$ python3 user_manage.py
lease enter your username: admin
please enter your password: reboot

--------------------------------------
欢迎登录用户系统，请选择对应的操作选项
--------------------------------------
    1. 增加用户信息(add)
    2. 删除用户信息(delete)
    3. 更新用户信息(update)
    4. 查询用户信息(find)
    5. 退出用户管理系统(exit)
--------------------------------------

select the option to operate:
```
### 增加用户信息
```
elect the option to operate: add
please add user information: wangyuhao male 23
输入错误，请重新输入，格式:ID Name Age Address

select the option to operate: add
please add user information: luof male 28 hunan

--------------------------------------
欢迎登录用户系统，请选择对应的操作选项
--------------------------------------
    1. 增加用户信息(add)
    2. 删除用户信息(delete)
    3. 更新用户信息(update)
    4. 查询用户信息(find)
    5. 退出用户管理系统(exit)
--------------------------------------

select the option to operate: add
please add user information: liqi male 23 hebei
[[1, 'luof', 'male', '28', 'hunan'], [2, 'liqi', 'male', '23', 'hebei']]
```
### 删除用户信息
```
select the option to operate: delete
Please enter the uid to delete: 5
用户UID不存在，请重新选择后在删除!!!

--------------------------------------
欢迎登录用户系统，请选择对应的操作选项
--------------------------------------
    1. 增加用户信息(add)
    2. 删除用户信息(delete)
    3. 更新用户信息(update)
    4. 查询用户信息(find)
    5. 退出用户管理系统(exit)
--------------------------------------

select the option to operate: delete
Please enter the uid to delete: 1
用户已从系统删除
```

### 更新用户信息
```
--------------------------------------
欢迎登录用户系统，请选择对应的操作选项
--------------------------------------
    1. 增加用户信息(add)
    2. 删除用户信息(delete)
    3. 更新用户信息(update)
    4. 查询用户信息(find)
    5. 退出用户管理系统(exit)
--------------------------------------

select the option to operate: update
Please enter the user name to update information: luof
Please modify the user information: luofeng male 28 beijing
用户luof信息更新成功.
```
### 查询用户信息
```
select the option to operate: find
please enter the user name to query: wangyuhao
用户wangyuhao不存在，请重新选择后在查询!!!

--------------------------------------
欢迎登录用户系统，请选择对应的操作选项
--------------------------------------
    1. 增加用户信息(add)
    2. 删除用户信息(delete)
    3. 更新用户信息(update)
    4. 查询用户信息(find)
    5. 退出用户管理系统(exit)
--------------------------------------

select the option to operate: find
please enter the user name to query: luofeng
-------------------------------------------------------
ID     		Name   		Sex    		Age    		Address
1      		luofeng		male   		28     		beijing
-------------------------------------------------------
```
### 退出用户信息系统
```
-------------------------------
欢迎登录用户系统，请选择对应的操作选项
-------------------------------
    1. 增加用户信息(add)
    2. 删除用户信息(delete)
    3. 更新用户信息(update)
    4. 查询用户信息(find)
    5. 退出用户管理系统(exit)
-------------------------------

select the option to operate: exit
```
