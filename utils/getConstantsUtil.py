# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 9:16
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : getConstantsUtil.py
# @Software: PyCharm

from constants.models import Constants

#获取参数值
def getConstantsVale(key):
    c_v = Constants.objects.filter(key=key)
    if c_v.exists():
        v = c_v[0].value
        return v
    else:
        return None

