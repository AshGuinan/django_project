# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.views import login, logout
from myapp.views import register,welcome
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', welcome),
	url(r'^login/$',login),
	url(r'^logout/$',logout),
	url(r'^register/$',register),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/profile/$',welcome),
(r'^myapp/', include('myproject.myapp.urls')),
	(r'^upload/', RedirectView.as_view(url='/myapp/list/')), # Just for ease of use.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

