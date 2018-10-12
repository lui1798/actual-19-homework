from apps.utils.msg import *
from apps.utils import date
whereDic = InputMsg("请输入你要更改的用户信息[ 字段名1=字段值1, 字段名2=字段值2, ... ]: ")
update_time = 'from_unixtime({})'.format(date.CurrentTimestamp())
# whereDic = whereDic + ',update_time=from_unixtime({})'.format(date.CurrentTimestamp())
whereDic = whereDic + ',update_time=' + update_time
# whereDic = ','.join(["{}='{}'".format(x.split('=')[0].strip(), x.split('=')[1].strip()) for x in whereDic.split(',')])
print(whereDic)