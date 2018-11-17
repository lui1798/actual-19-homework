from django.db import models

# Create your models here

class Users(models.Model):
    SEX_CHOICE = (
        ('0', '男'),
        ('1', '女'),
    )
    username    = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='姓名')
    sex         = models.CharField(max_length=10, choices=SEX_CHOICE, verbose_name='性别')
    age         = models.CharField(max_length=100, verbose_name='年龄')
    city        = models.CharField(max_length=100, verbose_name='城市')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')


    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        ordering = ['pk', 'username']
