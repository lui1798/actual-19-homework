user = []
USER_INFO_NUM = 4

text = input("请输入用户名，年龄，电话，地址,用空格分隔 ")
users = text.split()

if len(user) != USER_INFO_NUM:
    print("输入数据正确")
else:
    name,tel,age,address= users
    ha_error = False
    if not age.isdigit():
        print("年龄格式不对")
        ha_error = True

    if not tel.isdigit():
        print("电话号码格式不对")
        ha_error = True

    if not ha_error:
        uid = max([x.get("id") for x in users] + [0]) + 1
        users.append({"id": uid, "name": name, "age": int(age), "tel": tel,"address": address})
        print("添加用户成功")
        print(users)
