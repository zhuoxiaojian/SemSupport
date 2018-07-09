# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 14:35
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm

from speechcraft.models import Speechcraft, SpeechcraftShow
import xadmin
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from SemSupport.settings import MEDIA_ROOT
from utils.readExcelUtil import read_read_excel_speechcraft
class SpeechcraftAdmin(object):
    list_display = ('speechTarget', 'speechKeyword',  'speechGoal', 'speechAnswer', 'speechLabel', 'speechCreateTime')
    list_filter = ('speechGoal', 'speechKeyword', 'speechAnswer', 'speechLabel', )
    search_fields = ('speechKeyword', )
    exclude = ['speechTitle', 'speechQuestion', 'speechFlow', 'speechRemark', 'speechCount']
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    import_excel = True
    model_icon = 'fa fa-language'
    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            excelFile = request.FILES.get('excel')
            excel_name = excelFile.name
            path = default_storage.save(excel_name, ContentFile(excelFile.read()))
            tmp_file = os.path.join(MEDIA_ROOT, path)
            read_read_excel_speechcraft.delay(tmp_file, excel_name)
        return super(SpeechcraftAdmin, self).post(request, args, kwargs)
    # def save_models(self):
    #     obj = self.new_obj
    #     print(obj.speechFlow)
    #     pass
xadmin.site.register(Speechcraft, SpeechcraftAdmin)


class SpeechcraftShowAdmin(object):
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    model_icon = 'fa fa-search'

xadmin.site.register(SpeechcraftShow, SpeechcraftShowAdmin)
