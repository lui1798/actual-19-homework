# -*- coding: utf-8 -*-
from lock import *
from login import Login
from oprusers import *

# 主函数
def main():
    # 账号被锁定
    if not IsUnlock():
        return

    # 账号末被锁定且登录成功
    if Login():
        # 连接数据库
        conn, cur, m, ok = db.Connect()
        # 连接失败给错误提示
        if not ok:
            WarnMsg(m)
            return
        # 选择相应操作对用户信息进行操作
        operate(conn, cur)
    # 锁定账号
    else:
        LockUser()


# 执行主函数
if __name__ == '__main__':
    main()
