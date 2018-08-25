import json
import datetime
#  原始数据
user_list = [
	{'name' : '张三', 'age':'20', 'tel':'132xxx', 'address':'beijing', 'id':1},
	{'name' : '李四', 'age':'30', 'tel':'136xxx', 'address':'shanghai', 'id':2},
	{'name' : '王五', 'age':'40', 'tel':'135xxx', 'address':'guangzhou', 'id':3},
	{'name' : '马六', 'age':'50', 'tel':'186xxx', 'address':'hangzhou', 'id':4}]

# 写文件函数
def writefile(userinfor):
    with open('list_user.txt','a') as f:
        userinfor = json.dumps(userinfor) + "\n"
        f.write(userinfor)

# 将原始数据写入文件
# for i in user_list:
#      writefile(i)
# # 读文件函数
def readfile():
    with open('list_user.txt','r') as f:
        res = f.readlines()
        return res
#清空文件
def empyt():
    with open("list_user.txt", "w") as f:
        f.truncate()
#list
def list():
    res = readfile()
    for i in res:
        i = json.loads(i)
        print(i["id"], i["name"], i["tel"], i["age"], i["address"])

#add
def add():
    user_list = []
    user_dict = {}
    userinfor = input('输入添加的用户信息：（format：name age tel addr）')
    userinfor_1 = userinfor.split()
    ress = readfile()
    for i in ress:
        print(i)
        i = json.loads(i)
        user_list.append(i['id'])
    if not user_list:
        max_id = 1
    else:
        max_id = int(max(user_list)) + 1
    user_list = []
    user_list.append(max_id)
    user_list.extend(userinfor_1)
    user_dict['id'] = user_list[0]
    user_dict['name'] = user_list[1]
    user_dict['age'] = user_list[2]
    user_dict['tel'] = user_list[3]
    user_dict['address'] = user_list[4]
    writefile(user_dict)
#select
def select():
    flag = True
    username = input('输入查询的名字：').strip()
    res = readfile()
    for i in res:
        i = json.loads(i)
        if i['name'] == username:
            print(i["id"], i["name"], i["tel"], i["age"], i["address"])
            flag = False
    if flag:
        print("无此用户")
#delete
def delete():
    userinfo = input('输入你要删除的用户：').strip()
    user_list = []
    res = readfile()
    for i in res:
         i = json.loads(i)
         user_list.append(i)
    empyt()
    for i in user_list:
        if userinfo == i['name']:
            pass
        else:
            writefile(i)
    print('用户"{}" 已成功删除.'.format(userinfo))
#update
def update():
    userinfo = input('输入你要修改的用户：').strip()
    res = readfile()
    user_list = []
    for i in res:
        i = json.loads(i)
        user_list.append(i)

    flag = True
    for i in user_list:
        # print(i)
        if userinfo == i['name']:
            update_befor = input('输入要修改的字段（format:[name|age|tel|addres]）：')
            update_after = input('新的{}:'.format(update_befor))
            if update_befor == 'name':
                i['name'] = update_after

            elif update_befor == 'age':
                i['age'] = update_after

            elif update_befor == 'tel':
                i['tel'] = update_after

            elif update_befor == 'addres':
                i['addres'] = update_after

            else:
                print('输入有误,请重新输入.')
                flag = False
            print('用户"{}" 已成功更新.'.format(userinfo))
            flag = False

    if flag:
        print("没有此用户")
    empyt()
    for i in user_list:
        print(i)
        writefile(i)

# 管理账号登陆
login = ('root','123456')
reflag = 0
def log_in():
    cunt = 0
    flag = True
    while cunt < 3:
        try:
            if not flag:
                print('退出系统')
                break
            username = input('输入管理员姓名:').strip()
            password = input('输入管理员密码:').strip()
            if username.strip() == login[0] and password.strip() == login[1]:
                with open('lock.txt','r') as f:
                    time = f.read()
                    if time:
                        time = time.split(",")
                        time_tmp = time[1]
                        time_tmp_1 = datetime.datetime.strptime(time_tmp,'%Y-%m-%d %H:%M:%S')
                        if time_tmp_1 >= datetime.datetime.now():
                            print('账户锁定中，请于{}后登陆.'.format(time_tmp_1))
                            break
                    else:
                        print('管理员登陆成功')
                while True:
                    action = input('输入动作：').strip()
                    if action == '1':
                        list()
                    if action == '2':
                        add()
                    if action == '3':
                        select()
                    if action == '4':
                        delete()
                    if action == '5':
                        update()
                    if action == 'exit':
                        flag = False
                        break
            else:
                cunt += 1
                print('用户名密码错误,还有{}次机会'.format(3-cunt))
                if cunt == 3:
                    print('账户锁定，将于24小时后解锁')
                    time1 = datetime.datetime.now()
                    time2 = time1.strftime("%Y-%m-%d %H:%M:%S")
                    time3 = time1 + datetime.timedelta(days=1)
                    time4 = time3.strftime('%Y-%m-%d %H:%M:%S')
                    time5 = time2 + ',' + time4
                    print(time4)
                    with open('lock.txt', 'w') as f:
                        f.write(time5)
        except Exception as e:
             print('{}'.format(e))
        finally:
            print('有报错信息')

if __name__ == '__main__':
    log_in()