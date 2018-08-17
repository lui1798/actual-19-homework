#!/bin/python
logininfo = ('admin','51reboot')
userFile = open('userInfo.txt','r')
'''
设计两个list，其中userInfoList存放用户信息，userIndexList存放用户编号
两个list同时操作，使得userIndexList.index(userIndex)的值等于相应编号的用户信息
在userInfoList中的索引，这样可以在删除、修改、查询的时候无需遍历userInfoList。
'''
userInfoList = [] #初始化
userIndexList = [] #初始化
'''
存储信息时，用户信息userInfo转换成str存入文件，读取时需要转换。
在读取之后，依据userInfoList的内容重新生成userIndexList
'''
for line in userFile:
  userInfoList.append(line.rstrip('\n').split(' '))
userFile.close()
if len(userInfoList) >0 :
  userIndexList = [int(x[0]) for x in userInfoList] #依据userInfoList内容生成userIndexList
count = 3

while True:
  print('输入用户名和密码: ')
  username = input('用户名: ')
  password = input('密码: ')
  if username == logininfo[0] and password == logininfo[1]:
    print('登陆成功!')
    while True:
      op = input('选择所需操作 1)添加  2)删除  3)修改  4)显示  5)查找  6)退出 :')
      if op == '1':
        body = input('输入用户信息: ')
        userInfo = body.split(' ')
        if len(userInfo) != 4: #简单判断下输入的信息长度是否满足需求
          print('信息输入有误')
          continue
        if len(userInfoList) == 0:
          userIndex = 1
        else:
          userIndex = max(userIndexList)+1
        userInfo.insert(0,str(userIndex))  
        userInfoList.append(userInfo)  #将用户信息添加到userInfoList中
        userIndexList.append(userIndex) #同时将用户编号添加到userIndexList中
        userFile = open('userInfo.txt','w') #添加成功后，立即写入文件
        for userInfo in userInfoList:
          userFile.writelines(' '.join(userInfo)+'\n')
        userFile.close()  #文件写入完成，关闭文件
        print('操作成功！')
      elif op == '2':
        print(userIndexList)
        userIndex = int(input('输入需要删除的编号: '))
        if userIndex in userIndexList:  #利用userIndexList简单判断一下用户编号是否存在
          deleteIndex = userIndexList.index(userIndex) #如果存在，则找到相应的位置索引
          del(userIndexList[deleteIndex]) #利用索引删除
          del(userInfoList[deleteIndex]) #同时删除userIndexList中的编号
          print('操作成功！')
        else:
          print('编号错误。')
      elif op == '3':
        print(userIndexList)
        userIndex = int(input('输入需要修改的编号: '))
        if userIndex in userIndexList:  #利用userIndexList简单判断一下用户编号是否存在
          body = input('输入用户信息: ')
          #if len(userInfo) != 4: #简单判断输入信息是否满足要求
            #print('信息输入有误')
            #continue
          userInfo = body.split(' ')
          if len(userInfo) != 4: #简单判断输入信息是否满足要求
            print('信息输入有误')
            continue
          userInfo.insert(0,str(userIndex)) #生成新的userInfo
          userInfoList[userIndexList.index(userIndex)] = userInfo #利用索引更新信息
          userFile = open('userInfo.txt','w') #成功后，立即写入文件
          for userInfo in userInfoList:
            userFile.writelines(' '.join(userInfo)+'\n')
          userFile.close()  #文件写入完成，关闭文件
          print('操作成功！')
        else:
          print('编号错误。')
      elif op == '5':
        print(userIndexList)
        userIndex = int(input('输入需要查找的编号：'))
        if userIndex in userIndexList:
          userInfo = userInfoList[userIndexList.index(userIndex)]
          print('编号      姓名            年龄  电话          城市          ')
          print('{}{}{}{}{}'.format(userInfo[0].ljust(10,' '),userInfo[1].ljust(16,' '),userInfo[2].ljust(6,' '),userInfo[3].ljust(16,' '),userInfo[4].ljust(16,' ')))
        else:
          print('编号错误。')
      elif op == '4':
        pages = (len(userInfoList)-1)//5 #设置每页显示5行信息，计算出需要使用多少页
        page = 0 #显示页，初始化显示第0页
        while True:
          print('编号      姓名            年龄  电话          城市          ')
          if page == pages: #最后一页的显示需要使用[page*5:]
            for userInfo in userInfoList[page*5:]:
              print('{}{}{}{}{}'.format(userInfo[0].ljust(10,' '),userInfo[1].ljust(16,' '),userInfo[2].ljust(6,' '),userInfo[3].ljust(16,' '),userInfo[4].ljust(16,' ')))
          else:
            for userInfo in userInfoList[page*5:page*5+5]: #非最后一页显示的方式
              print('{}{}{}{}{}'.format(userInfo[0].ljust(10,' '),userInfo[1].ljust(16,' '),userInfo[2].ljust(6,' '),userInfo[3].ljust(16,' '),userInfo[4].ljust(16,' ')))
          pageOp = input('翻页:1)上一页 2)下一页 0)退出: ')
          if pageOp == '1': #上一页，需要判断page == 0
            if page == 0:
              print('没有上一页了')
              continue
            else:
              page -= 1
          elif pageOp == '2': #下一页，需要判断page == pages
            if page == pages:
              print('没有下一页了')
              continue
            else:
              page += 1
          elif pageOp == '0':
            break
          else:
            continue
      elif op == '6':
        break
      else:
        continue
    break
  else:
    if count <= 1:
      break
    else:
      count -= 1
        
