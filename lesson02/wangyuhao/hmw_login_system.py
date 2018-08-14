#!/user/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2018/8/12 下午6:20
# Author        : Yuhao.Wang
# FileName      : hmw_login_system.py
# Description   :
#
import os
import datetime
import shutil
admin_info = ('admin', '123')
count = 3

# 定义输出格式
func_tup = ('所有用户', '用户增加', '用户删除', '用户更改', '用户查询', '用户退出')
user_out_str = "{:20}\t{:20}\t{:20}\t{:20}"
user_title_str = user_out_str.format("用户编号", "用户名", "联系方式", "家庭住址")

# 初始化文件,判断文件是否存在,不存在就创建
user_file = "user.txt"
user_file_temp = "user_temp.txt"
if not os.path.exists(user_file):
    with open(user_file, 'w') as f:
        pass

# 定义一个所有用户函数,这里还是用函数吧,一次次输入的实在头疼


def print_all_user():
    '''
    打印所有用户信息:
    1/ 逐行读取文件中所有内容
    2/ 对文件每行进行处理,之后打印
    :return:
    '''
    if os.path.getsize(user_file):
        print(user_title_str)
        with open(user_file, 'r') as f:
            for line in f:
                uid, name, tel, add = line.strip().split(' ')
                print(user_out_str.format(uid, name, tel, add).strip())
    else:
        print("当前用户信息没有任何用户信息!")


# 定义一个添加用户函数
def add_user():
    '''
    1/用户传入信息
    2/追加用户传入信息到文件
    :return:
    '''
    while True:
        user_add_info = input(
            "请输入您所要添加的用户名,联系方式,家庭住址,这[3]项之间以空格分割(q/Q返回上一层):").strip()
        if user_add_info.lower() == 'q':
            break
        elif len(user_add_info.split(' ')) != 3:
            print("输入错误!")
            continue
        else:
            # 设置用户uid
            uid = 0
            with open(user_file, 'r') as f:
                for line in f:
                    if line.split(' ')[0] != '' and int(
                            line.split(' ')[0]) >= uid:
                        uid = int(line.split(' ')[0]) + 1
                        print(uid)
                    else:
                        print(line.strip(' ')[0])
            # 组装数据写入文件
            with open(user_file, 'a') as f:
                f.write("%s %s" % (uid, user_add_info + '\n'))
                f.flush()
                print("用户添加成功!")
                print_all_user()


def del_user():
    '''
    1/删除用户信息,每一次操作都对用户信息备份.
    2/将不包含所删除的用户以外的所有用户信息,重新写入到一个新的文件中
    3/将老用户文件删除
    4/将新文件重命名为用户文件
    :return:
    '''
    print_all_user()
    # 获取所有用户id
    uid_list = []
    with open(user_file) as f:
        for line in f:
            uid = int(line.split(' ')[0])
            uid_list.append(uid)
    while True:
        del_id = input("请输入你要删除的用户编号(Q/q返回上一层):")
        if del_id.lower() == 'q':
            break
        elif int(del_id) in uid_list:
            # 先备份文件,将文件中包含这个用户的行不打印到另外一个文件
            user_file_bak = "user.txt.bak.%s" % datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            shutil.copy(user_file, user_file_bak)
            with open(user_file, 'r') as src_f:
                with open(user_file_temp, 'a') as des_f:
                    for line in src_f:
                        if line.split(' ')[0] != del_id and line.strip() != '':
                            des_f.write(line)
            os.rename(user_file, "file_to_del")
            os.rename(user_file_temp, user_file)
            print_all_user()
        else:
            print("所要删除的用户不存在!")
            continue


def search_user():
    '''
    1/获取用户关键字
    2/用关键字在文件中检索
    3/打印检索到的行
    :return:
    '''
    while True:
        key = input("请输入你所要搜索的关键字(按Q/q返回上一层): ")
        if key.lower() != 'q':
            print(user_title_str)
            with open(user_file, 'r') as f:
                for line in f:
                    if key in line:
                        uid, name, tel, addr = line.strip().split(' ')
                        print(user_out_str.format(uid, name, tel, addr))
        else:
            break


