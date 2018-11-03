from django.db import models

class Assets(models.Model):

    status_choice = (
                    (0,'关机'),
                    (1,'运行中'),
                    )

    hostname    =	models.CharField(max_length=50, db_index=True, unique=True)
    cpu_num	=	models.IntegerField(db_index=True,verbose_name='cpu核数')
    cpu_model	=	models.CharField(max_length=100, verbose_name="cpu型号")
    mem_total           =   models.CharField(max_length=3, default="8G", verbose_name="内存")
    disk                =   models.CharField(max_length=4, verbose_name="磁盘大小")
    public_ip           =   models.CharField(max_length=32, default="", verbose_name="公网ip")
    private_ip          =   models.CharField(max_length=32, verbose_name="私有ip")
    remote_ip           =   models.CharField(max_length=32, default="", verbose_name="远程ip")
    op                  =   models.CharField(max_length=32, default="", verbose_name="运维负责人")
    status              =   models.IntegerField(choices=status_choice,verbose_name="机器的状态0 | 1")
    os_system           =   models.CharField(max_length=32, verbose_name="操作系统")
    service_line        =   models.CharField(max_length=32, verbose_name="所属业务线")
    frame               =   models.CharField(max_length=32, verbose_name="机架")
    remark              =   models.TextField(default="", null=True, verbose_name="备注")
    create_time		=   models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time		=   models.DateTimeField(auto_now=True, verbose_name='修改时间')


    def __str__(self):
        return self.hostname
    class Meta:
        db_table = "assets"

