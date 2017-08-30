from django.contrib import admin
from models import Brand, Message, UserProfile

# Register your models here.


class Brand_Admin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name', 'create_time']
    search_fields = ['name', 'create_time']
    pass


class Message_Admin(admin.ModelAdmin):
    list_filter = ['brand', 'status']
    list_display = ['devices_id', 'name', 'version', 'brand', 'borrower', 'status', 'create_time']
    search_fields = ['devices_id', 'name', 'borrower__name']
    pass


class User_Admin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name', 'job_num', 'phone']
    search_fields = ['name', 'job_num']

admin.site.register(Brand, Brand_Admin)
admin.site.register(Message, Message_Admin)
admin.site.register(UserProfile, User_Admin)
