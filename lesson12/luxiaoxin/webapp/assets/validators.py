#encoding:utf-8
from datetime import datetime
from .models import Assets


class Validator(object):
    @classmethod
    def is_integer(cls, value):
        try:
            int(value)
            return True
        except BaseException as e:
            return False

    @classmethod
    def valid_ip(cls, ipadress):
        try:
            ip_list = ipadress.split('.')
        except BaseException as e:
            return False
        if len(ip_list) != 4:
            return False
        for ip in ip_list:
            if not cls.is_integer(ip):
                return False
            elif int(ip) >= 255:
                return False
        return True


class AssetsValidator(Validator):
    @classmethod
    def valid_create(cls, params):
        is_valid = True
        asset = Assets()
        errors = {}

        asset.hostname = params.get('hostname', '').strip()

        if asset.hostname == '':
            is_valid = False
            errors['hostname'] = '主机名不能为空'
        elif len(Assets.objects.filter(hostname=asset.hostname)) > 0:
            is_valid = False
            errors['hostname'] = '主机名重复'

        asset.cpu_num = params.get('cpu_num', '1').strip()
        if not cls.is_integer(asset.cpu_num):
            errors['cpu_num'] = 'CPU核数格式错误'
            is_valid = False

        asset.cpu_model = params.get('cpu_model', '')
        if asset.cpu_model == '':
            is_valid = False
            errors['cpu_model'] = 'CPU型号不能为空'

        asset.mem_total = params.get('mem_total', '')
        if asset.mem_total == '':
            is_valid = False
            errors['mem_total'] = '内存容量不能为空'

        asset.disk = params.get('disk', '')
        asset.public_ip = params.get('public_ip', '')
        if asset.public_ip != '':
            if not cls.valid_ip(asset.public_ip):
                errors['public_ip'] = 'IP地址格式错误'
                is_valid = False

        asset.private_ip = params.get('private_ip', '')
        if asset.private_ip != '':
            if not cls.valid_ip(asset.private_ip):
                errors['private_ip'] = 'IP地址格式错误'
                is_valid = False

        asset.remote_ip = params.get('remote_ip', '')
        if asset.remote_ip != '':
            if not cls.valid_ip(asset.remote_ip):
                errors['remote_ip'] = 'IP地址格式错误'
                is_valid = False

        asset.status = params.get('status', '1')

        asset.service_line = params.get('service_line', '')

        asset.frame = params.get('frame', '')

        asset.op = params.get('op', '')
        if asset.op == '':
            is_valid = False
            errors['op'] = '负责人不能为空'
        asset.remark = params.get('remark', '')

        asset.create_time = datetime.now()
        asset.update_time = datetime.now()

        return is_valid, asset, errors



    @classmethod
    def valid_edit(cls, params):
        is_valid = True
        asset = None
        errors = {}

        print(params)
        try:
          asset = Assets.objects.get(pk = params.get('id', '').strip())
        except BaseException as e:
          errors['id'] = '主机信息不存在'
          is_valid = False
          return is_valid, asset, errors

        asset.public_ip = params.get('public_ip', '')
        if asset.public_ip != '':
            if not cls.valid_ip(asset.public_ip):
                errors['public_ip'] = 'IP地址格式错误'
                is_valid = False

        asset.private_ip = params.get('private_ip', '')
        if asset.private_ip != '':
            if not cls.valid_ip(asset.private_ip):
                errors['private_ip'] = 'IP地址格式错误'
                is_valid = False

        asset.remote_ip = params.get('remote_ip', '')
        if asset.remote_ip != '':
            if not cls.valid_ip(asset.remote_ip):
                errors['remote_ip'] = 'IP地址格式错误'
                is_valid = False

        asset.status = params.get('status', '1')

        asset.service_line = params.get('service_line', '')

        asset.frame = params.get('frame', '')

        asset.op = params.get('op', '')
        if asset.op == '':
            is_valid = False
            errors['op'] = '负责人不能为空'
        asset.remark = params.get('remark', '')

        asset.update_time = datetime.now()

        print(is_valid, asset, errors)
        return is_valid, asset, errors
