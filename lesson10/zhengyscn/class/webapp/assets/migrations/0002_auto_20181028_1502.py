# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='assets',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='修改时间'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assets',
            name='status',
            field=models.IntegerField(choices=[(0, '关机'), (1, '运行')], verbose_name='机器的状态0 | 1'),
        ),
    ]
