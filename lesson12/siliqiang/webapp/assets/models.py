from django.db import models

# Create your models here

class Assets(models.Model):
    STATUS_CHOICE = (
        (0, '关机'),
        (1, '运行'),
    )
    hostname    = models.CharField(max_length=50, db_index=True, unique=True,verbose_name='主机名')
    cpu_num     = models.IntegerField(verbose_name='cpu核数',default='2')
    cpu_model   = models.CharField(max_length=100,verbose_name='cpu型号',default='Core i7')
    mem         = models.CharField(max_length=100,verbose_name='内存',default='2G')
    disk        = models.CharField(max_length=100, verbose_name='硬盘', default='2G')
    ip          = models.CharField(max_length=100, verbose_name='IP地址', default='192.168.1.1')
    op          = models.CharField(max_length=32, verbose_name='运维负责人', default='')
    system      = models.CharField(max_length=32, verbose_name='操作系统',default='')
    line        = models.CharField(max_length=32, verbose_name='所属业务线',default='')
    remark      = models.TextField(default='', null=True, verbose_name='备注')
    host_status = models.IntegerField(verbose_name='机器的状态0|1',default='')
    # host_status = models.IntegerField(choices=STATUS_CHOICE, verbose_name='机器的状态0|1')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')


    def __str__(self):
        return self.hostname

    class Meta:
        db_table = 'assets'
