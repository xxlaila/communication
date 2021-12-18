# -*- coding: utf-8 -*-
"""
@File    : login.py
@Time    : 2021/9/7 9:32 上午
@Author  : xxlaila
@Software: PyCharm
"""
from django.contrib import auth
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
    """
    User login
    """
    def get(self, request):
        request.session.flush()
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
                if user.is_active:
                    if user.password == hash_code(password):
                        request.session['is_login'] = True
                        request.session['user_id'] = str(user.id)
                        request.session['username'] = user.username
                        return render(request, 'index.html')
                    else:
                        return render(request, 'users/login.html', {"login_form": login_form, "msg": "密码不正确"})
                else:
                    active_forms = ForgetForm(request.POST)
                    return render(request, 'users/_disable_user.html', {"active_forms": active_forms, "msg": "用户未激活"})
            except Exception as e:
                return render(request, 'users/login.html', {"login_form": login_form, "msg": "用户不存在！"})
        login_form = LoginForm
        return render(request, 'users/login.html', {'login_form': login_form})

def MyUserInfo(username):
    user_datas = Users.objects.filter(username=username)
    return user_datas

class UserInfoView(View):
    def get(self, request, p1):
        if request.session['username']:
            # username = request.user.is_authenticated():
            if not request.user.is_authenticated:
                user = Users.objects.filter(username=p1)
                return render(request, 'users/_app_profile.html', {"datas": user})
            else:
                return redirect('api-users:login')
        else:
            return redirect('api-users:login')

def logout(request):
    """
    logout
    :param request:
    :return:
    """
    if not request.session.get('is_login', None):
        return redirect('users:login')
    request.session.flush()
    return redirect('users:login')

class ForgetPwdView(View):
    """
    Retrieve password
    """
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
                return redirect('users:login')
                # return render(request, 'send_success.html')
            else:
                msg = "系统未找到该邮箱，请核对后输入！"
                return render(request, 'users/forgetpwd.html', {"forget_form": forget_form, "msg": msg})
        forget_form = ForgetForm()
        return render(request, 'users/forgetpwd.html', {"forget_form": forget_form})

class ResetView(View):
    """
    Jump to the reset password page
    """
    def get(self, request, reset_code):
        pwd_reset = PwdResetForm()
        try:
            record = EmailVerifyRecord.objects.filter(code=reset_code)[0]
            if record.is_active == False:
                if record:
                    email = record.email
                    record.is_active = True
                    record.save()
                    return render(request, 'users/password_reset.html', {'email': email, 'pwd_reset': pwd_reset})
            else:
                return render(request, 'users/_get_active_code.html')
        except:
            return render(request, 'users/_get_active_code.html')

class ModifyPwdView(View):
    """
    reset Password
    """
    def post(self, request):
        pwd_reset = PwdResetForm(request.POST)
        if pwd_reset.is_valid():
            # 获取两次输入的密码
            # pwd1 = pwd_reset.cleaned_data['password1']
            # pwd2 = pwd_reset.cleaned_data['password2']
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            # 这里还要取到对应邮箱，从前端hidden属性标签下的email值获取
            # email = pwd_reset.cleaned_data['email']
            email = request.POST.get('email', '')
            # reset_code 验证过期
            if pwd1 != pwd2:
                return render(request, 'users/password_reset.html', {'pwd_reset': pwd_reset, 'email': email, 'msg': '密码不一致!'})
            else:
                # 修改密码
                user = Users.objects.get(email=email)
                user.password = hash_code(pwd2)
                user.save()
                return redirect('users:login')
        else:
            return render(request, 'users/password_reset.html', {'pwd_reset': pwd_reset})
