# -*- coding: utf-8 -*-
"""
@File    : contacts.py
@Time    : 2021/9/15 4:50 下午
@Author  : xxlaila
@Software: PyCharm
"""

from django.views.generic import TemplateView
from ..models.contacts import *

class ContactsListView(TemplateView):
    """
    user list
    """
    template_name = 'commbook/_contacts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts_lists = Contacts.objects.all()
        context['contacts_lists'] = contacts_lists

        return context