#encoding:utf-8
#-----导入内置模块--------
#-----导入开源模块--------
import configparser
#-----导入自定义模块--------
#-----定义公用常量-------
#-----定义公用变量-------
#--------定义功能函数-------

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

