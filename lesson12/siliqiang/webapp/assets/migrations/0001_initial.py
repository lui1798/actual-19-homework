# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 06:44
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
                ('cpu_num', models.IntegerField(default='2', verbose_name='cpu核数')),
                ('cpu_model', models.CharField(default='Core i7', max_length=100, verbose_name='cpu型号')),
                ('mem', models.CharField(default='2G', max_length=100, verbose_name='内存')),
                ('disk', models.CharField(default='2G', max_length=100, verbose_name='硬盘')),
                ('ip', models.CharField(default='192.168.1.1', max_length=100, verbose_name='IP地址')),
                ('op', models.CharField(default='', max_length=32, verbose_name='运维负责人')),
                ('system', models.CharField(default='', max_length=32, verbose_name='操作系统')),
                ('line', models.CharField(default='', max_length=32, verbose_name='所属业务线')),
                ('remark', models.TextField(default='', null=True, verbose_name='备注')),
                ('host_status', models.IntegerField(default='', verbose_name='机器的状态0|1')),
            ],
            options={
                'db_table': 'assets',
            },
        ),
    ]
