#
# import io
# import csv342 as csv
#
# with io.open('mgt.xls', mode='wb') as csv_file:
#
#     # print(dir(csv))
#     csv.writer([1,'monkey1','18'])
#     # csv_reader = csv.reader(csv_file, delimiter=',')
#     #
#     # for row in csv_reader:
#     #     print('row {0:d}: data={1}'.format(csv_reader.line_num, row))
#         # pass


# import xlwt
#
# workbook = xlwt.Workbook(encoding='utf-8')
# booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
# # 存第一行cell(1,1)和cell(1,2)
#
# '''
#     x, y, v
#     x 表示第几行数
#     y 表示第几列
#     z 表示值
# '''
#
# booksheet.write(0, 0, 34)
# booksheet.write(0, 1, 38)
# # 存第二行cell(2,1)和cell(2,2)
# booksheet.write(1, 0, 36)
# booksheet.write(1, 1, 39)
# # 存一行数据
# rowdata = [43, 56]
# for i in range(len(rowdata)):
#     booksheet.write(2, i, rowdata[i])
# workbook.save('test_xlwt.xls')

import xlwt

def WriteExcel(filename, data):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

    '''
        写入到excel的逻辑
        data = [
            {'id': 1, 'name': 'monkey1', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
            {'id': 2, 'name': 'monkey2', 'age': 19, 'tel': '152xxx', 'address': 'beijing'}
        ]
        
        0 0 1
        0 1 monkey1
        
        
    '''
    keys = ['id', 'name', 'age', 'tel', 'address']

    for x in range(len(keys)):
        booksheet.write(0, x, keys[x])

    for i in range(len(data)):
        for j in range(len(data[i])):
            # print(i, j, data[i].get('id'), data[i].get('name'), data[i].get('age'), data[i].get('address'))
            # print(i, j, data[i][keys[j]])
            booksheet.write(i+1, j, data[i][keys[j]])

    workbook.save(filename)






data = [{'id': 1, 'name': 'monkey1', 'age': 18, 'tel': '132xxx', 'address': 'beijing'},
        {'id': 2, 'name': 'monkey2', 'age': 19, 'tel': '152xxx', 'address': 'beijing'}
    ]

WriteExcel('mgt1.xls', data)