# -*- coding: utf-8 -*-
"""
@File    : contacts.py
@Time    : 2021/9/22 10:45 上午
@Author  : xxlaila
@Software: PyCharm
"""

from django.forms import ModelForm
from ..models.contacts import *
from django import forms
from users.models.users import GENDER_CHOICES
from django.core.exceptions import ValidationError


class ContactsForm(ModelForm):

    class Meta:
        model = Contacts
        fields = '__all__'
        exclude = ['id']

        widgets = {
            'sex': forms.Select(choices=GENDER_CHOICES),
            'birthday': forms.DateInput({"type": "date"}),
            'email': forms.EmailInput(),
        }
        error_messages = {
            'email': {'invalid': '邮箱格式不正确'}
        }
        labels = {"name": "姓名", "sex": "性别", 'mobile': "电话", "gourp": "分组", "birthday": "生日",
                  "appellative": "称呼", "qq": "QQ", "email": "邮箱", "units": "单位", "address": "家庭住址", "comment": "备注"}

    def __init__(self, *args, **kwargs):
        super(ContactsForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}
            field.error_messages = {"required": "不能为空"}

