__author__ = 'watsy'

from django.conf.urls import patterns, include, url, static
from django.conf import settings

from QiQiBlog.blog import views

# api
urlpatterns = patterns('',
    url(r'^api/blogs/$', views.getAllBlogs),
)


# pages
urlpatterns += patterns('',

    url(r'^about$', views.about, name='blog_about'),
    url(r'^mark$', views.mark, name= 'blog_mark'),
    url(r'^weibo$', views.weibo, name="blog_weibo"),


    url(r'^time/([a-zA-Z0-9_-]+)$', views.times, name='blog_time_select'),
    url(r'^time/([a-zA-Z0-9_-]+)/page/(\d+)$', views.times, name='blog_time_select_page'),
    url(r'^category/([a-zA-Z0-9_+-]+)$', views.category, name='blog_category_select'),
    url(r'^category/([a-zA-Z0-9_-]+)/page/(\d+)$', views.category, name='blog_category_select_page'),

    url(r'^blog/(\d+)$', views.blog, name='blog_detail'),
    url(r'^blog/page/(\d+)$', views.blogPage, name='blog_page'),
    url(r'^blog$', views.index,  name="blog_blog"),

    url(r'^$', views.index, name="blog_index"),
)