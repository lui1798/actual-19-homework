from django.db import models
from django.utils.html import format_html

# Create your models here.

'''
choices=STATUS_CHOICE
STATUS_CHOICE = ((0,'关机'), (1,'开机'))
使可选项为2个
frame
1-2-3
表示第一个机房第2排第三个机架
'''

class Assets(models.Model):
    STATUS_CHOICE = ((0, '关机'), (1, '开机'))
    hostname = models.CharField(max_length=50, db_index=True, unique=True, verbose_name="主机名")  # 增加的一个字段
    cpu_num = models.IntegerField(null=True, blank=True,verbose_name="CPU核")  # 增加一个整型字段
    cpu_model = models.CharField(max_length=100, verbose_name="CPU型号")
    mem_total = models.CharField(max_length=3, default="8G", verbose_name="内存")
    disk= models.CharField(max_length=4, default="128G",verbose_name="磁盘大小")
    public_ip = models.CharField(max_length=32, default="", verbose_name="公网ip")
    private_ip = models.CharField(max_length=32,default="", verbose_name="私有ip")
    remote_ip = models.CharField(max_length=32, default="", verbose_name="远程ip")
    op = models.TextField(max_length=32,default="",null=True,verbose_name="运维负责人")
    status = models.IntegerField(choices=STATUS_CHOICE,verbose_name="机器状态",default="")
    os_system =models.CharField(max_length=32, default="",verbose_name="操作系统")
    service_line = models.CharField(max_length=32, default="",verbose_name="所属业务线")
    frame = models.CharField(max_length=32,default="", verbose_name="机架")
    remark = models.TextField(default="", null=True, verbose_name="备注")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="修改时间")

    '''注意同时要在admin的显示字段中增加这几个'''
    '''有的类型需要有一个默认值，不然提示增加'''

    def __str__(self):
        return self.hostname + self.remark# 让返回的变为字符串类型

    class Meta:
        db_table = "assets"
