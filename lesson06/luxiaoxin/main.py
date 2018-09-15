#encoding: utf-8
#-----导入内置模块--------
#-----导入开源模块--------
#-----导入自定义模块--------
import sys_function


#系统主程序函数
def main():
    #1、检查是否锁定
    if sys_function.is_unlock():
        #2、登录
        if sys_function.login():
            #3、加载用户数据
            users = sys_function.get_user()
            #4、进行操作
            sys_function.operate(users)
        else:
            sys_function.lock_admin()

#运行主程序函数
if __name__ == '__main__':
    main()
