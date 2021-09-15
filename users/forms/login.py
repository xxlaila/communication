# -*- coding: utf-8 -*-
"""
@File    : login.py
@Time    : 2021/9/11 4:48 下午
@Author  : xxlaila
@Software: PyCharm
"""

from django import forms

class LoginForm(forms.Form):
    """
    User login form
    """
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))