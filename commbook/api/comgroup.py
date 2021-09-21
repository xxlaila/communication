# -*- coding: utf-8 -*-
"""
@File    : comgroup.py
@Time    : 2021/9/16 5:12 下午
@Author  : xxlaila
@Software: PyCharm
"""

from rest_framework import viewsets
from ..serializers.comgroup import *
from ..models.comgroup import *
from django_filters import rest_framework as filters

class ComgroupFilter(filters.FilterSet):
    class Meta:
        model = Comgroup
        fields = ['name']


class ComgroupViewSet(viewsets.ModelViewSet):
    queryset = Comgroup.objects.all()
    serializer_class = ComgroupSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComgroupFilter
