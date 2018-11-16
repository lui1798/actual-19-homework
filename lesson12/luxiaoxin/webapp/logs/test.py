#encoding:utf-8
debug_num = 0
info_num = 0
warn_num = 0
error_num = 0
fhandle = open('django.log')
while True:
    line = fhandle.readline()
    print('start:{0},is blank:{1}'.format(line,line.strip()))
    if line != '':
        cell = line.strip().split()
        if len(cell) > 3 and cell[3] in ['[DEBUG]', '[INFO]', '[WARNING]', '[ERROR]']:
            if cell[3] == '[DEBUG]':
                debug_num += 1
            elif cell[3] == '[INFO]':
                info_num += 1
            elif cell[3] == '[WARNING]':
                warn_num += 1
            elif cell[3] == '[ERROR]':
                error_num += 1
    #pos = pos + len(line)
    print('last:{0}, is blank:{1}'.format(line,line.strip()))
    if line == '':
        print('break:{0},is blank:{1}'.format(line,line.strip()))
        break
fhandle.close()