def update_user():
    '''
    更改用户信息
    1/ 与删除用户信息 方式不同
    2/ 先将用户信息备份
    3/ 将所有用户信息从内存中全部读取到内存中,存放为一个列表
    4/ 修改所需要修改的用户,将修改好的列表从新组装数据,放入到文件中
    :return:
    '''
    print_all_user()
    all_user_lsit = []
    with open(user_file) as f:
        for line in f:
            ulist = line.strip().split(' ')
            all_user_lsit.append(ulist)

    while True:
        update_key = input("请输入你所要修改的用户编号(按Q/q返回上一层)").strip()
        if update_key != 'q':
            for list_temp in all_user_lsit:
                if list_temp[0] == update_key:
                    idx = all_user_lsit.index(list_temp)
                    print("所要修改的原信息为:")
                    print(
                        user_out_str.format(
                            list_temp[0],
                            list_temp[1],
                            list_temp[2],
                            list_temp[3]))
                    while True:
                        user_info = input(
                            "请输入你要修改的选项序号:1.用户名 2.联系方式 3.家庭住址 4.重新填写该用户信息(Q/q退出): ")
                        if user_info.strip() == '1':
                            name = input("请输入新用户名:")
                            all_user_lsit[idx][1] = name
                            break
                        elif user_info.strip() == '2':
                            tel = input("请输入新的联系方式:")
                            all_user_lsit[idx][2] = tel
                            break
                        elif user_info.strip() == '3':
                            addr = input("请输入新的家庭住址:")
                            all_user_lsit[idx][3] = addr
                            break
                        elif user_info.strip() == '4':
                            user_all_info = input(
                                "请输入您所要修改的用户名,联系方式,家庭住址,这[3]项之间以空格分割:").strip()
                            user_all_info_list = user_all_info.split(' ')
                            if len(user_all_info_list) == 3:
                                all_user_lsit[idx] = user_all_info_list
                                print(
                                    user_out_str.format(
                                        all_user_lsit[idx][0],
                                        all_user_lsit[idx][1],
                                        all_user_lsit[idx][2],
                                        all_user_lsit[idx][3]))
                                break
                            else:
                                print("输入错误!")
                    user_file_bak = "user.txt.bak.%s" % datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                    shutil.copy(user_file, user_file_bak)
                    with open(user_file, 'w') as f:
                        for line in all_user_lsit:
                            line_str = " ".join(line)
                            f.write(line_str + '\n')
                    print_all_user()
                else:
                    print("输入的用户编号不存在!")

        else:
            break


# login
while count > 0:
    print("用户管理系统登录".center(100, '*'))
    admin_name = input("管理员用户名:").strip()
    admin_pass = input("管理员密码:").strip()
    # 判断用户名密码
    if admin_name == admin_info[0] and admin_pass == admin_info[1]:
        print("欢迎你,%s,用户导航栏:" % admin_name)
        for i, j in enumerate(func_tup):
            print("{:>20}.{}".format(i + 1, j))
        # 用户登录成功,根据选项开始进入操作页面
        op = 0
        while op != 6:
            try:
                op = int(input("请输入你的操作序号:"))
            except ValueError as e:
                pass
            # 判断用户输入
            if op == 1:
                print("正在进入 [ %s ] 页面:" % func_tup[op - 1])
                print_all_user()
            elif op == 2:
                print("正在进入 [ %s ] 页面:" % func_tup[op - 1])
                add_user()
            elif op == 3:
                print("正在进入 [ %s ] 页面:" % func_tup[op - 1])
                if not os.path.getsize(user_file):
                    print("没有可以删除的用户!")
                else:
                    del_user()
            elif op == 4:
                print("正在进入 [ %s ] 页面:" % func_tup[op - 1])
                update_user()
            elif op == 5:
                print("正在进入 [ %s ] 页面:" % func_tup[op - 1])
                search_user()
            elif op == 6:
                print("再见!")
                break
            else:
                print("序号输入有误!")

    else:
        count -= 1
        print("用户名或密码错误!(还有 %s 次机会)" % count)
