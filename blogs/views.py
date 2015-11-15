# coding:utf-8
import logging
from django.shortcuts import render
from django.conf import settings

logger = logging.getLogger('blog.views')
# Create your views here.

def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_BESC': settings.SITE_BESC,}

def index(request):
    #测试日志例子, 找不到sss.txt文件的时候 在log文件夹的error.log里会发现多一个错误
    # try:
    #     open('sss.txt','r')
    # except Exception as e:
    #     logger.error(e)
    return render(request,'index.html',locals())