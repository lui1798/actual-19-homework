#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : ReadLog.py
# @Author: ZhouGui
# @Date  : 2018/11/15
# @Description :
import os
import time
from django.test import TestCase

seek_file = "/tmp/log_seek.log"


def getFilePos():
    if not os.path.exists(seek_file):
        os.mknod(seek_file)
        FILE_POS = 0
    else:
        fd = open(seek_file, 'r')
        FILE_POS = int(fd.read())
    return FILE_POS


def writeFilePos(FILE_POS):
    with open(seek_file, 'w+')  as fd:
        fd.write(str(FILE_POS))
        fd.closed


def readFile(LOGFILE, FILE_POS):
    fd = open(LOGFILE, 'r')
    fd.seek(FILE_POS)
    for line in fd:
        print(line, end='')
        FILE_POS += len(line)
        time.sleep(1)
        writeFilePos(FILE_POS)
    fd.close()


def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOGFILE = os.path.join(BASE_DIR, "access.log")
    FILE_POS = getFilePos()
    readFile(LOGFILE, FILE_POS)


if __name__ == '__main__':
    main()
