'''
重置锁定时间：
用户或密码三次输入错误后，系统将锁定一天后才可进入系统，此程序用于重置时间
'''
import json
import datetime

t3 =datetime.datetime.strptime("2000-01-01 00:00:00",'%Y-%m-%d %H:%M:%S')

f1 = open("timelog.db","w")
membu = json.dumps(t3.strftime('%Y-%m-%d %H:%M:%S'))
f1.write(membu)
f1.close()

