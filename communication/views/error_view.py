# -*- coding: utf-8 -*-
"""
@File    : error_view.py
@Time    : 2021/9/25 5:46 下午
@Author  : xxlaila
@Software: PyCharm
"""
from django.shortcuts import render
from django.http import JsonResponse

__all__ = ['handler404', 'handler500']


def handler404(request, *args, **argv):
    if request.content_type.find('application/json') > -1:
        response = JsonResponse({'error': 'Not found'}, status=404)
    else:
        response = render(request, 'error/error-404.html', status=404)
    return response


def handler500(request, *args, **argv):
    if request.content_type.find('application/json') > -1:
        response = JsonResponse({'error': 'Server internal error'}, status=500)
    else:
        response = render(request, 'error/error-500.html', status=500)
    return response
