#encoding=UTF-8
#  import json
# import datetime
#
# userlist=[]
# try:
#     f=open("userbase.txt","r")
#     data=f.read()
#     userlist=json.loads(data)
#     f.close()
# except FileNotFoundError:
#     print("用户文件未打开")
#
# f=open("timelog.txt",'r')
# mm=f.read()
# t=json.load(mm)
# t0 = datetime.datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
# f.close()
#
# user=("admin","123")
# ctime=3
# tn=datetime.datetime.now()
#
# if tn <=t0:
#     print("用户处于锁定,24小时后重试")
#     exit()
#

import time
LOCK_FILE="lock"
lock_time=0
try:
    fhandler=open (LOCK_FILE,"r")
    cxt= fhandler.read()
    fhandler.close()
    lock_time=float(cxt) #转换成浮点
except Exception as e:
    pass
is_unlock=time.time()-lock_time >24*60*60
print(is_unlock)
