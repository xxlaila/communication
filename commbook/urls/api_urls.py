# -*- coding: utf-8 -*-
"""
@File    : api_urls.py
@Time    : 2021/9/15 4:48 下午
@Author  : xxlaila
@Software: PyCharm
"""

from django.conf.urls import url
from django.urls import path,re_path
from rest_framework.routers import DefaultRouter
from ..views.contacts import *
from ..views.comgroup import *
from ..api import *

app_name = "commbook"

router = DefaultRouter()
# router.register(r'comgroups', ComgroupViewSet, 'comgroup')


urlpatterns = [
    path('comgroup/list/', ComgroupListView.as_view(), name='comgroup-list'),
    path('comgroup/add/', ComgroupAddView.as_view(), name='comgroup-add'),
    path('comgroup/<uuid:pk>/update/', ComgroupUpdateView.as_view(), name='comgroup-edit'),
    path('comgroup/<uuid:pk>/remove/', ComgroupDeleteView.as_view(), name='comgroup-remove'),
    path('contact-list/', ContactsListView.as_view(), name='contact-list'),
    ]

urlpatterns += router.urls