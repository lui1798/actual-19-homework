import db
import logging

TABLE_TPL = '{id:>10}|{name:>15}|{age:>5}|{tel:>15}|{addr:>20}'
TABLE_TITLE = {"id" : "id", "name" : "name", "age" : "age", "tel" : "tel" , "addr": "addr"}
TABLE_SPLIT_LINE = 64

'''添加用户信息'''
def add_user():
    try:
        input_info = input('请按照以下格式输入用户信息： name age tel address :')
        user_values = input_info.split(' ')

        if len(user_values) != 4:
            return

        user_values.insert(0, max(db.Select('id')+[0])+1)
        db.Insert(user_values)
        print("\033[32m用户已添加\033[0m")
        logging.info('用户已添加')
        return
    except :
        print('\033[31m添加用户程序发生异常\033[0m')
        logging.error('添加用户程序发生异常')

'''修改指定用户信息'''
def update_user():
    try:
        user_id = input('请输入需要修改信息的用户ID:')
        if int(user_id) in db.Select('id'):
            while True:
                user_info = input('请输入需要修改的内容（name/age/tel/addr）:')
                if user_info == 'name':
                    user_name = input('请输入新用户名:')
                    db.Update(user_id,user_info,user_name)
                    print("\033[32m用户名修改成功\033[0m")
                    logging.info('操作正常')
                    update_flag = input('是否继续修改（y/n）:')
                    if update_flag == 'y':
                        continue
                    else:
                        break
                elif user_info == 'age':
                    user_age = input('请输入新年龄:')
                    db.Update(user_id,user_info,user_age)
                    print("\033[32m年龄修改成功\033[0m")
                    logging.info('操作正常')
                    update_flag = input('是否继续修改（y/n）:')
                    if update_flag == 'y':
                        continue
                    else:
                        break
                elif user_info == 'tel':
                    user_tel = input('请输入新手机号:')
                    db.Update(user_id,user_info,user_tel)
                    print("\033[32m手机号修改成功\033[0m")
                    logging.info('操作正常')
                    update_flag = input('是否继续修改（y/n）:')
                    if update_flag == 'y':
                        continue
                    else:
                        break
                elif user_info == 'addr':
                    user_add = input('请输入新地址:')
                    db.Update(user_id,user_info,user_add)
                    print("\033[32m地址修改成功\033[0m")
                    logging.info('操作正常')
                    update_flag = input('是否继续修改（y/n）:')
                    if update_flag == 'y':
                        continue
                    else:
                        break
                else:
                    print("\033[32m输入错误\033[0m")
                    logging.warning('操作错误')
                    update_flag = input('是否放弃修改（y/n）:')
                    if update_flag == 'y':
                        break
        else:
            print("\033[31m无此ID用户\033[0m")
            logging.warning('操作错误')
    except:
        print('\033[31m修改程序发生异常\033[0m')
        logging.error('操作错误')
    else:
        print("\033[32m修改完成\033[0m")
        logging.info('操作正常')
    return


'''删除'''
def delete_user():
    user_id = input('输入要删除的用户ID:')
    if db.Delete(user_id):
        print("\033[32m用户已删除\033[0m")
        logging.info('操作正常')
    else:
        print("\033[31m无此ID用户\033[0m")
        logging.warning('操作正常')

'''查询一条信息'''
def search_user():

    user_list = db.get_userdict()

    input_info = input('请输入，查找关键字 :')
    find_list = []
    for user_x in user_list:
        if input_info in user_x.values():
            find_list.append(user_x)
    if len(find_list) != 0:
        print(TABLE_TPL.format(**TABLE_TITLE))
        for user in find_list:
            print(TABLE_TPL.format(**user))
    else:
        print('\033[31m未有相关用户\033[0m')
        logging.warning('操作错误')
    return user_list


'''分页'''
def pagination():
    try:
        user_list = db.get_userdict()

        user_num = len(user_list)
        print('\033[34m用户信息数： {}\033[0m'.format(user_num))
        print(TABLE_TPL.format(**TABLE_TITLE))
        print('-' * TABLE_SPLIT_LINE)
        if user_num == 0:
            print('\033[31m暂无用户数据\033[0m')
            logging.info('操作正常')
        elif user_num <= 10:
            for user in user_list:
                print(TABLE_TPL.format(**user))
        else:
            max_page = user_num // 10
            if user_num % 10:
                max_page += 1
            while True:
                text_page_num = input('共有1-{}页，输入显示页数：'.format(max_page))
                if text_page_num.isdigit() and int(text_page_num) <= max_page:
                    page_num = int(text_page_num)
                    print('-' * TABLE_SPLIT_LINE)
                    for user in user_list[(page_num - 1) * 10: page_num * 10]:
                        print(TABLE_TPL.format(**user))
                else:
                    print('\033[33m用户数据显示结束\033[0m')
                    logging.info('操作正常')
                    break

    except:
        raise
        print('\033[31m显示用户信息程序发生异常\033[0m')
        logging.error('操作错误')

