import json
import pickle


'''
    r > text
    w > text
    a > text
    b > byte
'''


USER_FILE = "user.db"

data = {'name': 'monkey', 'tel': '132xxx'}

# json v1 序列化
'''
fd = open(USER_FILE, 'w')

djson = json.dumps(data)
fd.write(djson)

fd.close()


# json v1 反序列化
fd = open(USER_FILE, 'r') # file describe

data_str = fd.read()
djson = json.loads(data_str)
print(djson)

fd.close()
'''


# json v2 序列化
'''
fd = open(USER_FILE, 'w')

json.dump(data, fd)

fd.close()
'''
'''
# json v2 反序列化
fd = open(USER_FILE, 'r')

djson = json.load(fd)
print(djson)

fd.close()
'''

# pickle v1 序列化
'''
fd = open(USER_FILE, 'wb') # w text | b byte

bytes = pickle.dumps(data)
fd.write(bytes)

fd.close()
'''

'''
fd = open(USER_FILE, 'rb') # w text | b byte

data_s = fd.read()
djson = pickle.loads(data_s)
print(djson)

fd.close()
'''
'''
fd = open(USER_FILE, 'wb') # w text | b byte

pickle.dump(data, fd)

fd.close()
'''

fd = open(USER_FILE, 'rb') # w text | b byte

djson = pickle.load(fd)
print(djson)

fd.close()
