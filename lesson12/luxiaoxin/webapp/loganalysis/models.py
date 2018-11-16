from django.db import models

# Create your models here.
class Log(models.Model):
    query_time = models.DateTimeField(auto_now_add=True, verbose_name='刷新时间')
    logname = models.CharField(max_length=64, db_index=True, verbose_name='日志名称')
    loglevel = models.CharField(max_length=128, verbose_name='日志等级', default='')
    count = models.IntegerField(verbose_name="日志数量", default=0)

    def __str__(self):
        return self.logname

    class Meta():
        db_table = 'log'
