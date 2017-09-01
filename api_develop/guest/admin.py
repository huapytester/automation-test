# coding:utf-8

from django.contrib import admin

# Register your models here.
from models import Guest, Event


class EventAdmin(admin.ModelAdmin):
    # 后台显示的字段
    list_display = ['id', 'title', 'status', 'address', 'start_time']
    # 定义搜索栏的关键字
    search_fields = ['title', 'address']
    # 过滤关键字
    list_filter = ['status']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'email', 'sign', 'create_time', 'event']
    # 定义搜索栏的关键字
    search_fields = ['user_name', 'phone']
    # 过滤关键字
    list_filter = ['sign']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
