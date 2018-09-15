import requests
from dbconnect import conn_db
import action
import sys

def login():
    code = requests.get('https://api.github.com/user', auth=('XXXXX', 'XXXX'))
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
                info ='''
 * * * * * * * * * * * * * * * *
 *1: 查看全部用户 
 *2：添加用户     
 *3：查找用户     
 *4：删除用户      
 *5：更新用户     
 *6：导出csv      
 *7：查看配置文件 
 *exit：退出系统 *
 * * * * * * * * * * * * * * * *
 '''
                print(info)
                op = input('输入动作：').strip()
                if op == '1':
                    action.query()
                if op == '2':
                    action.add()
                if op == '3':
                    action.select()
                if op == '4':
                    action.delete()
                if op == '5':
                    action.update()
                if op == '6':
                    action.dump_csv()
                if op == '7':
                    action.config()
                if op == 'exit':
                    sys.exit()
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