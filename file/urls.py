# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('file.views',
	(r'^get/(?P<key>.+)/$', 'get'),
	(r'^put/(?P<public_key>.+)/(?P<secret_key>.+)/$', 'put'),
	(r'^delete/(?P<public_key>.+)/(?P<secret_key>.+)/(?P<key>.+)/$', 'delete'),
)
