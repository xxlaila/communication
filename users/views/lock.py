# -*- coding: utf-8 -*-
"""
@File    : lock.py
@Time    : 2021/10/15 3:07 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django.views import View
from django.shortcuts import (
    render, redirect
)
from utils.hashcode import hash_code
from ..models.users import *

class LockView(View):
    """
    User Lock
    """
    def get(self, request):
        return render(request, "page-lock.html")

    def post(self, request):
        data = request.POST
        username = data.get('username', '')
        password = data.get('password')
        try:
            if username:
                user = Users.objects.get(username=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = str(user.id)
                    request.session['username'] = user.username
                    return render(request, 'index.html')
                else:
                    return render(request, 'page-lock.html', {"msg": "密码不正确"})
            else:
                return redirect('api-users:login')
        except Exception as e:
            return redirect('api-users:login')
