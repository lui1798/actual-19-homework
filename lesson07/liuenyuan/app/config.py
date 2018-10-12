#!/usr/bin/env python3
import configparser
def readconfig(request):
    mysql= {}
    log = {}
    INI_FILE = "../config/config.ini"
    config  = configparser.ConfigParser()
    #没有这部啥都没有
    config.read(INI_FILE)
    if request == "mysql":
#    print(config.read(INI_FILE))
#    print(config.sections())
         mysql['host'] = config['MYSQL']['DBHOST']
         mysql['port'] = int(config['MYSQL']['DBPORT'])
         mysql['name'] = config['MYSQL']['DBNAME']
         mysql['user'] = config['MYSQL']['DBUSER']
         mysql['passwd'] = config['MYSQL']['DBPASSWD']
         return mysql
    elif request == 'log':
         log['logfile'] = config['LOG']['LOGFILE']
         return log
    else:
         return None

if __name__ == '__main__':
   a =  readconfig('log')
   b =  readconfig('mysql')
   print(a,b)
