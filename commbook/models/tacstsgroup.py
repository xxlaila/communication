# -*- coding: utf-8 -*-
"""
@File    : tacstsgroup.py
@Time    : 2021/9/22 9:26 下午
@Author  : xxlaila
@Software: PyCharm
"""

from django.db import models
import logging
import uuid
from ..models.comgroup import *
from ..models.contacts import *

__all__ = ['Tacstsgroup']

logger = logging.getLogger(__name__)

class Tacstsgroup(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    group = models.ForeignKey(Comgroup, blank=True, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(Contacts, blank=True, null=True, on_delete=models.SET_NULL)
    date_updated = models.DateTimeField(auto_now=True, null=True, verbose_name=('更新时间'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=('创建时间'))

    class Meta:
        ordering = ['-date_created']
        verbose_name = '分组关联'
