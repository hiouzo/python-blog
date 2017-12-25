# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# from django.http import HttpResponse
from blogs.models import Article, Category

logger = logging.getLogger('blogs.views')


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
    # return render(request, 'index.html', locals())
 
    # 广告数据
    #  最新文章数据
    article_list = Article.objects.all()
    paginator = Paginator(article_list,3)
    try:
        # 通过requests对象获取当前页的数据, 如果没找到这个对象返回1
        page = int(request.GET.get('page',1))
        article_list = paginator.page(page)
        # 异常捕获
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        article_list = paginator.page(1)

    # 导航数据, 读取models里Category分类表里所有数据,截取5个
    category_list = Category.objects.all().values()[:5]
    return render(request, 'index.html', locals())

# 文章归档
# 1. 先获取文章中的年月信息
# print Article.objects.values('date_publish_').distinct()



