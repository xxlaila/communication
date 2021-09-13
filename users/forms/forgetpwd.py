# -*- coding: utf-8 -*-
"""
@File    : forgetpwd.py
@Time    : 2021/9/13 4:30 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django import forms
from captcha.fields import CaptchaField


class ForgetForm(forms.Form):
    """
    用户找回密码表单
    """
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码', error_messages={"invalid": "验证码不正确！"})