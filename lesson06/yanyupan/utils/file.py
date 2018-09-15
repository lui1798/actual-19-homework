import configparser
import xlwt


# 读取配置文件信息函数
def ReadConfig(filename, section):
    config = configparser.ConfigParser()
    config.read(filename)
    options_dict = {}
    try:
        options = config.options(section)
    except Exception as e:
        return False
    for option in options:
        options_dict.setdefault(option, config.get(section, option))

    return options_dict, True


# 读文件函数
def Read_File(fname):
    data = ''
    try:
        with open(fname, 'r') as f:
            data = f.read()
    except Exception as e:
        pass
    return data


# 写文件函数，参数：fname文件参数/data写入的数据/ser是否进行系列化
def Write_File(fname, data, ser):
    with open(fname, 'w') as f:
        if ser == "json":
            f.write(json.dumps(data))
        else:
            print(data)
            f.write(data)


# 设置表格样式
def Set_Style(name='Courier New', fcolor=4, height=200, bold=False, bgcolor=1):
    style = xlwt.XFStyle()  # 初始化样式

    # 设置字体
    font = xlwt.Font()
    font.name = name
    font.height = height
    font.bold = bold
    font.color_index = fcolor

    # 设置边框
    borders = xlwt.Borders()
    '''
        边框线：
        May be: 
        NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED,
        THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.

        DASHED虚线
        NO_LINE没有
        THIN实线 
    '''
    borders.left = xlwt.Borders.DASHED
    borders.right = xlwt.Borders.DASHED
    borders.top = xlwt.Borders.DASHED
    borders.bottom = xlwt.Borders.DASHED

    # 设置居中
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_LEFT  # 水平方向
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直方向

    # 设置背景颜色
    pattern = xlwt.Pattern()
    '''
        # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    '''
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    '''
        背景颜色:
        May be: 8 through 63. 
        0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 
        7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 
        20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
    '''
    pattern.pattern_fore_colour = bgcolor

    style.font = font
    style.borders = borders
    style.alignment = alignment
    style.pattern = pattern

    return style


# 获取字符串长度，一个中文的长度为2
def Len_Byte(value):
    length = len(value)
    utf8_length = len(value.encode('utf-8'))
    length = (utf8_length - length) / 2 + length
    return int(length)


# 写Excel


def Write_Excel(filename, data):
    # 表格头及数据内容部分样式
    title_sty = Set_Style(bold=True, bgcolor=22)
    content_sty = Set_Style(bgcolor=1)

    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

    keys = ['id', 'username', 'age', 'tel', 'address']
    data = [dict(zip(keys, x)) for x in data]

    # 确定头部各列宽度
    title_width = []
    for i in range(len(keys)):
        title_width.append(Len_Byte(keys[i]))

    # 确定数据部分各列宽度
    content_width = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i == 0:
                content_width.append(Len_Byte(str(data[i][keys[j]])))
            else:
                if content_width[j] < Len_Byte(str(data[i][keys[j]])):
                    content_width[j] = Len_Byte(str(data[i][keys[j]]))

    # 表格头每列宽与数据部分列宽比对，较长的为列宽
    for i in range(len(title_width)):
        if title_width[i] > content_width[i]:
            content_width[i] = title_width[i]

    # 设置宽度，在原宽度上再加4字节加以分隔
    for i in range(len(content_width)):
        if content_width[i] > 0:
            booksheet.col(i).width = 256 * (content_width[i] + 4)

    # 表格头部内容
    for x in range(len(keys)):
        booksheet.write(0, x, label=keys[x], style=title_sty)

    # 表格数据内容
    for i in range(len(data)):
        for j in range(len(data[i])):
            booksheet.write(i + 1, j, label=data[i][keys[j]], style=content_sty)

    workbook.save(filename)

