from django.db import models

# Create your models here.
class Users(models.Model):
    SEX_CHOICE = (
        ('0','男'),
        ('1', '女'),
    )
    username = models.CharField(max_length=32,db_index=True,unique=True,verbose_name='用户名')
    sex = models.CharField(max_length=32,choices=SEX_CHOICE,verbose_name='性别')
    city = models.CharField(max_length=32,verbose_name='城市')
    age = models.IntegerField(verbose_name='年龄')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    def __str__(self):
        return self.username
    class Meta:
        ordering = ['pk','username']


