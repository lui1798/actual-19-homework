from django.db import models

# Create your models here.
class Users(models.Model):
    GNEDER_CHOICE = [
        [0,'man'],
        [1,'woman']
    ]

    username = models.CharField(max_length=20,verbose_name='姓名')
    gender = models.IntegerField(choices=GNEDER_CHOICE,default=0,verbose_name='性别')
    id_card = models.CharField(max_length=18,verbose_name='身份证号')
    age = models.IntegerField(verbose_name='年龄')
    address = models.TextField(max_length=100,verbose_name='地址')
    remark = models.TextField(default='', null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True,verbose_name='修改日期')

    #用meta类来对数据库里的此表进行重全名
    class Meta:
        db_table = 'users'