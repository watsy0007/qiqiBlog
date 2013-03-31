__author__ = 'watsy'

import json
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from QiQiBlog.blog.models import ArticlePost
from django.contrib import admin
from django.contrib.auth import *

def index(request, **kwargs):
    return render_to_response(kwargs['template_name'])


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