#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from os.path import getsize



def main(log_name, post, last_post, current_post):
    fo = open(log_name, "r")
    fo.seek(last_post, 0)
    warn_num = 0

    while last_post < current_post:
        line = fo.readline().strip()
        if line.split(" ")[2] == 'WARN':
            warn_num += 1
        last_post = fo.tell()
    fo.close()
    SetPost(post, current_post)
    print(warn_num)


def GetPost(filename):
    try:
        filegetpost = open(filename, 'r')
        last_post = filegetpost.read().strip()
        filegetpost.close()
        return last_post
    except:
        return 0

def SetPost(filename, current_post):
    filesetpost = open(filename, 'w')
    filesetpost.truncate()
    filesetpost.write(str(current_post))
    filesetpost.close()


if __name__ == '__main__':
    post = 'log.post'
    log_name = 'django.log'

    last_post = GetPost(post)
    current_post = getsize(log_name)

    main(log_name, post, int(last_post), current_post)