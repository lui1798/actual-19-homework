#coding: utf-8
'''
用户管理系统
1.登陆验证（管理员：admin / 123456），如果用户连续输错三次密码便锁定一分钟
2.登陆成功后，加载系统已存在的用户信息
3.对用户进行操作
    3.1查询并分页展示用户（支持用户名、电话、地址搜索，每页展示4条记录，通过输入页数来切换页码）
    3.2添加用户（如果添加用户名重复，则报错）
    3.3删除用户（如果删除用户不存在，则报错）
    3.4保存用户到数据库中
    3.5导出到excel中
    3.6退出（自动保存）
    3.7其他指令提示无效

'''
#导入涉及的模块

import db
import tool
import logging



#定义常量
SQL_HOST = "127.0.0.1"                                  #数据库host地址
SQL_PORT = 3306                                         #数据库port
SQL_USER = 'root'                                       #数据库用户
SQL_PASSWD ="root"                                      #数据库密码
SQL_DB = "mysql"                                        #数据库database名
MAX_LOGIN_TIMES = 3                                     #用户、密码最大输入次数
USER_NAME = "admin"                                     #管理员用户名
USER_PASSWORD = "e10adc3949ba59abbe56e057f20f883e"      #管理员用户密码
LOG_LEVEL = logging.DEBUG                               #日记级别
LOCK_TIME = 60                                          #锁定时间设置为60秒
CONF_FILE = "conf.ini"                                  #配置文件
PRINT_TITLE = "|{id:<10}|{name:<20}|{age:<4}|{tel:<12}|{address:<30}|"  # 打印表头
FORMAT_ARGS = {'id': 'id','name': 'name', 'age': 'age', 'tel': 'tel', 'address': 'address'}  # 格式化打印参数
PAGE_EACH = 4                                           # 每页打印数量

#定义变量
log_path = tool.ReadConfigFile(CONF_FILE,"LOG","LOGFILE")
logging.basicConfig(level=LOG_LEVEL,
                    filename = log_path,
                    filemode = "a",
                    format='%(asctime)s - %(filename)s[%(funcName)s] - %(levelname)s: %(message)s')


##############################################################################

def user_main():
    logging.info("-------------系统开启------------")
    if tool.lock_check(CONF_FILE,LOCK_TIME):
        if tool.login(USER_NAME,USER_PASSWORD,MAX_LOGIN_TIMES):
            print("\033[31m----------------------登陆成功------------------------\033[0m")
            logging.info("用户admin登陆成功")
        else:
            tool.login_lock(CONF_FILE)
            exit()
    else:
        print("用户锁定中，请稍后再试！")
        logging.warning("登陆失败，用户锁定")
        exit()

    #创建数据库congzhihao
    try:
        conn, cur = db.ConnectSql(SQL_HOST, SQL_PORT, SQL_USER, SQL_PASSWD, SQL_DB)
        db.CreateMysql(cur)
        cur.close()
        conn.close()
    except:
        print("数据库已存在")
    finally:
        #初始化数据库
        conn,cur = db.ConnectSql(SQL_HOST,SQL_PORT,SQL_USER,SQL_PASSWD,"congzhihao")
        db.InitSql(cur)
        conn.commit()

    while True:
        print("\033[31m-" * 40)
        print("-" * 20)
        print("请输入操作：\n","\033[34madd   ->添加\n","query ->查询\n","update->修改\n",
                               "delete->删除\n","exit  ->退出系统\n","export->导出")
        op = input("please input your option:\033[0m").strip()
        if op == "add":
            db.InsertUser(cur, conn)

        elif op == "query":
            db.SelectUser(conn,PRINT_TITLE,FORMAT_ARGS,PAGE_EACH)

        elif op == "export":
            conn.commit()
            db.ExpertUser(cur)

        elif op == "update":
            db.UpdateUser(cur, conn)

        elif op == "delete":
            db.DeleteUser(cur,conn)

        elif op == "exit":
            conn.commit()
            cur.close()
            conn.close()
            print("\033[31m--------------------退出系统成功------------------------\033[0m")
            logging.info("退出系统！！！")
            break
        else:
            print("输入指令无效，请重新输入！")
            logging.warning("错误指令")

#调用主函数
if __name__=="__main__":
    user_main()