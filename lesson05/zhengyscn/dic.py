
dic = {}

# 写操作
dic['name'] = 'monkey'
print(dic)

# 读操作
print(dic['name'])
print(dic.get('name1', 'nil'))

# 合并dic
print(dic)
dic1 = {'tel' : '132xxx'}
dic2 = {'name' : '51reboot'}
dic.update(dic2)
print("dic>>> ", dic)


# 修改
print('------------update--------------------')
print(dic)
dic['name'] = '51reboot.com'
print(dic)

# 清空
print('------------clean--------------------')
# dic = []
dic.clear()
print(dic)

# 删除
print('------------delete--------------------')
dic = {'name': '51reboot', 'tel' : '132xxx'}
# dic.pop('name')
del dic['name']
print(dic)

# 获取所有的key|values
print('------------get keys|values--------------------')
dic = {'name': '51reboot', 'tel' : '132xxx', 'address' : 'beijing'}
keys = dic.keys()
values = dic.values()
print(keys)
print(values)

# items
print('------------items--------------------')
dic = {'name': '51reboot', 'tel' : '132xxx', 'address' : 'beijing'}
print(dic.items())

for k, v in dic.items(): # tuple 解包 [('', '', ''), ()]
    print(k, v)

# for k in dic:
#     print(k, dic[k])


# setdefault
# 如果没有获取到 就设置一个默认值





# exam1
print("---------------exam1-----------------------")
dic = {'name': '51reboot', 'tel' : '132xxx', 'address' : 'beijing'}
# dic = {'51reboot': 'name', '132xxx': 'tel', 'BEIJING': 'address'}

# ret_dic = {}
# for k, v in dic.items():
#     ret_dic[v] = k
# print(ret_dic)

# ret_dic = { v:k for k, v in dic.items() }
# print(ret_dic)

ret_dic = { v.upper():k for k, v in dic.items() }
print(ret_dic)