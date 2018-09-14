#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django import forms

# 上传表单
class PdfMergeForm(forms.Form):
    file1 = forms.FileField(label='上传pdf文件1')
    file2 = forms.FileField(label='上传pdf文件2')
