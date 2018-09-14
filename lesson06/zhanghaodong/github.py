#!/usr/local/bin/python3
# mail:haodongz@yeah.net
# _*_ coding:utf-8 _*_ 
import requests
import json
git_tokens = '4a16bc935d2916e34293ecbc3fdcca1e6e11fa52'
headers = {'Authorization':'Token ' + git_tokens}
req = requests.get('https://api.github.com/user',headers=headers)
print(json.dumps(req.json(),indent=4))

