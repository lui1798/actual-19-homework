#encoding:utf-8
#-----导入内置模块--------
#-----导入开源模块--------
import xlwt
#-----导入自定义模块--------
#-----定义公用常量-------
#-----定义公用变量-------
#--------定义功能函数-------

'''导出Excel文件'''
def WriteExcel(filename, data):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    keys = ['id', 'name', 'age', 'tel', 'address']

    for x in range(len(keys)):
        booksheet.write(0, x, keys[x])

    for i in range(len(data)):
        for j in range(len(data[i])):
            booksheet.write(i+1, j, data[i][keys[j]])

    workbook.save(filename)
