## 用户管理系统V2

- 数据结构
```
第一版数据结构：
[
	['', '', '', '', ''],
	['', '', '', '', ''],
	['', '', '', '', ''],
]
第二版数据结构：
[
	{'name' : 'monkey1', 'age':20, 'tel':'132xxx', 'address':'beijing'},
	{'name' : 'monkey2', 'age':20, 'tel':'132xxx', 'address':'beijing'},
	{'name' : 'monkey3', 'age':20, 'tel':'132xxx', 'address':'beijing'},
]

```
- 分页
```
分页示例：
page=1&page_size=10
page=2&page_size=10
page=3&page_size=10


提示：
list 1 10
list 2 10
list 3 10
```
- 持久化
```
import json

# write
fd = open('persistence.db', 'w')
membuf = json.dumps(xxxxx) ### xxxxx是用户列表
fd.write(membuf)
fd.close()

# read
fd = open('persistence.db', 'r')
data = fd.read()
membuf = json.loads(data)
fd.close()
```
- 异常处理
```
try:
    pass
except:
    pass
else:
    pass
finally:
	pass
```
