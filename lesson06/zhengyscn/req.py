import requests
import json

# for x in dir(requests):
#     print(x)

TOKEN = "54dc14eaa2ff507420b837f2e9b75c14740fcbb1"
headers = {'Authorization': 'token ' + TOKEN}


# req = requests.get('https://api.github.com/user', params={'username' :'shouwz', 'password' : 'ma540051824'}, verify=False)
req = requests.get('https://api.github.com/user', headers=headers)
print(req)
print()

print(json.dumps(req.json(), indent=4))