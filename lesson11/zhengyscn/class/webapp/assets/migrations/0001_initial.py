# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='主机名')),
                ('cpu_num', models.IntegerField(verbose_name='cpu核')),
                ('cpu_model', models.CharField(max_length=100, verbose_name='cpu型号')),
                ('mem_total', models.CharField(default='8G', max_length=3, verbose_name='内存')),
                ('disk', models.CharField(max_length=4, verbose_name='磁盘大小')),
                ('public_ip', models.CharField(default='', max_length=32, verbose_name='公网ip')),
                ('private_ip', models.CharField(max_length=32, verbose_name='私有ip')),
                ('remote_ip', models.CharField(default='', max_length=32, verbose_name='远程ip')),
                ('op', models.CharField(default='', max_length=32, verbose_name='运维负责人')),
                ('status', models.IntegerField(verbose_name='机器的状态0 | 1')),
                ('os_system', models.CharField(max_length=32, verbose_name='操作系统')),
                ('service_line', models.CharField(max_length=32, verbose_name='所属业务线')),
                ('frame', models.CharField(max_length=32, verbose_name='机架')),
                ('remark', models.TextField(default='', null=True, verbose_name='备注')),
            ],
            options={
                'db_table': 'assets',
            },
        ),
    ]
