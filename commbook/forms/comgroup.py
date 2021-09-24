# -*- coding: utf-8 -*-
"""
@File    : comgroup.py
@Time    : 2021/9/20 12:59 下午
@Author  : xxlaila
@Software: PyCharm
"""

from django.forms import ModelForm
from ..models.comgroup import *
from django import forms
from django.core.exceptions import ValidationError

class ComgroupForm(ModelForm):
    """
    Comgroup form
    """

    class Meta:
        model = Comgroup
        fields = ['name', 'comment']

        widgets = {
            # "__all__": forms.TextInput(attrs={'class': 'c1'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            "__all__": {"required": "不能为空", 'invalid': '格式不正确'},
            'name': {"required": "不能为空", 'invalid': '组名不能为空'}
        }
        labels = {"name": "组名", "comment": "备注"}

    def clean_name(self):
        if self.cleaned_data.get("name"):
            value = Comgroup.objects.filter(name=self.cleaned_data.get("name"))
            if value:
                raise ValidationError("%s组已存在，不能使用该名称" % value)
            else:
                return self.cleaned_data.get("name")
        raise ValidationError("组名不能为空")
