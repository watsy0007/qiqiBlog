__author__ = 'watsy'

from QiQiBlog.blog.models import ArticlePost, Category
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category' ,'created_date', 'content', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(ArticlePost, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
