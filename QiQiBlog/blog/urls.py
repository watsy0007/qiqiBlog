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
    url(r'^$', views.index, kwargs={'template_name' : "index.html"}, name="blog_index"),
)