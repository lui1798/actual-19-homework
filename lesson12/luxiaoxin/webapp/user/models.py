from django.db import models

class Users(models.Model):
    STATUS_CHOICES = (
        (0, '男'),
        (1, '女')
        )
    username = models.CharField(max_length=32, db_index=True, unique=True, verbose_name='用户名')
    sex = models.IntegerField(choices=STATUS_CHOICES, verbose_name="性别 0 | 1", default=0)
    age = models.IntegerField(verbose_name="年龄")
    city = models.CharField(max_length=32, verbose_name="城市", default='')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.username

    class Meta():
        db_table = 'user'
