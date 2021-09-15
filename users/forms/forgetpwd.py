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
    User retrieve password form
    """
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码', error_messages={"invalid": "验证码不正确！"})

class PwdResetForm(forms.Form):
    """
    Password reset form
    """
    password1 = forms.CharField(label="密码", min_length=8, max_length=20,
                                required=True, help_text='密码必须包含大写、小写以及数字',
                                widget=forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
                                error_messages={"required": "不能为空", "min_length": "密码最短8位",
                                                "max_length": "密码最长20位", "invalid": "密码需要包含大写、小写和数字",})
    password2 = forms.CharField(label="确认密码", min_length=8, max_length=20,
                                required=True, help_text='密码必须包含大写、小写以及数字',
                                widget=forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
                                error_messages={"required": "不能为空", "min_length": "密码最短8位",
                                                "max_length": "密码最长20位", "invalid": "密码需要包含大写、小写和数字",})

