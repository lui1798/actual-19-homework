from django.db import models

# Create your models here.


class Student(models.Model):
	'''
		DateTimeField auto_now 无论是你添加还是修改对象，时间为你添加或者修改的时间。
		DateTimeField auto_now_add 为添加时的时间，更新对象时不会有变动。
		https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
	'''
	name            =   models.CharField(max_length=32, verbose_name="名称")
	sex             =   models.IntegerField(verbose_name="性别")
	age             =   models.IntegerField(verbose_name="年龄")
	email           =   models.EmailField(verbose_name="邮箱")
	tel             =   models.CharField(max_length=11, verbose_name="手机号")
	desc            =   models.TextField(verbose_name="个人介绍")
	create_time     =   models.DateTimeField(editable=False)
	update_time     =   models.DateTimeField()
	
	def __str__(self):
		return self.name
	
	class Meta:
		db_table = 'student'