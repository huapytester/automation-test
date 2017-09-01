# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-31 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0006_auto_20170831_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Y', '\u5df2\u53d1\u5e03'), ('N', '\u5f85\u53d1\u5e03')], default='N', max_length=10, verbose_name='\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='sign',
            field=models.CharField(choices=[('N', '\u672a\u7b7e\u5230'), ('Y', '\u5df2\u7b7e\u5230')], default='N', max_length=10),
        ),
    ]