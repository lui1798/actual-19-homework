from django.db import models

class Users(models.Model):
    SEX_CHOICE = (
    (0,'男'),
    (1,'女'),
    )
    name = models.CharField(max_length=20,verbose_name='姓名')
    sex = models.IntegerField(choices=SEX_CHOICE,verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    city = models.CharField(max_length=50,verbose_name='地址')
    creat_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'users'
