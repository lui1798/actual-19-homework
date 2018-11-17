# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-11 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181111_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.IntegerField(choices=[('0', '男'), ('1', '女')], max_length=10, verbose_name='性别'),
        ),
    ]
