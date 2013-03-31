from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# import blog
# from blog import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'QiQiBlog.views.home', name='home'),
    # url(r'^QiQiBlog/', include('QiQiBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/', include('QiQiBlog.blog.urls')),
)
