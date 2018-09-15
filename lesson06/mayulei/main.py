

import db
import file
import oper
import login
import xlmtfile
import logging

count = 3
option_list=['0','1','2','3','4','5','6']

display_info='''
操作列表：
0、显示已有用户信息
1、增加用户信息
2、删除用户信息
3、修改用户信息
4、查询用户信息
5、保存用户文本信息
6、退出系统
'''


'''入口函数'''
def main():

    login.login(count)
    while True:
        file.WriteLog()
        print(display_info)

        option = input('请选择对应操作：')
        if option in option_list:

            if option == option_list[0]:
                oper.pagination()

            elif option == option_list[1]:
                oper.add_user()

            elif option == option_list[2]:
                oper.delete_user()

            elif option == option_list[3]:
                oper.update_user()

            elif option == option_list[4]:
                oper.search_user()

            elif option == option_list[5]:

                users_info = db.get_userdict()
                filename = file.ReadConfigFile('config.ini', 'DB')
                file.WriteFile(filename['TXTFILE'],users_info)
                xlmtfile.WriteExcel(filename['DBFILE'],users_info)

            elif option == option_list[6]:

                break
        else:
            print("\033[32m请再次选择操作\033[0m")
            logging.info('请再次选择操作')


if __name__ == '__main__':
    main()