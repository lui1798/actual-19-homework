import json
import logging
import configparser

def ReadConfigFile(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return False

    if not key:
        return config[section]
    else:
        return config[section][key]


'''读文件'''
def ReadFile():
    try:
        fd = open('user.txt')
        user_info1 = fd.read()
        user_list = json.loads(user_info1)
        return user_list
    except:
        print('\033[31m读取用户数据异常\033[0m')
        logging.error('读取用户数据异常')
    finally:
        fd.close()


'''写文件'''
def WriteFile(filename,user_list):
    try:
        user_info = json.dumps(user_list)
        fd=open(filename,'w')
        fd.write(user_info)
    except:
        print('\033[31m保存用户数据异常\033[0m')
        logging.error('保存用户数据异常')
    finally:
        fd.close()


def WriteLog():

    logfile = ReadConfigFile('config.ini', 'LOG', 'LOGFILE')
    logging.basicConfig(level=logging.DEBUG,
        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
        filename=logfile,
        filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)