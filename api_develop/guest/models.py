# coding:utf-8
from __future__ import unicode_literals

from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    limit = models.IntegerField(verbose_name=u'最大容纳观众')
    status_code = {
        (u'False', u'待发布'),
        (u'True', u'已发布'),
    }
    status = models.CharField(choices=status_code, max_length=10, verbose_name=u'状态', default=u'False')
    address = models.CharField(max_length=200, verbose_name='发布会地址')
    start_time = models.DateTimeField('events time')
    describe = models.CharField(max_length=300, verbose_name=u'详情', default=' ')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'发布会'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Guest(models.Model):
    event = models.ForeignKey(Event)
    user_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    status_code = {
        (u'N', u'未签到'),
        (u'Y', u'已签到'),
    }
    sign = models.CharField(choices=status_code, max_length=10, default=u'N')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'嘉宾'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name
