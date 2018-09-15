#import DB
import utils
import useradmin

LOGIN_SUCCESS = '''\033[32m
-----------------------------------
认证成功！欢迎使用本用户管理系统！
您可以执行以下操作：
    1. 添加用户(add)
    2. 删除用户(delete)
    3. 更新用户(update)
    4. 搜索用户(query)
    5. 查询用户并导出xls (export)
    6. 退出登录（exit）
-----------------------------------
\033[0m'''

# TOKEN = "0075844e71051dd19138ecf0e54179e1ad38601c"
CONFIGFILE = 'conf.ini'    # 存lock，xls，log文件路径
CONFIGFILE2 = 'conf2.ini'  # 存连接数据库需要的配置信息
LOG = 'LOG'
LOGFILE = 'LOGFILE'        # /var/log/mgt.lg
DB1 = 'DB'
DBFILE = 'DBFILE'          # /opt/user.xls
LOCKFILE = 'LOCKFILE'      # /opt/lock
LOCK_DURATION = 30         # 账户锁定时间
MAX_LOGINTIMES = 3         # 登录失败次数

# 格式化输出变量
TABLE_TPL = '{uid:>10}|{name:>10}|{age:>5}|{tel:>15}|{address:>20}'
TABLE_SPLIT_LINE = 64
TABLE_TITLE = {"uid": "uid", "name": "name", "age": "age", "tel": "tel", "address": "address"}
PAGE_SIZE = 3              # 翻页显示条数
TABLE_FORMAT = [TABLE_TPL, TABLE_SPLIT_LINE, TABLE_TITLE]


# 程序主函数
def admin_main():
    login_count = 0
    while True:
        TOKEN = input('请输入token值：')
        stat = useradmin.Github_auth(TOKEN)
        #stat = int(input('输入200：'))
        if stat == 200:
            if not useradmin.is_unlock(CONFIGFILE, DB1, LOCKFILE, LOCK_DURATION):
                print('用户锁定！')
            else:
                print(LOGIN_SUCCESS)
                '''
                此部分可以增加创建数据库和表的操作(省略)...
                DB.Create_database(DATABASE)
                DB.Create_table(DATABASE, CREATE_TABLE)
                '''
                while True:
                    text = input('请输入对应操作数字(1-6):')
                    if text.isdigit():
                        if int(text) == 1:
                            useradmin.user_add(CONFIGFILE2)
                        elif int(text) == 2:
                            useradmin.user_delete(CONFIGFILE2)
                        elif int(text) == 3:
                            useradmin.user_update(CONFIGFILE2)
                        elif int(text) == 4:
                            useradmin.user_query(CONFIGFILE2, *TABLE_FORMAT)
                        elif int(text) == 5:
                            '此部分实现导出到csv文件或xls部分' \
                            '1.实现从数据库读出所有数据' \
                            '2.将数据存到xls'
                            users, ok = useradmin.user_list(CONFIGFILE2)
                            # print(users)
                            if ok:
                                # input()
                                'users信息转为字典形式。'
                                userinfo = []
                                keys = ['uid', 'name', 'age', 'tel', 'address']
                                for x in users:
                                    userinfo.append(dict(zip(keys, list(x))))
                                useradmin.user_page(userinfo, PAGE_SIZE, *TABLE_FORMAT)  # 分页显示
                                text = input('输入yes可以保存数据到xls文件：')
                                if text == 'yes':
                                    filename, ok = utils.ReadConfigFile(CONFIGFILE, DB1, DBFILE)
                                    if ok:
                                        utils.WriteExcel(filename, userinfo)
                                        print('导出到xls成功！')
                            else:
                                print('数据查询error！')

                        elif int(text) == 6:
                            print('退出系统.....')
                            break

                    else:
                        print('输入有误')
        else:
            login_count += 1
            if login_count == MAX_LOGINTIMES:
                print('\033[0;31m认证失败3次，用户锁定！\033[0m')
                # logging.warning("失败3次，用户锁定！")
                useradmin.lock_user(CONFIGFILE, DB1, LOCKFILE)
                break
            else:
                print('\033[0;31m认证失败，请重新认证!\033[0m')
                # logging.warning("登录失败，请重新输入!")


# 程序入口
if __name__ == '__main__':
    admin_main()
