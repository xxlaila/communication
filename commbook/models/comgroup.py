# -*- coding: utf-8 -*-
"""
@File    : comgroup.py
@Time    : 2021/9/15 10:01 上午
@Author  : xxlaila
@Software: PyCharm
"""

from django.db import models
import logging
import uuid
from django.urls import reverse


__all__ = ['Comgroup']

logger = logging.getLogger(__name__)

class Comgroup(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(null=True, blank=True, max_length=32, verbose_name=('组名'))
    comment = models.TextField(blank=True, verbose_name=('备注'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=('创建日期'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '通讯录组'
        verbose_name_plural = '通讯录组'

    def get_absolute_url(self):
        return reverse('api-commbook:comgroup-list')