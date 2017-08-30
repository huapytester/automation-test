# coding:utf-8
from __future__ import unicode_literals
# from django.contrib.auth.models import AbstractUser
from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 自定义user表
class UserProfile(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'昵称')
    job_num = models.CharField(max_length=20, verbose_name=u'工号')
    sign = models.CharField(max_length=100, verbose_name=u'签名')
    phone = models.CharField(max_length=11, verbose_name=u'联系方式')
    # devices = models.CharField(max_length=20, verbose_name=u'借用设备')
    # devices = models.ForeignKey(, verbose_name=u'借用设备')
    gender = models.CharField(choices=(('men', u'酷哥'), ('woman', u'靓女')), max_length=8, default='woman' )

    class Meta:
        verbose_name = u'小伙伴'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 设备品牌表
class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'设备品牌',)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'设备品牌'
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
    borrower = models.ForeignKey(UserProfile, verbose_name=u'借用人', null=True, blank=True, default='/')
    status_code = [
        ('True', u'未借用'),
        ('False', u'已借用'),
        ('Error', u'设备异常')
    ]
    status = models.CharField(max_length=16, verbose_name='设备状态', choices=status_code, default='True')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'设备登记'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

