#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.urls import path

from . import views

app_name = 'pdf'

urlpatterns = [
    # 合并访问的映射
    path('merge/', views.pdf_merge, name='pdf_merge'),
]