#coding=UTF-8
from django.db import models

# Create your models here.

class Assets(models.Model):
    STATUS_CHOICE = (
        (0,"下线"),
        (1,'在线')
    )

    host_name = models.CharField(max_length=50, db_index=True, unique=True, verbose_name="主机名")
    cpu_num = models.IntegerField(verbose_name="cpu核数")
    cpu_model = models.CharField(max_length=20, verbose_name="cpu型号")
    remark = models.TextField(default='', null=True, verbose_name="备注")
    mem_total = models.CharField(max_length=3, default="8G", verbose_name="内存")
    disk = models.CharField(max_length=4, verbose_name="磁盘大小")
    public_ip = models.CharField(max_length=32, default="", verbose_name="公网ip")
    private_ip = models.CharField(max_length=32, verbose_name="私有ip")
    remote_ip = models.CharField(max_length=32, default="", verbose_name="远程ip")
    op = models.CharField(max_length=32, default="", verbose_name="运维负责人")
    status = models.IntegerField(choices=STATUS_CHOICE,verbose_name="机器的状态0 | 1")
    os_system = models.CharField(max_length=32, verbose_name="操作系统")
    service_line = models.CharField(max_length=32, verbose_name="所属业务线")
    frame = models.CharField(max_length=32, verbose_name="机架")
    use_date = models.DateTimeField(auto_now_add=True,verbose_name='使用日期')
    update_date = models.DateTimeField(auto_now=True,verbose_name="更新日期")

    def __str__(self):
        return self.host_name

    class Meta:
        db_table = 'assets'

