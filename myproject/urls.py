# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.views import login, logout
from myapp.views import register,welcome

urlpatterns = patterns('',
	(r'^myapp/', include('myproject.myapp.urls')),
	url(r'^$',welcome),
	url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'^accounts/register/$',register),
	(r'^upload/$', RedirectView.as_view(url='/myapp/list/')), # Just for ease of use.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
