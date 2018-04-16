# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 17:23
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from counts.models import FormCount
from counts.models import FormCountTotal

class FormCountTotalAdmin(object):
    list_display = ('user', 'depart', 'xs_name', 'url_count', 'create_time', )
    list_filter = ('create_time', 'xs_name', 'user', 'depart', )
    search_fields = ('xs_name',)
    readonly_fields = ('url_count', 'create_time', 'xs_name',)
    model_icon = 'fa fa-area-chart'  # 修改图标
    show_bookmarks = False  # 屏蔽书签
    refresh_times = (3, 5, 7, 10)  # 每5秒或7秒刷新
    list_export = ()
    def has_delete_permission(request, obj=None):
        return False
    def has_change_permission(request, obj=None):
        return False
xadmin.site.register(FormCountTotal, FormCountTotalAdmin)

class FormCountAdmin(object):
    list_display = ('user', 'depart', 'xs_name', 'hit_url', 'hit_count', 'create_time',)
    list_filter = ('create_time', 'xs_name', 'user', 'depart', )
    search_fields = ('xs_name',)
    readonly_fields = ('hit_url', 'hit_count', 'create_time', 'xs_name',)
    model_icon = 'fa fa-hand-o-up'  # 修改图标
    show_bookmarks = False  # 屏蔽书签
    refresh_times = (3, 5, 7, 10)  # 每5秒或7秒刷新
    list_export = ()
    def has_change_permission(request, obj=None):
        return False
    def has_delete_permission(request, obj=None):
        return False

xadmin.site.register(FormCount, FormCountAdmin)








