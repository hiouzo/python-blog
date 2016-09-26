# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render
from django.conf import settings
# from django.http import HttpResponse

logger = logging.getLogger('blogs.views')


# Create your views here.


# 配置站点信息,站点名字、描述、邮箱
def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_BESC': settings.SITE_BESC,
            'PRO_EMAIL': settings.PRO_EMAIL}


def index(request):
    # 测试日志例子, 找不到sss.txt文件的时候 在log文件夹的error.log里会发现多一个错误
    # try:
    #     open('sss.txt','r')
    # except Exception as e:
    #     logger.error(e)
    return render(request, 'index.html', locals())


def login(request):
    return render(request, 'login.html', locals())


def failure(request):
    return render(request, 'failure.html', locals())


def article(request):
    return render(request, 'article.html', locals())
