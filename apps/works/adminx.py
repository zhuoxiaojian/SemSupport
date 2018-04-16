# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 11:13
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
from works.models import customerUser
import xadmin
class customerUserAdmin(object):
    list_display = ('user_id', 'change_user_id', 'customer_id', 'create_time', )
    list_filter = ('user_id', 'create_time', )
    search_fields = ('create_time', )
    model_icon = 'fa fa-sticky-note'

xadmin.site.register(customerUser, customerUserAdmin)

