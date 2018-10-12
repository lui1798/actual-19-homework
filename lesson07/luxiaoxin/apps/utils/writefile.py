#encoding:utf-8
#-----导入内置模块--------
import json
#-----导入开源模块--------
#-----导入自定义模块--------
#-----定义公用常量-------
#-----定义公用变量-------
#--------定义功能函数-------

''' 写文件'''
def WriteFile(filename, data):
    fhandler = open(filename, 'w')
    fhandler.write(data)
    #fhandler.write(json.dumps(data))
    fhandler.close()
