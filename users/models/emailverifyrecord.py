# -*- coding: utf-8 -*-
"""
@File    : emailverifyrecord.py
@Time    : 2021/9/3 9:14 上午
@Author  : xxlaila
@Software: PyCharm
"""

from django.db import models
import logging
import uuid
import datetime

__all__ = ['EmailVerifyRecord']
logger = logging.getLogger(__name__)

class EmailVerifyRecord(models.Model):
    """
    邮箱验证码表
    :raise: is_active 0=True，1=False
    """
    register = "register"
    forget = "forget"
    send_type_choices = (
        (register, "注册"),
        (forget, "找回密码"),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(max_length=8, choices=send_type_choices, verbose_name="验证码类型")
    is_active = models.BooleanField(default=True)
    send_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s (%s)" % (self.code, self.email)