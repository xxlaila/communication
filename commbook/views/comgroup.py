# -*- coding: utf-8 -*-
"""
@File    : comgroup.py
@Time    : 2021/9/15 4:50 下午
@Author  : xxlaila
@Software: PyCharm
"""

from django.views.generic import TemplateView
from ..models.comgroup import *

class ComgroupListView(TemplateView):
    """
    user list
    """
    template_name = 'commbook/_comgroup_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_lists = Comgroup.objects.all()
        context['group_lists'] = group_lists

        return context