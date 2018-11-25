#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('LTAINsigoAE5dHg5', 'hgZQUTccmMd6AgHQaJvnhNobNYIhqJ', 'cn-hangzhou')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('ecs.aliyuncs.com')
request.set_method('POST')
request.set_version('2014-05-26')
request.set_action_name('DescribeRegions')

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))