'''userinfo = [
    [1, 'monkey2', 20, '132xxx', 'beijing'],
    [2, 'monkey1', 20, '132xxx', 'beijing'],
    [3, 'monkey4', 20, '132xxx', 'shanghai'],
    [4, 'monkey7', 20, '132xxx', 'beijing'],
]
'''

userinfo=[]
logininfo=('admin','51reboot')
trycount=3
while trycount>0:
    username=input('请输入账号：')
    password=input('请输入密码：')
    if username==logininfo[0] and password==logininfo[1]:
        while True:
         op=input('input op:')
         if op=='add':
                # name=input('请输入用户姓名：')
                # age=input('请输入用户年龄：')
                # tel=input('请输入电话号码：')
                # city=input('请输入城市：')
                # user=[name,age,tel,city]
                info=input('请输入用户信息')
                user=info.split(" ")
                if len(userinfo)==0:
                    user.insert(0,1)
                    userinfo.append(user)
                else:
                    userid=[ x[0] for x in userinfo]
                    newid=max(userid)+1
                    user.insert(0,newid)
                    userinfo.append(user)
         elif op=='delete':
                userid=input('please input userid：')
                for x in userinfo:
                    if x[0]==userid:
                        userinfo.remove(x)
                    else:
                        print('userid not in range')
         elif op=='update':
                userid = input('please input userid：')
                for x in userinfo:
                    if x[0] == userid:
                        y=int(input("请输入修改元素ID"))
                        if y in  len(x):
                            n=input('请输入修改内容')
                            x[y]=n
                        else:
                            print('没有对应修改项')
         elif op=='list':
                print(userinfo)
         elif op=='find':
                finduser=input("请输入查询用户姓名：")
                for x in userinfo:
                    if x[1]==finduser:
                        print(x)
                    else:
                        print('没有该用户')
         elif op=='exit':
                print('退出操作')
                break
    else:
        print('请你输入正确的账号密码')
    trycount-=1
else:
    print('你已错误输入三次，请稍后再登')