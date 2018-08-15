### 演示
```
请输入登录名:a
请输入密码:a
用户名或密码错误，还有2次机会
请输入登录名:admin
请输入密码:1
请输入关键字(list,add,delete,update,find,exit): list
---------------------用户信息-------------------------
id       name        tel             address 
1 	 	 wyw1 	 	 132xxx 	 	 beijing 	 	 
2 	 	 wyw2 	 	 132xxx 	 	 shenyang 	 	 
5 	 	 wyw3 	 	 132xxx 	 	 shanghai 	 	 
6 	 	 wyw5 	 	 132xxx 	 	 shanghai 	 	 
请输入关键字(list,add,delete,update,find,exit): add
请输入： name tel address 用空格分隔 :www 1333 shenyang
用户已添加
请输入关键字(list,add,delete,update,find,exit): list
---------------------用户信息-------------------------
id       name        tel             address 
1 	 	 wyw1 	 	 132xxx 	 	 beijing 	 	 
2 	 	 wyw2 	 	 132xxx 	 	 shenyang 	 	 
5 	 	 wyw3 	 	 132xxx 	 	 shanghai 	 	 
6 	 	 wyw5 	 	 132xxx 	 	 shanghai 	 	 
7 	 	 www 	 	 1333 	 	 shenyang 	 	 
请输入关键字(list,add,delete,update,find,exit): delete
输入要删除的行id:2
用户已删除
请输入关键字(list,add,delete,update,find,exit): list
---------------------用户信息-------------------------
id       name        tel             address 
1 	 	 wyw1 	 	 132xxx 	 	 beijing 	 	 
5 	 	 wyw3 	 	 132xxx 	 	 shanghai 	 	 
6 	 	 wyw5 	 	 132xxx 	 	 shanghai 	 	 
7 	 	 www 	 	 1333 	 	 shenyang 	 	 
请输入关键字(list,add,delete,update,find,exit): update
请输入关键字查找 :shanghai
---------------------用户信息-------------------------
id       name        tel             address 
5 	 	 wyw3 	 	 132xxx 	 	 shanghai 	 	 
6 	 	 wyw5 	 	 132xxx 	 	 shanghai 	 	 
请输入要修改的行id :5
请输入新信息： name tel address 用空格分隔 :aa 66666 ddd
用户已更新
请输入关键字(list,add,delete,update,find,exit): find 66666
关键字输入错误
请输入关键字(list,add,delete,update,find,exit): find
请输入： 查找关键字 :66666
['5', 'aa', '66666', 'ddd']
请输入关键字(list,add,delete,update,find,exit): list
---------------------用户信息-------------------------
id       name        tel             address 
1 	 	 wyw1 	 	 132xxx 	 	 beijing 	 	 
5 	 	 aa 	 	 66666 	 	 ddd 	 	 
6 	 	 wyw5 	 	 132xxx 	 	 shanghai 	 	 
7 	 	 www 	 	 1333 	 	 shenyang 	 
```

