# -*- coding: utf-8 -*-
"""
@File    : index.py
@Time    : 2021/9/25 5:45 下午
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