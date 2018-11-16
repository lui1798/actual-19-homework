#encoding:utf-8

def valid_userinfo(jsondata):
    is_valid = True
    errors = {}
    '''
    如果返回True， 表明验证成功， 否则验证失败；
    :param jsondata: json
    :return: str, bool
    '''
    if isinstance(jsondata, dict):
        for k, v in jsondata.items():
            if v == "":
                is_valid = False
                errors[k] = '{}不能为空值'.format(k)
                return errors, is_valid

        if 'sex' in jsondata:
            sex = jsondata.get('sex')
            if sex.isdigit() and sex in ['0', '1']:
                pass
            else:
                is_valid = False
                errors[k] = '性别属性错误！'
                return errors, is_valid
    return errors, is_valid
