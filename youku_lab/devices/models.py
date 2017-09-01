# coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'设备品牌',)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'设备品牌表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 设备信息表
class Message(models.Model):
    devices_id = models.CharField(max_length=20, verbose_name=u'设备ID')
    name = models.CharField(max_length=50, verbose_name=u'设备名',)
    version = models.CharField(max_length=50, verbose_name=u'系统版本')
    brand = models.ForeignKey(Brand, verbose_name=u'设备品牌')
    # borrower = models.CharField(max_length=20, verbose_name=u'借用人')
    borrower = models.ForeignKey(User, verbose_name=u'借用人', null=True, blank=True)
    status_code = [
        ('True', u'未借用'),
        ('False', u'已借用'),
        ('Error', u'设备异常')
    ]
    status = models.CharField(max_length=16, verbose_name='设备状态', choices=status_code, default='True')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'设备信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

