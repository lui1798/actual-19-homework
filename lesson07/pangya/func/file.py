'''导入模块'''
import json
import configparser
import xlwt
import hashlib

'''读文件'''


def ReadFile(filename):
    fd = open(filename, 'r')
    message_str = json.loads(fd.read())
    fd.close()
    return message_str


'''写文件'''


def WriteFile(filename, data):
    fd = open(filename, 'w')
    message = json.dumps(data)
    fd.write(message)
    fd.close()


'''读ini文件'''


def ReadConfigFile(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return 'config.ini文件为空.', False
    if not config.has_section(section):
        return 'section不存在'
    if not key:
        return dict(config.items(section)), True
    else:
        return config[section][key], True


if __name__ == '__main__':
    msg, ok = ReadConfigFile('config.ini', 'DB', 'LOCKFILE')
    print(msg)
    print(ok)

'''对str生成hash md5'''


def GenHashmd5(s):
    hash_md5 = hashlib.md5(s)
    return hash_md5.hexdigest()


'''写入Excel'''


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
