import os

# 获取当前文件的绝对路径
abspath = os.path.abspath(__file__)
print(abspath)

# 获取当前目录的上一级目录
workdir = os.path.dirname(os.path.dirname(abspath))
print(workdir)

# 拼接字符串
LOGFILE = os.path.join(workdir, 'ngxlog', 'mysqld.log')
print(LOGFILE)

# 判断文件是否存在 True | False
print(os.path.exists("/etc/passwd123"))
print(os.path.getsize("/etc/passwd"))

print(os.path.isfile("/etc/passwd"))
print(os.path.isdir("/etc/passwd"))
print(os.path.isdir("/etc/"))

print(os.stat('/etc/passwd'))

# print(os.path.curdir())
print(os.path.realpath('/usr/bin/python'))

print("----分割线-----")
print(os.getcwd())
os.chdir("/usr/local")
print(os.getcwd())