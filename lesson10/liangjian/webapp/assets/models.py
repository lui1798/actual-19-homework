from django.db import models

# Create your models here.

class Assets(models.Model):
    

    STATUS_CHOICE = (
        (0,'GUANJI'),
        (1,'kaiji'),
    )


    hostname = models.CharField(max_length=50,db_index=True,unique=True, verbose_name='hostname')
    cpu_num = models.IntegerField(verbose_name='cpuhe')
    cpu_model = models.CharField(max_length=100,verbose_name='cpu xinghao')
    mem_total      = models.CharField(max_length=3,default='8g',verbose_name='neicun')
    disk           = models.CharField(max_length=4,verbose_name='cipandaxiao')
    public_ip      = models.CharField(max_length=32,verbose_name='public ip')
    private_ip          =   models.CharField(max_length=32, verbose_name="priviate ip")
    remote_ip           =   models.CharField(max_length=32, default="", verbose_name="remote ip")
    op                  =   models.CharField(max_length=32, default="", verbose_name="aa ")
    status              =   models.IntegerField(choices=STATUS_CHOICE,verbose_name="status 0 | 1")
    os_system           =   models.CharField(max_length=32, verbose_name="os")
    service_line        =   models.CharField(max_length=32, verbose_name="group")
    frame               =   models.CharField(max_length=32, verbose_name="jijia")
    remark    = models.TextField(default="",null=True,verbose_name='beizhu')
    create_time         = models.DateTimeField(auto_now_add=True,verbose_name='chuangjianshijian')
    update_time         = models.DateTimeField(auto_now=True,verbose_name='update time')
    
    
    def __str__(self):
        return self.hostname
    class Meta:
        db_table = "assets"
