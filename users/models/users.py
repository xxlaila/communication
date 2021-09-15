# -*- coding: utf-8 -*-
"""
@File    : users.py
@Time    : 2021/9/3 8:40 上午
@Author  : xxlaila
@Software: PyCharm
"""

from django.db import models
import logging
import uuid

__all__ = ['Users']
logger = logging.getLogger(__name__)

GENDER_CHOICES = (
    ('male', '男'),
    ('female', '女'),
)

class Users(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(null=True, blank=True, max_length=64, db_index=True, verbose_name=('用户名'))
    password = models.CharField(null=True, blank=True, max_length=64, verbose_name=('密码'))
    realname = models.CharField(null=True, blank=True, max_length=128, verbose_name=('姓名'))
    sex = models.CharField(max_length=8, choices=GENDER_CHOICES, default='男', verbose_name=('性别'))
    email = models.EmailField(verbose_name=('邮箱'))
    mobile = models.BigIntegerField(blank=True, null=True, verbose_name=('电话'))
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=('创建日期'))

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = '用户'
        verbose_name_plural = '用户'
