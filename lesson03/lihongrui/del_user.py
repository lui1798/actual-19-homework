users=[
    {'name':'monkey1','age':20,'tel':'133','address':'xxx','id':1},
    {'name':'monkey2','age':20,'tel':'133','address':'xxx','id':2},
    {'name':'monkey3','age':20,'tel':'133','address':'xxx','id':3}
]
text= input("请输入要删除用户的id")
if text.isdigit():
    uid=int(text)
    for user in users:
        if uid == user.get("id"):
            users.remove(user)
            print("删除用户成功")
            break
        else:
            print("输入id错误")
    else:
        print("输入id错误")

print("删除成功")