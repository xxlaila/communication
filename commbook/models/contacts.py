# -*- coding: utf-8 -*-
"""
@File    : contacts.py
@Time    : 2021/9/3 9:32 上午
@Author  : xxlaila
@Software: PyCharm
"""

from django.db import models
import logging
import uuid
from users.models.users import GENDER_CHOICES
from users.models.groups import *

__all__ = ['Contacts']
logger = logging.getLogger(__name__)

class Contacts(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(null=True, blank=True, max_length=128, verbose_name=('联系人'))
    sex = models.CharField(max_length=8, choices=GENDER_CHOICES, default='男', verbose_name=('性别'))
    mobile = models.IntegerField(default=None, blank=True, null=True, verbose_name=('电话'))
    gourp = models.ForeignKey(Groups, null=True, related_name='contacts_groups', on_delete=models.SET_NULL)
    birthday = models.DateField(blank=True, null=True)
    appellative = models.CharField(null=True, blank=True, max_length=16, verbose_name=('称呼'))
    qq = models.IntegerField(null=True, verbose_name=('QQ'))
    email = models.EmailField(unique=True, verbose_name=('邮箱'))
    units = models.CharField(null=True, blank=True, max_length=512, verbose_name=('单位'))
    address = models.CharField(null=True, blank=True, max_length=512, verbose_name=('家庭住址'))
    comment = models.TextField(blank=True, verbose_name=('备注'))
    date_updated = models.DateTimeField(auto_now=True, null=True, verbose_name=('更新时间'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=('创建时间'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '联系人'
        verbose_name_plural = '联系人'

