import prettytable as pt
## 按行添加数据
def clean(list_data):
    tb = pt.PrettyTable()
    tb.field_names = ["name", "server", "qq"]
    for i in list_data:
        tb.add_row([i[0],i[1], i[2]])
    return tb
if __name__ == '__main__' :
    a = clean([[1,2,3],[1,2,3],[1,2,3]])
    print(a)

