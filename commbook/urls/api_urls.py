# -*- coding: utf-8 -*-
"""
@File    : api_urls.py
@Time    : 2021/9/15 4:48 下午
@Author  : xxlaila
@Software: PyCharm
"""

from django.conf.urls import url
from django.urls import path,re_path
from ..views.contacts import *
from ..views.comgroup import *

app_name = "commbook"

urlpatterns = [
    path('comgroup-list/', ComgroupListView.as_view(), name='comgroup-list'),
    path('contact-list/', ContactsListView.as_view(), name='contact-list'),
    ]