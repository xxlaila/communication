# -*- coding: utf-8 -*-
"""
@File    : tacstsgroup.py
@Time    : 2021/9/24 1:15 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django.views.generic import DeleteView
from ..models.tacstsgroup import *
from django.http import JsonResponse


class TacstsgroupDeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        t_user = Tacstsgroup.objects.get(user_id=self.kwargs['pk'])
        t_user.delete()
        return JsonResponse({"status": "success"})

