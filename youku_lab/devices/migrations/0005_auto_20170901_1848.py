# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-01 18:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_auto_20170901_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u501f\u7528\u4eba'),
        ),
    ]
