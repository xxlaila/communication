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
from ..forms.login import *
from ..models.users import *
from utils.hashcode import hash_code
from ..forms.forgetpwd import *
from utils.email_send import *

class LoginView(View):

    def get(self, request):
        login_form = LoginForm(request.POST)
        if request.session.get('is_login', None):
            return redirect('/')
        return render(request, "users/login.html", {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = Users.objects.get(username=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = str(user.id)
                    request.session['username'] = user.username
                    return render(request, 'index.html')
            except Exception as e:
                message = "用户不存在！"
                return render(request, 'users/login.html', {"message": message})

        login_form = LoginForm
        return render(request, 'users/login.html', {'login_form': login_form})


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('users:login')
    request.session.flush()
    return redirect('users:login')

class ForgetPwdView(View):

    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'users/forgetpwd.html', {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = forget_form.cleaned_data['email']
            user_email = Users.objects.filter(email=email)
            if user_email:
                send_register_email(email, "forget")
                return redirect('/login/')
            else:
                message = "系统为找到该邮箱，请核对后输入！"
            # return render(request, 'authapp/login.html', locals())
        forget_form = ForgetForm()
        return render(request, 'users/forgetpwd.html', {"forget_form": forget_form})
