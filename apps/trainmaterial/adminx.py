# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 9:39
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from trainmaterial.models import Trainmaterial
class TrainmaterialAdmin(object):
    list_display = ('train_type', 'showTrainFile', 'train_remark', 'create_time', 'changeTrainFile', )
    list_filter = ('train_type', )
    search_fields = ('train_type', )
    show_bookmarks = False #屏蔽书签
    model_icon = 'fa fa-file-word-o'
    list_export = ()#设置不显示导出按钮

xadmin.site.register(Trainmaterial, TrainmaterialAdmin)