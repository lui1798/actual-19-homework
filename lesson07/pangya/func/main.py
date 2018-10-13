import logging
import login
import oper
'''入口函数'''
logging.basicConfig(level=logging.INFO,
                    format='%(message)s')

def main():
    # 1.判断是否锁定
    if login.lock_flag():
        logging.error("你的账号已被锁,请1天后重试")
        return  # 使函数退出
    # 2.登录
    if login.is_login():
        logging.info("****************************")
        logging.info("欢迎进入用户管理系统")
        # 3.登陆成功
        # 3.2操作
        oper.LogicOper()
    # 4.登录失败，账号锁定
    else:
        login.lock_user()


main()

if __name__ == '__main__':
    main()
