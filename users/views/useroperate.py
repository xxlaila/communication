# -*- coding: utf-8 -*-
"""
@File    : useroperate.py
@Time    : 2021/9/14 4:01 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django.views import View
from ..models.emailverifyrecord import *
from ..models.users import *
from django.shortcuts import (
    render, redirect
)

class UsersActiveView(View):
    """
    Operate on login account status
    """
    def post(self, request, pk):
        user = Users.objects.filter(id=str(pk).replace("-", "")).first()
        if user.is_active == False:
            user.is_active = True
        else:
            user.is_active = False
        user.save()
        return redirect('users:user-list')

class UsersDeleteView(View):

    def get(self, request, pk=None):
        if request.session['username'] == 'admin':
            user = Users.objects.filter(id=str(pk).replace("-", "")).first()
            user.delete()
            return redirect('users:user-list')
        return redirect('users:user-list')


class AciveUserView(View):
    """
    User status enables email connection sending
    """
    def get(self, request, active_code):
        try:
            all_records = EmailVerifyRecord.objects.filter(code=active_code)
            if all_records.exists:
                for record in all_records:
                    if record.is_active == True:
                        email = record.email
                        user = Users.objects.get(email=email)
                        user.is_active = True
                        user.save()
                        # 禁用验证码
                        record.is_active = False
                        record.save()
                        return redirect('users:login')
                    else:
                        return render(request, 'users/_get_active_code.html')
        except:
            return render(request, 'users/_get_active_code.html')