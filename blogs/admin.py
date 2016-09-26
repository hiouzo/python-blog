# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
from django.contrib.auth.admin import UserAdmin  # 引用admin的类
from django.utils.translation import ugettext, ugettext_lazy as _  # 继承原有admin中对用户管理类引用


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    # list_display 是列参数的配置, 列表参数配置
    list_display = ('title', 'user', 'date_publish', 'is_recommend')

    # #页面内容需要显示的参数.exclude 是不显示的参数列举
    # fields = ('title','desc','content','user')
    # fieldsets 是管理集合, 一部分信息显示在一个主要区域, 另外一部分信息隐藏在扩展里
    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user')
        }),
        # 扩展要显示的参数
        ('more', {
            'classes': ('collapse',),
            'fields': ('tag', 'category', 'is_recommend')
        }),
    )

    # 引入富文本媒体编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


# 继承原有admin中对用户管理类
class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'qq', 'mobile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


"""
# 为什么要定义UserProfileAdmin, 数据库在添加用户密码的时候由于我们在Setting自定义了user的model(111行)
# #自定义用户model
# AUTH_USER_MODEL = 'blogs.User'
# 所以我们的密码在新建的时候是明文密码, 没有经过django的用户类处理过, 所以我们为了对密码或者一些信息加密
# 要把admin的类引用回来
"""





# 定义UserProfileAdmin,对密码以及注册用户参数进行控制
admin.site.register(User, UserProfileAdmin)
admin.site.register(Tag)
admin.site.register(Category)
# 发布文章需要填写的参数扩展
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
