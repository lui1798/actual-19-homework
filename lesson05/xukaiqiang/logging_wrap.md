## python 装饰器

> 定义:
>> python装饰器就是用于拓展原来函数功能的一种函数，这个函数的特殊之处在于它的返回值也是一个函数，使用python装饰器的好处就是在不用更改原函数的代码前提下给函数增加新的功能.

###### 一般我们给一个老的函数增加功能,都是在修改原代码的基础上去做的,有了装饰器就可以在外部定义一个函数去增加原函数的功能.

## 如何写一个装饰器


#### 代码如下:

```
	def wrapper(f):   #wrapper 装饰器的名字,   f被装饰的函数
	    def inner(*args,**kwargs):
	    	#这里写被装饰之前要干的事
	        result = f(*args,**kwargs)
	        #这里写被装饰之后要干的事
	        return result
	    return inner
	@wrapper
	def func(a,b):
	    time.sleep(1)
	    print("我是装饰器")
	    return "我是一个固定装饰器"

```
首先定义wrapper,定义inner函数 retuer inner 之后是inner里面被装饰的函数,这个函数事wrapper传递过来的,如果带有返回值就result接受同时inner  里面return回去,如果有参数就带上*args **kwargs参数,这个参数也是innner传递过来的

以上来看装饰器就是闭包函数

###带参数的装饰器

```
	from functools import wraps
	def wrapper(func):  #func = holiday
	    @wraps(func)
	    def inner(*args,**kwargs):
	        print('在被装饰的函数执行之前做的事')
	        ret = func(*args,**kwargs)
	        print('在被装饰的函数执行之后做的事')
	        return ret
	    return inner

	@wrapper   #holiday = wrapper(holiday)
	def lalala(wra):
	    '''这是一个装饰器'''
	    print('我是:%s,'%wra)
	    return '好开心'

	print(lalala.__name__)
	print(lalala.__doc__)
	ret = lalala(3)   #inner
	print(ret)


```

@wrapper 解释:
lalala = wrapper(lalalla)
这时候调用lalala的时候就在调用inner

##lambda函数
lamba 函数
	来创建匿名函数
	lambda函数是匿名的
	lambda函数有输入和输出
	lambda函数一般功能简单

	```
	def multnum(x):
	    return x * 10

	print(multnum(3))      	#30
	multnum = lambda x:x*10  #等同于上面的函数  这个是lambda函数
	print(multnum(3))		#30
	```


	defname = lambda [x,y,z]:表达式   
	add =  lambda x:x+1
	print(add(10))


	lambda x, y: x*y；函数输入是x和y，输出是它们的积x*y
	lambda:None；函数没有输入参数，输出是None
	lambda *args: sum(args); 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
	lambda **kwargs: 1；输入是任意键值对参数，输出是1


	```
	求最大vlaue的key
	dict1 = {
	    "k1":"a",
	    "k2":"g",
	    "k3":"e",
	    "k4":"b"
	}

	print(max(dict1))			#k4
	def funkey(key):
	    return dict1[key]
	print(max(dict1,key=funkey))		#k2
	print(max(dict1,key=lambda key:dict1[key]))		#k2

	```


## logging模块

logging模块
```
	import logging

	logging.debug("i am debug message")
	logging.info("i am info message")
	logging.warning("i am waring message")
	logging.error("i am error message")
	logging.critical("i am critical message")
输出:
	WARNING:root:i am waring message
	ERROR:root:i am error message
	CRITICAL:root:i am critical message

```
	- basicConfig:  #无法解决中文乱码问题,且不能同时往文件和屏幕上输出
	LOG_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] [line:%(lineno)d] [%(pathname)s] [%(message)s] "#配置输出日志格式
	DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a' #配置输出时间的格式，注意月份和天数不要搞乱了  %a星期几
	logging.basicConfig(level=logging.DEBUG,
	                    format=LOG_FORMAT,
	                    datefmt = DATE_FORMAT ,
	                    filename=r"test.log" #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
	                    )
	logging.debug("i am debug message")
	logging.info("i am info message")
	logging.warning("i am waring message")
	logging.error("i am error message")
	logging.critical("i am critical message")


#### 日志对象

```
	logger = logging.getLogger()
	#文件操作符
	fh = logging.FileHandler('test.log',encoding='utf-8')
	#创建屏幕输出对象
	th = logging.StreamHandler()
	#日志格式
	formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] [line:%(lineno)d] [%(pathname)s] [%(message)s]")
	#文件操作和日志格式关联
	fh.setFormatter(formatter)
	#loger 对象和文件关联
	logger.addHandler(fh)
	#绑定屏幕输出
	logger.addHandler(th)

	logging.debug("i am debug message")
	logging.info("i am info message")
	logging.warning("i am waring message")
	logging.error("i am error message")
	logging.critical("我是 critical message")
```



