import json
import datetime

userlist=[]
try:
    f=open("userbase.txt","r")
    data=f.read()
    userlist=json.loads(data)
    f.close()
except FileNotFoundError:
    print("用户文件未打开")

f=open("timelog.txt",'r')
mm=f.read()
t=json.load(mm)
t0 = datetime.datetime.strptime(t,"%Y-%m-%d %H:%M:%S")
f.close()

user=("admin","123")
ctime=3
tn=datetime.datetime.now()

if tn <=t0:
    print("用户处于锁定,24小时后重试")
    exit()

