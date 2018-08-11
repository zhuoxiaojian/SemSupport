# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 10:20
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : validators.py
# @Software: PyCharm

from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    max_size = 50 * 1024 * 1024
    valid_extensions = ['.pptx', '.docx', '.txt', '.xlsx', '.ppt', '.doc', '.xls', '.pdf', ]
    if not ext in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
    else:
        if value.size > max_size:
            raise ValidationError(u'Unsupported file size.')


