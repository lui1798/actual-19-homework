#!/bin/python

import json
import datetime

logininfo = ('admin','51reboot')
userInfoDict = {} #初始化
count = 3
retflag = False

try:   #尝试打开文件，如果没有文件则先创建文件
  fd = open('loginTime.txt')
except FileNotFoundError:
  fd = open('loginTime.txt','w+')
membuf = fd.read()
fd.close()
if len(membuf) == 0:
  pass
else:
  lastLoginTime = datetime.datetime.strptime(membuf,"%Y-%m-%d %H:%M:%S")
  if datetime.datetime.now() < lastLoginTime+datetime.timedelta(days=1):
    print('账号被锁,24小时之内无法登陆')
    exit()


while True:
  if retflag:
    break
  else:
    print('输入用户名和密码。')
    username = input('用户名: ')
    password = input('密码: ')
    if username == logininfo[0] and password == logininfo[1]:
      print('登陆成功!')
      fd = open('loginTime.txt','w') #成功后清空文件的内容
      fd.truncate()
      fd.close()

      #从用户信息文件中读入内容
      try:      #尝试打开文件，如果没有文件则先创建文件
        fd = open('userInfo.txt')
      except FileNotFoundError:
        fd = open('userInfo.txt','w+')
      membuf = fd.read()
      if len(membuf) == 0:
        pass
      else:
        userInfoDict = json.loads(membuf)
      fd.close()

      #用户信息操作
      while True:
        op = input('选择所需操作 1)添加  2)删除  3)修改  4)显示  5)查找  6)退出 :')
       
        #添加操作
        if op == '1':
          body = input('输入用户信息，以空格区分: ')
          indList = body.split(' ')  #先生成个人信息的list
          if len(indList) != 4: #简单判断下输入的信息长度是否满足需求
            print('信息输入有误')
            continue
          #判断本次添加的用户信息的key值
          if len(userInfoDict) == 0:
            userIndex = 1
          else:
            userIndex = int(max(userInfoDict.keys()))+1
          #生成本次个人信息的dict
          indDict = {}
          indDict['name'] = indList[0]
          indDict['age'] = indList[1]
          indDict['tel'] = indList[2]
          indDict['add'] = indList[3]
          #将个人信息的dict添加到userInfoDict中，并以userIndex作为key值
          userInfoDict[str(userIndex)] = indDict
          #添加成功后，立即写入文件
          fd = open('userInfo.txt','w')
          fd.write(json.dumps(userInfoDict))
          fd.close()  #文件写入完成，关闭文件
          print('操作成功！')
          

        #删除操作
        elif op == '2':
          userIndexList = userInfoDict.keys()
          print(userIndexList) #显示可操作的编号
          userIndex = input('输入需要删除的编号: ')
          if userIndex in userIndexList:  #利用userIndexList简单判断一下用户编号是否存在
            userInfoDict.pop(userIndex)
            print('操作成功！')
          else:
            print('编号错误。')
            #continue

        
        #修改操作
        elif op == '3':
          userIndexList = userInfoDict.keys()
          print(userIndexList)
          userIndex = input('输入需要修改的编号: ')
          if userIndex in userIndexList:  #利用userIndexList简单判断一下用户编号是否存在
            body = input('输入用户信息: ')
            indList = body.split(' ')
            if len(indList) != 4: #简单判断输入信息是否满足要求
              print('信息输入有误')
              continue
            indDict = {}
            indDict['name'] = indList[0]
            indDict['age'] = indList[1]
            indDict['tel'] = indList[2]
            indDict['add'] = indList[3]
            userInfoDict[userIndex] = indDict
            fd = open('userInfo.txt','w')
            fd.write(json.dumps(userInfoDict))
            fd.close()
            print('操作成功！')
          else:
            print('编号错误。')


        #查询操作
        elif op == '5':
          userIndexList = userInfoDict.keys()
          print(userIndexList)
          userIndex = input('输入需要查找的编号：')
          if userIndex in userIndexList:
            indDict = userInfoDict[userIndex]
            print('编号      姓名            年龄  电话          城市          ')
            print('{}{}{}{}{}'.format(userIndex.ljust(10,' '),indDict['name'].ljust(16,' '),indDict['age'].ljust(6,' '),indDict['tel'].ljust(16,' '),indDict['add'].ljust(16,' ')))
          else:
            print('编号错误。')

        
        #显示操作
        elif op == '4':
          userInfoList = [] #先将Dict转换成List，用于切片操作
          for key,val in userInfoDict.items():
            userInfoList.append((key,val)) #[('1',{'name':'aa','age':'13','tel':'122','add':'bj'}),......]
          pages = (len(userInfoList)-1)//5 #设置每页显示5行信息，计算出需要使用多少页
          page = 0 #显示页，初始化显示第0页
          while True:
            print('编号      姓名            年龄  电话          城市          ')
            for indInfo in userInfoList[page*5:page*5+5]:
              print('{}{}{}{}{}'.format(indInfo[0].ljust(10,' '),indInfo[1]['name'].ljust(16,' '),indInfo[1]['age'].ljust(6,' '),indInfo[1]['tel'].ljust(16,' '),indInfo[1]['add'].ljust(16,' ')))
            pageOp = input('翻页:1)上一页 2)下一页 0)退出: ')
            if pageOp == '1': #上一页，需要判断page == 0
              if page == 0:
                print('没有上一页了。')
                #continue
              else:
                page -= 1
            elif pageOp == '2': #下一页，需要判断page == pages
              if page == pages:
                print('没有下一页了。')
                #continue
              else:
                page += 1
            elif pageOp == '0':
              break
            else:
              pass


        elif op == '6':
          retflag = True
          break


        else:
          pass
    
    #break
    else:
      if count <= 1:
        fd = open('loginTime.txt','w')
        fd.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        fd.close()
        print('3次密码输入错误，账号锁定。')
        exit()
      else:
        count -= 1
        
