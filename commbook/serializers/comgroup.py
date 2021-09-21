# -*- coding: utf-8 -*-
"""
@File    : comgroup.py
@Time    : 2021/9/16 5:06 下午
@Author  : xxlaila
@Software: PyCharm
"""

from rest_framework import serializers
from ..models.comgroup import *

class ComgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comgroup
        fields = '__all__'

        # fields = ['name', comment]
        # exclude = ['date_created']
        # depth = 2  # 自动深度，值代表深度次数，但是被深度的外键采用__all__，显示所以字段