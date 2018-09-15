import hashlib
import configparser

import xlwt

'''
	工具函数
'''

'''读小文件'''


def ReadFile(filename):
    try:
        fd = open(filename, 'r')
        return fd.read(), True
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()


'''写文件'''


def WriteFile(filename, data):
    try:
        fd = open(filename, 'w')
        if isinstance(data, int):
            return fd.write(str(data)), True
        elif isinstance(data, list) or isinstance(data, dict):
            return fd.write(json.dumps(data)), True
        else:
            return "file isinstance(data) match failed.", False
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()


'''读ini文件'''


def ReadConfigFile(filename, section, key=None):
    '''
        Read ini file
    '''
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return 'config ini is empty.', False

    if not config.has_section(section):
        return 'section {} not found.'.format(section), False

    if not key:
        return config.items(section), True
    else:
        return config[section][key], True


'''对str生成hash md5'''


def GenHashmd5(s):
    hash_md5 = hashlib.md5(s)
    return hash_md5.hexdigest()


'''写Excel'''


def WriteExcel(filename, data):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    if isinstance(data, list):
        keys = list(data[0].keys())
  
        for x in range(len(keys)):
            booksheet.write(0, x, keys[x])

        for i in range(len(data)):
            for j in range(len(data[i])):
                booksheet.write(i + 1, j, data[i][keys[j]])
        
        workbook.save(filename)
        return '', True
    else:
        return 'match isinstance error.', False
