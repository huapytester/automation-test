#!/usr/bin/env python
# coding:utf-8
from models import Brand, Message, UserProfile
import xadmin
# Register your models here.
from xadmin import views
from xadmin.views import ListAdminView


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u"设备借用管理"
    site_footer = u"author 李振华"
    menu_style = "accordion"


class Brand_Admin(object):
    list_filter = ['name']
    list_display = ['name', 'create_time']
    search_fields = ['name', 'create_time']
    pass


class Message_Admin(object):
    list_filter = ['brand', 'status']
    list_display = ['devices_id', 'name', 'version', 'brand', 'borrower', 'status', 'create_time']
    search_fields = ['devices_id', 'name', 'borrower__name']
    pass


class User_Admin(object):
    list_filter = ['name']
    list_display = ['name', 'job_num', 'phone']
    search_fields = ['name', 'job_num']

xadmin.site.register(Brand, Brand_Admin)
xadmin.site.register(Message, Message_Admin)
xadmin.site.register(UserProfile, User_Admin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
