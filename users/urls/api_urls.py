# -*- coding: utf-8 -*-
"""
@File    : api_urls.py
@Time    : 2021/9/7 9:32 上午
@Author  : xxlaila
@Software: PyCharm
"""
from django.conf.urls import url
from django.urls import path,re_path
from ..views import login
from ..views.register import *
from ..views.usergroup import *
from ..views.useroperate import *

app_name = "users"

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='login'),
    path('logout/', login.logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forget-pwd/', login.ForgetPwdView.as_view(), name='forget-pwd'),
    path('userinfo/<str:p1>/', login.UserInfoView.as_view(), name='user-info'),
    url(r'^user-one-active/(?P<active_code>.*)/$', AciveUserView.as_view(), name='user-one-active'),
    path('modify/', login.ModifyPwdView.as_view(), name='modify-pwd'),
    url(r'^user-reset/(?P<reset_code>.*)/$', login.ResetView.as_view(), name='user-reset'),

    path('user-list/', UserTempldate.as_view(), name='user-list'),
    path('group-list/', GroupListView.as_view(), name='group-list'),
    path('user-delete/<uuid:pk>/delete/', UsersDeleteView.as_view(), name='user-delete'),

    path('user-active/<uuid:pk>/', UsersActiveView.as_view(), name='user-active'),
]