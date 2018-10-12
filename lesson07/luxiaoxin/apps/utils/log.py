#encoding:utf-8
#-----导入内置模块--------
#-----导入开源模块--------
import logging
#-----导入自定义模块--------
from apps.utils.readconfig import ReadConfigFile
#-----定义公用常量-------
#系统日志配置选项
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s'
LOG_FILEMODE = 'a'
LOG_ENCODING = 'utf-8'
#-----定义公用变量-------
#--------定义功能函数-------

'''日志记录'''
#初始化log实例
LOG_FILENAME = ReadConfigFile('conf.ini', 'LOG', 'LOGFILE')
logger = logging.getLogger('log')
logger.setLevel(LOG_LEVEL)
fhandler = logging.FileHandler(LOG_FILENAME, encoding=LOG_ENCODING)
fhandler.setLevel(LOG_LEVEL)
fhandler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(fhandler)

#装修器函数，将操作日志保存到日志
def log_info(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "debug":
                logger.debug(*args, **kwargs)
            elif level == "warn":
                logger.warn(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 成功时提示信息
@log_info(level="debug")
def success_info(info):
    print('\033[32m{}\033[0m'.format(info))

# 错误或警告时提示信息
@log_info(level="warn")
def warn_info(info):
    print('\033[31m{}\033[0m'.format(info))

