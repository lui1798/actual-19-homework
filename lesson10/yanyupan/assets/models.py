from django.db import models

# Create your models here.


class Assets(models.Model):
    '''
        status:
            0：表示关机
            1：表示运行
    '''
    STATUS_CHOICE = (
        (0, '已下线'),
        (1, '已上线'),
    )
    hostname                = models.CharField(max_length=50, db_index=True, unique=True, verbose_name="主机名")
    cpu_num                 = models.IntegerField(null=True, blank=True, verbose_name="CPU核数")
    cpu_model               = models.CharField(max_length=100, verbose_name="CPU型号")
    mem_total               = models.CharField(max_length=3, default="8G", verbose_name="内存")
    disk                    = models.CharField(max_length=4, verbose_name="硬盘")
    public_ip               = models.CharField(max_length=32, default="", verbose_name="公网IP")
    private_ip              = models.CharField(max_length=32, default="", verbose_name="内网IP")
    remote_ip               = models.CharField(max_length=32, default="", verbose_name="远程IP")
    op                      = models.CharField(max_length=32, default="", verbose_name="负责人")
    status                  = models.IntegerField(choices=STATUS_CHOICE, null=True, blank=True, verbose_name="上下线")
    os_system               = models.CharField(max_length=32, verbose_name="操作系统")
    service_line            = models.CharField(max_length=32, verbose_name="所属业务")
    frame                   = models.CharField(max_length=32, verbose_name="机柜位置")
    remark                  = models.TextField(default="", null=True, verbose_name="备注")
    create_time             = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time             = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.hostname + self.remark

    class Meta:
        db_table = "assets"