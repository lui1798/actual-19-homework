users=[
    {'name':'monkey1','age':20,'tel':'133','address':'xxx','id':1},
    {'name':'monkey2','age':20,'tel':'133','address':'xxx','id':2},
    {'name':'monkey3','age':20,'tel':'133','address':'xxx','id':3}
]
user_find = []
for user in users:
    if text == "" or user.get("name").find(text)c!=-1 or \
        user.get("tel").find(text) !=-1 or \
        user.get("address").find(text) !=-1:
        user_find.append(user)

users_find_count=len(user_find)
if users_find_count==0:
    print("无数据")
elif users_find_count <=PAGE_SIZE:
    print(users_find)
else:
    max_page=user_find_count //PAGE_SIZE
    if users_find_count %PAGE_SIZE:
        max_page+=1

    while True:
        text_page_num=input("共有{0}页，请输入查询页码（1——{0}）".format(max_page))
        if text_page_num.isdigit() and in(text_page_num) <=max_page:
            text_page_num=in(text_page_num)
            print(users_find[(page_num-1) * PAGE_SIZE:page_num*PAGE_SIZE])
        else:
            print("输入页码错误")
            break

