# -*- coding: utf-8 -*-
"""
@File    : views.py
@Time    : 2021/9/7 9:30 上午
@Author  : xxlaila
@Software: PyCharm
"""

from django.shortcuts import (
    render, redirect
)

def IndexView(request):

    if not request.session.get('is_login', None):
        return redirect('users:login')
    return render(request, 'index.html')
