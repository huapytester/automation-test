# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-31 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0003_auto_20170831_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': '\u53d1\u5e03\u4f1a', 'verbose_name_plural': '\u53d1\u5e03\u4f1a'},
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Y', '\u5df2\u53d1\u5e03'), ('N', '\u5f85\u53d1\u5e03')], max_length=10),
        ),
        migrations.AlterField(
            model_name='guest',
            name='sign',
            field=models.CharField(choices=[('N', '\u672a\u7b7e\u5230'), ('Y', '\u5df2\u7b7e\u5230')], max_length=10),
        ),
    ]
