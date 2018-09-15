#encoding: utf-8
#-----导入内置模块--------
import json
#-----导入开源模块--------
import xlwt
import logging
import configparser
#-----导入自定义模块--------


#-----定义公用常量-------
#系统日志配置选项
LOG_LEVEL = logging.CRITICAL
LOG_FORMAT = '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s'
LOG_FILEMODE = 'a'
LOG_ENCODING = 'utf-8'

#-----定义公用变量-------



#--------定义功能函数-------
''' 读小文件'''
def ReadFile(filename):
    fhandler = open(filename, 'at+')
    fhandler.seek(0)
    cxt = fhandler.read()
    fhandler.close()
    return cxt

''' 写文件'''
def WriteFile(filename, data):
    fhandler = open(filename, 'w')
    fhandler.write(json.dumps(data))
    fhandler.close()


''' 读ini文件'''
def ReadConfigFile(filename, section, key):
    config = configparser.ConfigParser()
    config.read(filename)

    if config.sections() == []:
        print('{0}未配置，请检查ini文件'.format(section))
    else:
        try:
            return config[section][key]
        except Exception as e:
            print('{0}文件路径不存在'.format(key))


'''MD5'''
def GenHashmd5(s):
    hash_md5 = hashlib.md5(s.encode('utf-8'))
    hash_string = hash_md5.hexdigest()

    return hash_string


'''导出Excel文件'''
def WriteExcel(filename, data):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    keys = ['id', 'name', 'age', 'tel', 'address']

    for x in range(len(keys)):
        booksheet.write(0, x, keys[x])

    for i in range(len(data)):
        for j in range(len(data[i])):
            booksheet.write(i+1, j, data[i][keys[j]])

    workbook.save(filename)

'''日志记录'''
#初始化log实例
LOG_FILENAME = ReadConfigFile('conf.ini', 'LOG', 'LOGFILE')
logger = logging.getLogger('log')
logger.setLevel(LOG_LEVEL)
fhandler = logging.FileHandler(LOG_FILENAME, encoding=LOG_ENCODING)
fhandler.setLevel(LOG_LEVEL)
fhandler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(fhandler)
'''def init_log():
    LOG_FILENAME = ReadConfigFile('conf.ini', 'LOG', 'LOGFILE')
    logger = logging.getLogger('log')
    logger.setLevel(LOG_LEVEL)
    fhandler = logging.FileHandler(LOG_FILENAME, encoding=LOG_ENCODING)
    fhandler.setLevel(LOG_LEVEL)
    fhandler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(fhandler)
    return logger'''
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
