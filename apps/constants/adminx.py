# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 9:13
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from constants.models import Constants
class ConstantsAdmin(object):
    list_display = ('key', 'value', 'remark', )
    list_filter = ('key', )
    search_fields = ('key',)
    model_icon = 'fa fa-sun-o'  # 修改图标
    show_bookmarks = False  # 屏蔽书签
xadmin.site.register(Constants, ConstantsAdmin)