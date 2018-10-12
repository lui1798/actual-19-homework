#encoding:utf-8
#-----导入内置模块--------
import time
#-----导入自定义模块--------
from apps.utils.readfile import ReadFile
from apps.utils.writefile import WriteFile
from apps.utils.readconfig import ReadConfigFile
from apps.utils.log import success_info,warn_info

#-----定义公用常量-------
#管理员登录锁定时长30s
LOCK_INTERVAL = 30


#--------定义功能函数-------
#检查是否被锁定函数
def is_unlock():
    lock_time = 0
    LOCK_FILE = ReadConfigFile('conf.ini', 'LOG', 'LOGFILE')

    try:
        cxt = ReadFile(LOCK_FILE)
        lock_time = float(cxt)
    except Exception as e:
        pass

    is_unlock = time.time() - lock_time > LOCK_INTERVAL

    if not is_unlock:
        warn_info('锁定用户尝试登录')

    return is_unlock


#锁定管理员账号
def lock_admin():
    lock_init_time = time.time()
    LOCK_FILE = ReadConfigFile('conf.ini', 'LOG', 'LOGFILE')
    WriteFile(LOCK_FILE,lock_init_time)
