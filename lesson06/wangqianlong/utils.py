'''
工具函数
'''
import configparser
import json
import xlwt

'读小文件'


def ReadFile(filename):
    fd = open(filename, 'r')
    cxt = fd.read()
    djson = json.loads(cxt)
    # print(cxt)
    fd.close()
    return djson


'写文件'


def WriteFile(filename, data):
    fd = open(filename, "w")
    djson = json.dumps(data)
    fd.write(djson)
    fd.close()


'读ini文件'


def ReadConfigFile(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return 'config is empty.', False

    if not key:
        return config.items(section), True
    else:
        return config[section][key], True


'对str生成hash MD5'


def GenHashmd5(s):
    pass


'写excle'


def WriteExcel(filename, data):
    '''
    :param filename:
    :param data: =[
            {'id': 1, 'name': 'monkey1', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
            {'id': 2, 'name': 'monkey2', 'age': 19, 'tel': '152xxx', 'address': 'beijing'}
        ]
    :return:
    '''

    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    keys = ['uid', 'name', 'age', 'tel', 'address']
    # 插入表头
    for x in range(len(keys)):
        booksheet.write(0, x, keys[x])
    # 插入数据
    for i in range(len(data)):
        for j in range(len(data[i])):
            booksheet.write(i + 1, j, data[i][keys[j]])
    try:
        workbook.save(filename)
    except Exception as e:
        print(e.args)
