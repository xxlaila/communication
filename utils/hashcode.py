# -*- coding: utf-8 -*-
"""
@File    : hashcode.py
@Time    : 2021/9/11 4:55 下午
@Author  : xxlaila
@Software: PyCharm
"""
import hashlib

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()