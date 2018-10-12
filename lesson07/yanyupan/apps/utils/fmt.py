import json

from prettytable import PrettyTable


def Println(data):
    print(json.dumps(data, indent=4))


def PrintTable(data):
    '''
    type and isinstance?
    '''
    x = PrettyTable()
    if isinstance(data, list):
        x.field_names = data[0].keys()  # keys -> list ['id', 'name', 'age', 'tel', 'adderss']
        for dicinfo in data:
            x.add_row(dicinfo.values())  # 每个元素的values 返回的列表
    elif isinstance(data, dict):
        x.field_names = data.keys()
        x.add_row(data.values())
    else:
        return '', False
    return x, True