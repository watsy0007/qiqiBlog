# -*- coding: UTF-8 –*-
__author__ = 'watsy'

import json
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from QiQiBlog.blog.models import ArticlePost, Category
from django.contrib import admin
from django.contrib.auth import *

page_count = 2

def getBlogsCategoryAndTime():
    blogs = ArticlePost.objects.all()

    timeset = set()
    for blog in blogs:
        timeset.add(blog.created_date.strftime("%Y-%m"))
    times = [time for time in timeset]

    categorys = Category.objects.all()

    return (blogs, categorys, times)

def getBlogs(request, select_page=None, select_category = None, select_time = None):
    templateName = 'index.html'
    (blogs, categorys, times) = getBlogsCategoryAndTime()

    show_blogs = []
    #选择类型
    if (select_category):
        for blog in blogs:
            if blog.category and blog.category.title == select_category:
                show_blogs.append(blog)
    elif (select_time):
        for blog in blogs:
            time = blog.created_date.strftime("%Y-%m")
            if time == select_time:
                show_blogs.append(blog)
    else:
        show_blogs = list(blogs)

    #计算翻页
    if len(show_blogs) < page_count + 1:
        sum_pages = 1
    else:
        sum_pages = len(show_blogs) / page_count + 1

    #当前翻页的页面
    if not select_page:
        select_page = 1
    else:
        select_page = int(select_page)

    #计算页面中的blog
    if select_page == sum_pages:
        show_blogs = show_blogs[(select_page - 1) * page_count:]
    else:
        show_blogs = show_blogs[(select_page - 1) * page_count: (select_page) * page_count]

    kwargs = {
        "nav_active_index"  :   'blog',
        'blogs'             :   show_blogs,
        'categorys'         :   categorys,
        'cur_category'      :   select_category,
        'times'             :   sorted(times, reverse=True),
        'cur_time'          :   select_time,
        'cur_page'          :   select_page
    }

    if sum_pages > 1:
        kwargs['pages'] = range(1,sum_pages + 1)

    return render_to_response(templateName, kwargs)

#首页
def index(request):
    return getBlogs(request)
#翻页
def blogPage(request, page):
    return getBlogs(request, select_page=page)

#根据时间索引
def times(request, stimes, page = None):
    return getBlogs(request, select_time=stimes, select_page=page)

#根据分类索引
def category(request, sCategory, page = None):
    return getBlogs(request, select_category= sCategory, select_page=page)

#具体页面
def blog(request, blog_id):
    templateName = 'blogDetail.html'
    (blogs, categorys, times) = getBlogsCategoryAndTime()

    blog = ArticlePost.objects.get(id=blog_id)

    kwargs = {
        "nav_active_index"  :   'blog',
        'categorys'         :   categorys,
        'times'             :   times,
        'blog'             :   blog,
    }

    return render_to_response(templateName, kwargs)

#TODO
def weibo(request):
    templateName = 'index.html'
    kwargs = {"nav_active_index" : 'weibo'}
    return render_to_response(templateName, kwargs)
#TODO
def mark(request):
    templateName = 'index.html'
    kwargs = {"nav_active_index" : 'mark'}
    return render_to_response(templateName, kwargs)
#TODO
def about(request):
    templateName = 'about.html'
    kwargs = {"nav_active_index" : 'about'}
    return render_to_response(templateName, kwargs)

#other device get data function
def getAllBlogs(request):
    blogs = ArticlePost.objects.all()
    jsonBlogs = []
    for blog in blogs:
        jsonBlogs.append(
            {
                "id" : blog.id,
                "title": blog.title,
                "status" : blog.status,
                "author" : blog.author.username,
                "created_date" : unicode(blog.created_date),
                "update_date" : unicode(blog.updated_date),
                "content" : blog.content,
             })
    return HttpResponse(json.dumps(jsonBlogs), mimetype='application/json')