# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 11:13
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
from works.models import customerUser, BackUpWork, BackUpWorkRepeat
from utils.DateFormatUtil import get_today
import works.worksPlugin
import xadmin


class customerUserAdmin(object):
    list_display = ('user_id', 'change_user_id', 'customer_id', 'create_time', )
    list_filter = ('user_id', 'create_time', )
    search_fields = ('create_time', )
    model_icon = 'fa fa-sticky-note'
    list_per_page = 20
    works_show = True


class BackUpWorkAdmin(object):
    list_display = ('user_id', 'user_name', 'create_time', 'update_time', )
    list_filter = ('user_id', 'create_time', 'user_name', )
    search_fields = ('create_time', )
    model_icon = 'fa fa-sticky-note'
    list_per_page = 10

    def queryset(self):
        qs = super(BackUpWorkAdmin, self).queryset()
        return qs


class BackUpWorkRepeatAdmin(object):
    list_display = ('user_id', 'user_name', 'create_time', 'update_time', 'repeat_count', )
    list_filter = ('user_id', 'create_time', 'user_name', )
    search_fields = ('create_time', )
    model_icon = 'fa fa-sticky-note'
    list_per_page = 10

    def queryset(self):
        qs = super(BackUpWorkRepeatAdmin, self).queryset()
        return qs.filter(create_time=str(get_today()))


xadmin.site.register(customerUser, customerUserAdmin)
xadmin.site.register(BackUpWork, BackUpWorkAdmin)
xadmin.site.register(BackUpWorkRepeat, BackUpWorkRepeatAdmin)