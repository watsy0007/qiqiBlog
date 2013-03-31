__author__ = 'watsy'

from QiQiBlog.blog.models import ArticlePost
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_date', 'content')

admin.site.register(ArticlePost, ArticleAdmin)
