#encoding:utf-8
#-----导入内置模块--------
#-----导入开源模块--------
#-----导入自定义模块--------
#-----定义公用常量-------
#-----定义公用变量-------
#--------定义功能函数-------

''' 读小文件'''
def ReadFile(filename):
    fhandler = open(filename, 'at+')
    fhandler.seek(0)
    cxt = fhandler.read()
    fhandler.close()
    return cxt
