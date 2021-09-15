# -*- coding: utf-8 -*-
"""
@File    : usergroup.py
@Time    : 2021/9/14 12:13 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from ..models.users import *
from ..models.groups import *

class UserTempldate(TemplateView):
    """
    user list
    """
    template_name = 'users/_user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_lists = Users.objects.all()
        context['user_lists'] = user_lists

        return context

class GroupListView(TemplateView):
    """
    user group list
    """
    template_name = 'users/_group_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_lists = Groups.objects.all()
        context['group_lists'] = group_lists

        return context