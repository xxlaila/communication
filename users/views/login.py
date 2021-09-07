# -*- coding: utf-8 -*-
"""
@File    : login.py
@Time    : 2021/9/7 9:32 上午
@Author  : xxlaila
@Software: PyCharm
"""

from django.views import View
from django.shortcuts import (
    render, redirect
)


# def LoginView(request):

class LoginView(View):

    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        pass


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('users:login')
    request.session.flush()
    return redirect('users:login')


class register(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        pass