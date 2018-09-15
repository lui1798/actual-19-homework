import db
import file
import xlwt

user_keys = ['id', 'name', 'age', 'tel', 'addr']

def WriteExcel(filename,data):

    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

    for x in range(len(user_keys)):
        booksheet.write(0, x, user_keys[x])

    for i in range(len(data)):
        for j in range(len(data[i])):
            booksheet.write(i+1, j, data[i][user_keys[j]])

    workbook.save(filename)
