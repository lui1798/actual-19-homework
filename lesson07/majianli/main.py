import requests
from dbconnect import conn_db
from jinja_test import jinja1
import action
import sys

def login():
    code = requests.get('https://api.github.com/user', auth=('majianli567@126.com', 'Ma540051824'))
    return code

def main():
    res = login()
    cnt = 3
    sql = "select if((select date_sub(now(),interval 1 day)) > (select max(lock_time) from admin_lock ),1,0); "
    data = conn_db(sql)
    while True:
        if res.status_code == 200 and data[0][0] == 1:
            print('登陆成功')
            while True:
                menu = "\nMenu: \n\t1:查看全部用户:\n\t2：添加用户:\n\t3：查找用户:\n\t4：删除用户：\n\t5：更新用户:\n\t6：导出csv:\n\t7：导出html\n\t8：查看配置文件\n\texit：退出系统\nPlease input your action:"
                mapf = {'1':action.query, '2':action.add, '3':action.select, '4':action.delete, '5':action.update, '6':action.dump_csv, '8':action.config,'7':jinja1, 'exit':sys.exit}
                op = input(menu).strip()
                mapf[op]()

        else:
            print('登陆失败,还有{}次机会'.format(cnt - 1))
            cnt = cnt - 1
            print(cnt)
            if cnt == 0:
                print('用户已锁定，24小时后重新登录。')
                sql = "insert into admin_lock(name) values ('majianli567@126.com');"
                conn_db(sql)
                break

if __name__ == '__main__':
    main()