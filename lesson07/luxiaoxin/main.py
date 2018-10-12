#encoding: utf-8
#-----导入内置模块--------
#-----导入开源模块--------
#-----导入自定义模块--------
from apps.lock import is_unlock, lock_admin
from apps.login import  login
from apps.sys_operation import get_user, operate



#系统主程序函数
def main():
    #1、检查是否锁定
    if is_unlock():
        #2、登录
        if login():
            #3、加载用户数据
            users = get_user()
            #4、进行操作
            operate(users)
        else:
            lock_admin()

#运行主程序函数
if __name__ == '__main__':
    main()
