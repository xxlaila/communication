# -*- coding: utf-8 -*-
"""
@File    : register.py
@Time    : 2021/9/7 7:42 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django.core import validators
from django.core.exceptions import ValidationError
from ..models import *
from django import forms
from ..models.users import GENDER_CHOICES
from django.forms import fields, widgets
import re


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

def idcard_validate(value):
    idcard_re = re.compile(r'^[0-9]+$')
    if not idcard_re.match(value):
        raise ValidationError('请输入数字')

class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               error_messages={"required": "不能为空","invalid": "格式错误",})
    realname = forms.CharField(label="真实姓名", max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               error_messages={"required": "不能为空",})
    sex = fields.ChoiceField(label="性别", choices=GENDER_CHOICES)
    email = forms.EmailField(label="邮箱",  widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(label="手机", widget=forms.TextInput(attrs={'class': 'form-control'}),
                                validators=[mobile_validate,])
    password1 = forms.CharField(label="密码", max_length=256,  widget=forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
                                error_messages={"required": "不能为空", "min_length": "密码最短8位"}, min_length=6)
    password2 = forms.CharField(label="确认密码", max_length=256,  widget=forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
                                error_messages={"required": "不能为空","min_length": "密码最短8位"})

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        exists = Users.objects.filter(mobile=mobile).exists()
        if exists:
            raise forms.ValidationError("手机号码已经存在!")
        return mobile

    def clean_username(self):
        username = self.cleaned_data.get("username")
        exists = Users.objects.filter(username=username).exists()
        if exists:
            self.add_error("username", ValidationError("用户名存在"))
        if username in ["admin", "administrator"]:
            self.add_error("username", ValidationError("该名称不能使用"))
        return username

    def clean(self):
        password_value = self.cleaned_data.get('password1')
        re_password_value = self.cleaned_data.get('password2')
        if password_value == re_password_value:
            return self.cleaned_data
        else:
            self.add_error('password2', ValidationError('两次密码不一致'))

    # def __int__(self, *args, **kwargs):
    #     super(RegisterForm, self).__int__(*args, **kwargs)
    #     for field in iter(self.fields):
    #         self.fields[field].widget.attrs.update({
    #             'class': 'form-control'
    #         })

class a(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'
        exclude = ['is_active']
        widgets = {
            "__all__": forms.TextInput(attrs={'class':'c1'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'sex': forms.ChoiceField(choices=GENDER_CHOICES),
            'mobile': forms.IntegerField(validators=[mobile_validate,])
        }
        error_messages = {
            "__all__": {"required": "不能为空", 'invalid': '格式不正确'},
            'email': {"required": "不能为空", 'invalid': '邮箱格式不正确'}
        }
        help_texts = {"email": "test@163.com"}
        labels = {"username": "登陆名", "realname": "用户名", "sex": "性别", "mobile": "电话", "idcard": "身份证", "password": "密码"}

    def clean_username(self):
        value = self.cleaned_data.get("username")
        if ["admin", "administrator"] in value:
            raise ValidationError("不能使用该名称")
        else:
            return value

    def clean(self):
        password_value = self.cleaned_data.get('password1')
        re_password_value = self.cleaned_data.get('password2')
        if password_value == re_password_value:
            return self.cleaned_data
        else:
            self.add_error('password2', '两次密码不一致')
            raise ValidationError('两次密码不一致')
