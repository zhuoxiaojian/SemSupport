# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 9:29
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from channel.models import Channel
class ChannelAdmin(object):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    model_icon = 'fa fa-cubes'


xadmin.site.register(Channel, ChannelAdmin)