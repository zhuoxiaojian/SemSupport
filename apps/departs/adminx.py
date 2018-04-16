# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 12:31
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
from departs.models import TSDepart
import xadmin
class TSDepartAdmin(object):
    list_display = ('departname', 'description', 'parent',)
    list_filter = ('departname', 'description', 'parent',)
    search_fields = ('departname', )
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    model_icon = 'fa fa-user-secret'

xadmin.site.register(TSDepart, TSDepartAdmin)