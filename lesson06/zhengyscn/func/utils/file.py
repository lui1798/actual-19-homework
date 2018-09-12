import configparser

'''
	工具函数
'''

'''读小文件'''


def ReadFile(filename):
    pass


'''写文件'''


def WriteFile(filename, data):
    pass


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
    pass


'''写Excel'''


def WriteExcel(filename, data):
    pass
