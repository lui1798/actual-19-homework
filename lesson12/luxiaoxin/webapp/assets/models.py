from django.db import models

# Create your models here.

class Assets(models.Model):
    STATUS_CHOICES = (
        (0, '关机'),
        (1, '运行')
        )
    hostname = models.CharField(max_length=64, db_index=True, unique=True, verbose_name='主机名')
    cpu_num = models.IntegerField(verbose_name='CPU核数', default=1)
    cpu_model = models.CharField(max_length=128, verbose_name='CPU型号', default='')
    mem_total = models.CharField(max_length=3, verbose_name="内存", default="8G")
    disk = models.CharField(max_length=4, verbose_name="磁盘大小", default='120G')
    public_ip = models.CharField(max_length=32, verbose_name="公网ip", default='')
    private_ip = models.CharField(max_length=32, verbose_name="私有ip", default='')
    remote_ip = models.CharField(max_length=32, verbose_name="远程ip", default='')
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name="机器的状态0 | 1", default=1)
    os_system = models.CharField(max_length=32, verbose_name="操作系统", default='')
    service_line = models.CharField(max_length=32, verbose_name="所属业务线", default='')
    frame = models.CharField(max_length=32, verbose_name="机架", default='')
    op = models.CharField(max_length=32, verbose_name="运维负责人", default='')
    remark = models.TextField(default='', null=True, verbose_name='备注')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.hostname

    class Meta():
        db_table = 'assets'

