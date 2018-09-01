#作业4


#执行情况如下：



请输入用户名:admin
请输入密码:51reboot

-----------------------------------
登录成功！本用户管理系统可以执行以下操作：
    1. 添加用户(add)
    2. 删除用户(delete)
    3. 更新用户(update)
    4. 查询用户(list)
    5. 按关键字搜索用户(find)
    6. 退出登录（exit）
-----------------------------------

请输入操作方式(add/delete/update/list/query/exit) :list
第 1 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         1|      wang|   28|            132|             tianjin
         3|     zhang|   23|            152|             beijing
         2|      zhao|   25|            153|               hebei
         4|     wang1|   26|            134|             beijing
         5|     wang2|   27|            154|               anhui
请输入up或down进行翻页,也可以选择exit退出翻页：down
第 2 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         6|     wang3|   29|            134|               henan
请输入up或down进行翻页,也可以选择exit退出翻页：add
输入错误！
第 2 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         6|     wang3|   29|            134|               henan
请输入up或down进行翻页,也可以选择exit退出翻页：exit
请输入操作方式(add/delete/update/list/query/exit) :add
请输入用户信息(格式name age tel address):wql 24 137 beijing
添加成功，可以通过list查看！
请输入操作方式(add/delete/update/list/query/exit) :list
第 1 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         1|      wang|   28|            132|             tianjin
         3|     zhang|   23|            152|             beijing
         2|      zhao|   25|            153|               hebei
         4|     wang1|   26|            134|             beijing
         5|     wang2|   27|            154|               anhui
请输入up或down进行翻页,也可以选择exit退出翻页：down
第 2 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         6|     wang3|   29|            134|               henan
         7|       wql|   24|            137|             beijing
请输入up或down进行翻页,也可以选择exit退出翻页：delete
输入错误！
第 2 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         6|     wang3|   29|            134|               henan
         7|       wql|   24|            137|             beijing
请输入up或down进行翻页,也可以选择exit退出翻页：exit
请输入操作方式(add/delete/update/list/query/exit) :delete
请输入用户ID:7
请输入操作方式(add/delete/update/list/query/exit) :list
第 1 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         1|      wang|   28|            132|             tianjin
         3|     zhang|   23|            152|             beijing
         2|      zhao|   25|            153|               hebei
         4|     wang1|   26|            134|             beijing
         5|     wang2|   27|            154|               anhui
请输入up或down进行翻页,也可以选择exit退出翻页：down
第 2 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         6|     wang3|   29|            134|               henan
请输入up或down进行翻页,也可以选择exit退出翻页：exit
请输入操作方式(add/delete/update/list/query/exit) :query
请输入要查找的内容：wang2
第1页，共1页：
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         5|     wang2|   27|            154|               anhui
请输入操作方式(add/delete/update/list/query/exit) :update
请输入要更新的用户ID：5
要更新的内容：{'userid': 5, 'name': 'wang2', 'age': '27', 'tel': '154', 'address': 'anhui'}
请输入要更新的内容（格式name age tel address)，以空格分割：wang22 25 126 tianjin
更新用户成功！
请输入操作方式(add/delete/update/list/query/exit) :list
第 1 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         1|      wang|   28|            132|             tianjin
         3|     zhang|   23|            152|             beijing
         2|      zhao|   25|            153|               hebei
         4|     wang1|   26|            134|             beijing
         6|     wang3|   29|            134|               henan
请输入up或down进行翻页,也可以选择exit退出翻页：down
第 2 页 ， 共 2 页 
    userid|      name|  age|            tel|             address
----------------------------------------------------------------
         5|    wang22|   25|            126|             tianjin
请输入up或down进行翻页,也可以选择exit退出翻页：exit
请输入操作方式(add/delete/update/list/query/exit) :exit
程序退出，自动保存用户！
请输入用户名:admin
请输入密码:
登录失败，请重新输入!
请输入用户名:admin
请输入密码:
登录失败，请重新输入!
请输入用户名:admin
请输入密码:
失败3次，用户锁定！
请输入用户名:admin
请输入密码:
用户已锁定,请稍后再试
请输入用户名:er
请输入密码:
此账户不存在，请检查输入或选择退出！
输入yes选择退出：yes

Process finished with exit code 0