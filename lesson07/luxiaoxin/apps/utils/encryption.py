#encoding:utf-8
#-----导入内置模块--------
#-----导入开源模块--------
#-----导入自定义模块--------
#-----定义公用常量-------
#-----定义公用变量-------
#--------定义功能函数-------

'''MD5'''
def GenHashmd5(s):
    hash_md5 = hashlib.md5(s.encode('utf-8'))
    hash_string = hash_md5.hexdigest()

    return hash_string
