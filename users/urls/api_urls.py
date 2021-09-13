# -*- coding: utf-8 -*-
"""
@File    : api_urls.py
@Time    : 2021/9/7 9:32 上午
@Author  : xxlaila
@Software: PyCharm
"""

from django.urls import path,re_path
from ..views import login
from ..views.register import *

app_name = "users"

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='login'),
    path('logout/', login.logout, name='logout'),
    path('register/', RegisterView, name='register')
]