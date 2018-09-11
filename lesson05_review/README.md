## Lesson05 Review

> 针对前五天复习， 笔记已上传；

> 这次复习，笔记我来为大家记， 平时还要大家自已做好上课笔记；

## 存在的问题以及目标
```
1. 思路。+ 2
2. 基础知识不扎实，平时写的少。 + 3


目标：
1. 从lesson1到lesson5 全面的复习；2.5
2. 针对大家的欠缺的知识点做练习和巩固；1.5
3. homework usersystem.py；3
```

### Lesson01
```
1. 环境的安装配置

	1) CentOS 6.8 + Python 3.6.4
	2) IDE PyCharm | vim
	3) pip
		ipython
		包管理工具
	4) virtualenv
		django
	

2. 交互式环境 | 脚本方式
	python | ipython
		做临时的代码测试， 如果符合预期，那就把代码拷贝下来；
		
	脚本方式
		持久存储
3. 变量
	变量名 = 值
		不能以数字开头
		区分大小写
		可以（大、小）字母、下划线、
		
		在内存里存的
		
		变量必须先定义，在使用， 否则就会抛出 NameError异常
4. 注释
	单行
	#	
	
	多行
	''' '''
	""" """
	
	" "
	' '
	
5. if判断
	条件 称为 表达式

	if 条件:
		加4个空格
		符合条件时、条件为真
	elif 条件: == else + if
		加4个空格
	else:
		加4个空格
		不符合条件时、条件为假
		
	-1 0 1 2 3
	非（0和None）之外都为true
	
	# 逻辑运算符
		and	与
		or 或
		not 非
6. 循环
	for
		遍历
		
		循环体对象
			range
			str
			123456 > 不可以
			True > 不可以
		
		for 变量 in 循环体对象:
			加4个空格
		else:
			pass
			
		如果for循环正常退出 就执行else语句， 反之不执行else语句
		正常退出 正常执行完成
			
		
	while
		无限循环、死循环
		
		while 条件:
			加4个空格
		break
			跳出当前循环
		continue
			结束本次循环、进入下次循环
			
	pass
		占位符
7. 数据类型
	str
		引号引起来的都叫字符串
		单引号、双引号
	int
		数字
	float
		小数点
	bool
		True
		False
		
8. 内置函数
	input
		等待用户输入
		返回类型是字符串类型
		
		input(prompt=None)	# 默认值参数
		
		?
		help
		
	type
		查看变量的类型
	print
		输出到控制台
			标准输出 stdout
	int
	str
	float
9. 四则运算
	+
	-
	*
	**
	/
	%
	//
	
		如果判断是一个数字是奇数还是偶数 就是通过 % 结果==0 就是偶数 否则就是奇数
	
10. 格式化
	%s -> string
		元组
		%s
	format
		.format
		{}
		索引
11. pass | break | continue
12. 内置模块
	random
		取随机数
		random.randint(1, 10)
		
		生成一个长度为10 的随机数
		
		1. 定义一个字符串
		2. for循环 10次
		3. random.randint(1, 9)
		4. 字符串拼接
		5. 拼接
		
		'5469223189'
	range
		生成一个偶数的字符串02468
	sys
		sys.version
	keyword
		查看关键字
		返回的类型是列表
13. 比较运算符
	==
	not
	!=
	>
	<
	>=
	<=
	
	if
	while
```