# -*- coding: utf-8 -*-
"""
@File    : login.py
@Time    : 2021/9/11 4:48 下午
@Author  : xxlaila
@Software: PyCharm
"""

from django import forms
from django.core.exceptions import ValidationError
from utils.hashcode import hash_code
from users.models.users import *

class LoginForm(forms.Form):
    """
    User login form
    """
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # def clean(self):
    #     """
    #     Determine whether the two passwords are the same
    #     :return:
    #     """
    #     username = self.cleaned_data.get('username')
    #     password_value = self.cleaned_data.get('password')
    #     re_password_value = Users.objects.get(username=username)
    #     if re_password_value.password == hash_code(password_value):
    #         return self.cleaned_data
    #     else:
    #         self.add_error('password', ValidationError('密码不正确'))
