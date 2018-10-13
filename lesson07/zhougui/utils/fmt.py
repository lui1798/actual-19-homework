#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @File  : fmt.py
# @Author: ZhouGui
# @Date  : 2018/10/11
# @Description : 格式化输出
import json
from prettytable import PrettyTable


def PrintTable(users):
    x = PrettyTable()
    if isinstance(users, list):
        x.field_names = users[0].keys()
        for listinfo in users:
            x.add_row(listinfo.values())
    elif isinstance(users, dict):
        x.field_names = users.keys()
        x.add_row(users.values())
    else:
        return '', False
    return x, True
