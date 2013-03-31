__author__ = 'watsy'

from django.db import models
from django.utils.translation import gettext_lazy as _



class BasePost(models.Model):
    DRAFT   = 0
    LIVE    = 1
    CLOSED  = 2

    STATUS_CHOICES = (
        (DRAFT, _(u'Draft')),
        (LIVE, _ (u'Live')),
        (CLOSED, _(u'Closed')),
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=LIVE,
        db_index=True,
    )
    author = models.ForeignKey('auth.User', db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _(u'base post')
        ordering = ('-created_date', )


class ArticlePost(BasePost):

    title = models.CharField(max_length=120)
    content = models.TextField()
