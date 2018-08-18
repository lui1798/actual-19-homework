#! /usr/bin/python
# -*- coding: utf-8 -*-
user = []
count = 0
admin = ['admin','admin123']
while count < 3:
  username = input('username please :')
  password = input('passwd please :')
  if username == admin[0] and password == admin[1]:
    print("\033[1;32m 欢迎登录！！\033[0m")
    while True:
      inputs = input('please [add|dele|update|lists|exit]')
      if inputs == 'add':
        op = input("please :")
        ushow = op.split(' ')
        if len(ushow) != 3:
          print("\033[31m输入错误，格式:Name Age City\033[0m")
        else:
          if len(user) == 0:
            ushow.insert(0,1)
            user.append(ushow)
            print(user)
          else:
            uid = user[-1][0]+1
            ushow.insert(0,uid)
            user.append(ushow)
            print(user)

      elif inputs == 'dele':
        dele_id = input('please id :')
        for x in user:
          flag = False
          if dele_id in str(x[0]):
            user.remove(x)
            flag = True
        if flag == True:
          print('操作成功')
          print(user)
        else:
          print('操作失败')
          print(user)
      elif inputs == 'update':
        information = input('please Name :')
        flag = False
        for x,y in enumerate(user):
          if information in y[1]:
            new_information = input('please Name Age City :')
            ushow = new_information.split(' ')
            uid = y[0]
            ushow.insert(0,uid)
            del user[x]
            user.insert(x,ushow)
            flag = True
            print(user)
        if flag == False:
          print('操作失败')
      elif inputs == 'lists':
        information = input('please Name :')
        flag = False
        for x,y in enumerate(user):
          if information in y[1]:
            flag = True
            print('name:{}\nage:{}\ncity:{}'.format(y[1],y[2],y[3]))
        if flag == False:
          print('操作失败')
      elif inputs == 'exit':
        print('感谢使用')
        exit()
  else:
    print('账号或密码输入错误')
    count += 1
else:
  print('三次机会用完啦')
