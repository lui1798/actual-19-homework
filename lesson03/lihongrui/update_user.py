import json
users=[]
USER_INFO_NUM=4
text=input("请输入用户id")
is_exists=False
uid=0
if text.isdigit():
    uid=int(text)
    for user in users:
        if uid == users.get("id"):
            print("更新用户信息"+json.dumps(user))
            if_exists=True
            break

if is_exists:
    text=input("请输入用户信息")
    user=text.split()
    if len(user) !=USER_INFO_NUM:
        print("输入数据争取")
    else:
        name,age,tel,address= user
        has_error=False
        if not age.isdigit():
            has_error=True
            print("输入年龄不正确")

        if  not tel.isdigit():
            has_error=True
            print("输入年龄不正确")

        if not has_error:
            for user in users:
                if uid == user.get("id"):
                    user["name"]=name
                    user["age"]=age
                    user["tel"]=tel
                    user["address"]=address

                print("更新成功")
                break


                