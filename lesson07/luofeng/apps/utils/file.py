import configparser
import json
import xlwt
import hashlib
import datetime
import os


# 读取配置文件信息函数
def ReadConfigFile(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return '配置错误，配置节点为空！', False

    if not config.has_section(section):
        return '配置错误，未找到该配置节点{}！'.format(section), False

    if not key:
        return dict(config.items(section)), True
    else:
        return dict(config[section][key]), True


# 读文件函数
def ReadFile(fname):
    try:
        with open(fname, 'r') as f:
            data = f.read()
    except Exception as e:
        return e.args, False
    return data, True


# 写文件函数，参数：fname文件参数/data写入的数据/ser是否进行系列化
def WriteFile(fname, data):
    try:
        with open(fname, 'w') as f:
            if isinstance(data, str):
                return f.write(data), True
            elif isinstance(data, int):
                return f.write(str(data)), True
            elif isinstance(data, list) or isinstance(data, dict):
                return f.write(json.dumps(data)), True
            else:
                return "错误，数据类型不匹配！", False
    except Exception as e:
        return e.args, False


# str生成hash md5
def hash(s):
    hash_md5 = hashlib.md5(s)
    return hash_md5.hexdigest()


'''
    生成Excel表格部分
'''
# 设置表格样式
def SetStyle(name='Courier New', fcolor=4, height=200, bold=False, bgcolor=1, datefmt=False):
    style = xlwt.XFStyle()  # 初始化样式

    # 设置单元格格式为日期格式
    if datefmt:
        style.num_format_str = 'YYYY-MM-DD h:mm:ss'

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
def LenByte(value):
    length = len(value)
    utf8_length = len(value.encode('utf-8'))
    length = (utf8_length - length) / 2 + length
    return int(length)


# 写Excel
def WriteExcel(filename, data):
    # 表格头及数据内容部分样式
    title_sty = SetStyle(bold=True, bgcolor=22)
    content_sty = SetStyle(bgcolor=1)
    date_sty = SetStyle(bgcolor=1, datefmt=True)

    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

    #[{'id': 1, 'name': 'yyp', 'age': 28, 'tel': '13333', 'address': 'beijing'},....]
    if isinstance(data, list):
        keys = list(data[0].keys())
        print(data)

        # 确定头部各列宽度
        title_width = []
        for i in range(len(keys)):
            title_width.append(LenByte(keys[i]))

        # 确定数据部分各列宽度
        content_width = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                if i == 0:
                    content_width.append(LenByte(str(data[i][keys[j]])))
                else:
                    if content_width[j] < LenByte(str(data[i][keys[j]])):
                        content_width[j] = LenByte(str(data[i][keys[j]]))

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
                if keys[j] == 'create_time' or keys[j] == 'update_time':
                    booksheet.write(i + 1, j, label=data[i][keys[j]], style=date_sty)
                else:
                    booksheet.write(i + 1, j, label=data[i][keys[j]], style=content_sty)

        workbook.save(filename)
        return '成功保存用户信息至xls文件！', True
    else:
        return '数据格式不匹配！', False
