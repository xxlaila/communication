# -*- coding: utf-8 -*-
"""
@File    : backends.py
@Time    : 2021/9/26 11:22 上午
@Author  : xxlaila
@Software: PyCharm
"""

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from ..models.users import Users
from utils.hashcode import *

class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Users.objects.get(username=username)
            if user.check_password(hash_code(password)):
                return user
        except Exception as e:
            return None