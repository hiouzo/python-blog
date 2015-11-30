# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    # #页面内容需要显示的参数参数.exclude是不显示的参数列举
    # fields = ('title','desc','content','date_publish','user')
    fieldsets = (
        (None, {
            'fields': ('title','desc','content','user')
        }),
        ('more', {
            'classes': ('collapse',),
            'fields': ('tag','category','is_recommend')
        }),
    )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
