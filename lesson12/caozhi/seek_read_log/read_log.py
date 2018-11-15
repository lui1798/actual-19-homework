# /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = caozhi
# create_time 2018-11-12,update_time 2018-11-14
# version = 1.0
# 录像高可用报警
# 1 读取日志 使用游标移动
# 2 线上业务日志文件会切割，切割后，读取上一个切割的日志

import os
import sys
import json
import requests
import time
import re

#CONF = {"seek": 0, "inode": 922817, "last_file": "/data/logs/lmrs/logstash.log"}
cini = '/root/conf.ini'
log_file = '/data/logs/lmrs/logstash.log'

def readconf():
    with open(cini, 'r+') as f:
        CONF = json.load(f)
    return CONF

def writeconf(CONF):
    with open(cini, 'w+') as e:
        json.dump(CONF, e)

def main(log_file, seek):
    f = open(log_file, 'r')
    f.seek(seek)
    line = f.readline()
    new_seek = f.tell()
    if new_seek == seek:
        print('没有追加日志，退出程序')
        sys.exit()
    while line:
        logstash = json.loads(line)
        #if '''re.search(time.strftime("%Y:%H:%M", time.localtime()), logstash.get('log_time')) and '''logstash.get('rtype') == 6 and logstash.get('uri') == '/publish' and logstash.get('event') == 0:
        if logstash.get('rtype') == 6 and logstash.get('uri') == '/publish' and logstash.get('event') == 0:
            value = 1
            stream = logstash.get('name')
            print('{}  {}'.format(value, stream))
            record(value=value, stream=stream)
        else:
            value = 0
            stream = 0
        line = f.readline()
    seek = f.tell()
    f.close
    return value, stream, seek

def record(value, stream):
    data = []
    record = {}
    record['metric'] = 'recording_high_availability_monitor'
    record['endpoint'] = os.uname()[1]
    record['timestamp'] = int(time.time())
    record['step'] = 60
    record['value'] = value
    record['Tags'] = '{}={}'.format(int(time.time()), stream)
    data.append(record)
    
    if data:
        print('这是data的json数据' + data)
        falcon_request = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(data))
        #falcon_request = requests.post("http://127.0.0.1:1988/v1/push", json=data)
        print('json参数请求返回状态码为：' + str(falcon_request.status_code))


if __name__ == '__main__':
    CONF = readconf()
    print('first_CONF :{}'.format(CONF))
    print('NO1.log_file',log_file)
    last_inode = CONF['inode']
    inode = os.stat(log_file).st_ino
    print('last_inode: {}  inode: {}'.format(last_inode, inode))

    if inode == last_inode:
        seek = CONF['seek']
        next_file = 0
    else:
        log_file = CONF['last_file'] + time.strftime("-%Y%m%d_", time.localtime()) + str(int(time.strftime("%k%M", time.localtime())))[:-1] + '0'
        next_file = 1
        seek = CONF['seek']

    print('NO2.log_file',log_file)
    value, stream, seek = main(log_file=log_file,seek=seek)

    if next_file:
        CONF['seek'] = 0
    else:
        CONF['seek'] = seek

    CONF['inode'] = os.stat('/data/logs/lmrs/logstash.log').st_ino
    writeconf(CONF=CONF)
    print('last_CONF :{}'.format(CONF))
