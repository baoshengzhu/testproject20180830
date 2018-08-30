#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 21:43
# @Author  : benson
# @Site    : 
# @File    : urls.py.py
# @Software: PyCharm
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)$',views.show)
]