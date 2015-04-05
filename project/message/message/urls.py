from django.conf.urls import patterns, include, url

from django.contrib import admin
from message_app.views import register,welcome,add_photo
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', welcome),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'^accounts/register/$',register),
    url(r'^accounts/profile/$',welcome),
    url(r'^add_photo.html',add_photo),
 )
