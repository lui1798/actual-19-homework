'''
工具函数
'''
import configparser
import json
import xlwt
import prettytable

'读小文件'


def ReadFile(filename):
    try:
        fd = open(filename, 'r')
        return fd.read(), True
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()


'写文件'


def WriteFile(filename, data):
    try:
        fd = open(filename, "w")
        if isinstance(data, int):
            return fd.write(str(data)), True
        elif isinstance(data, list) or isinstance(data, dict):
            return fd.write(json.dumps(data)), True
        else:
            return 'file isinstance(data) match failed.', False
    except Exception as e:
        return e.args, False
    finally:
        if 'fd' in locals():
            fd.close()


'读ini文件'


def ReadConfigFile(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return 'config is empty.', False
    if not config.has_section(section):
        return 'section {} not found.'.format(section), False
    if not key:
        return dict(config.items(section)), True
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

'输出table形式'


def PrintTable(data):
    '''
    type and isinstance?
    '''
    x = prettytable.PrettyTable()
    if isinstance(data, list):
        x.field_names = data[0].keys()  # keys -> list ['id', 'name', 'age', 'tel', 'adderss']
        for dicinfo in data:
            x.add_row(dicinfo.values())  # 每个元素的values 返回的列表
    elif isinstance(data, dict):
        x.field_names = data.keys()
        x.add_row(data.values())
    else:
        return '', False
    return x, True
