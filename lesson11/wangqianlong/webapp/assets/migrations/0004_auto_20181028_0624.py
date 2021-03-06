# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20181028_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='disk',
            field=models.CharField(default='100g', max_length=4, verbose_name='磁盘大小'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='frame',
            field=models.CharField(default='1-2-3', max_length=32, verbose_name='机架'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='mem_total',
            field=models.CharField(default='8G', max_length=3, verbose_name='内存'),
        ),
        migrations.AddField(
            model_name='assets',
            name='op',
            field=models.CharField(default='', max_length=32, verbose_name='运维负责人'),
        ),
        migrations.AddField(
            model_name='assets',
            name='os_system',
            field=models.CharField(default='centos 6.4', max_length=32, verbose_name='操作系统'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='private_ip',
            field=models.CharField(default='1.1.1.1', max_length=32, verbose_name='私有ip'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='public_ip',
            field=models.CharField(default='', max_length=32, verbose_name='公网ip'),
        ),
        migrations.AddField(
            model_name='assets',
            name='remote_ip',
            field=models.CharField(default='', max_length=32, verbose_name='远程ip'),
        ),
        migrations.AddField(
            model_name='assets',
            name='service_line',
            field=models.CharField(default='VRouter', max_length=32, verbose_name='所属业务线'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='status',
            field=models.IntegerField(default='1', verbose_name='机器的状态0 | 1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assets',
            name='cpu_model',
            field=models.CharField(max_length=100, verbose_name='cpu型号'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='cpu_num',
            field=models.IntegerField(verbose_name='cpu核'),
        ),
    ]
