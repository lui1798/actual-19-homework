## 第四次作业

用户管理系统实现功能：
1，判断用户是否被锁定
2，用户登录：用户名密码输入正确，可进入用户管理系统；
3，进入用户管理系统后，可进行：
 - add:添加用户信息；
 - delete：删除用户信息；
 - update：更新用户信息；
 - list：搜索相关信息列表；
 - save：保存用户信息
 - exit：退出用户系统
4，用户登录时，密码连续输错三次后锁定，24h后解锁



### 登录系统密码:

user:admin

password:admin

### 用户管理信息通过user_message.txt加载

user_message.txt初始信息如下:

userinfo = [{"id": 1, "name": "zs", "tel": 18312000000, "address": "hebei", "age": 25},
         {"id": 2, "name": "ls", "tel": 18909090902, "address": "beijing", "age": 35},
         {"id": 3, "name": "wu", "tel": 15869545120, "address": "shanxi", "age": 28},
         {"id": 4, "name": "zz", "tel": 15869545000, "address": "zhengzhou", "age": 18},
         {"id": 5, "name": "zq", "tel": 12220000220, "address": "luoyang", "age": 24},
         {"id": 6, "name": "p1", "tel": 12220000210, "address": "luoyang", "age": 39},
         {"id": 7, "name": "p2", "tel": 12220000230, "address": "luoyang", "age": 39},
         {"id": 8, "name": "p3", "tel": 12220000240, "address": "luoyang", "age": 39},
         {"id": 9, "name": "p4", "tel": 12220000250, "address": "luoyang", "age": 39},
         {"id": 10, "name": "p5", "tel": 12220000260, "address": "luoyang", "age": 39},
         {"id": 11, "name": "p7", "tel": 12220000270, "address": "luoyang", "age": 39},
         {"id": 12, "name": "p8", "tel": 13300000000, "address": "luoyang", "age": 39}]

