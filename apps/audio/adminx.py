# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 14:35
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from audio.models import Audio
class AudioAdmin(object):
    list_display = ('visitType', 'title', 'abstarct', 'visitResult', 'anInterviewCompany', 'anInterviewPeople', 'partakeSale', 'changeAudioFile')
    list_filter = ('visitType', 'keyword', 'title', )
    search_fields = ('visitType', )
    show_bookmarks = False #屏蔽书签
    model_icon = 'fa fa-audio-description'
    list_export = ()#设置不显示导出按钮

    # def save_models(self):
    #     obj = self.new_obj
    #     print(obj.audioFile.name)
    #     print(obj.id)


xadmin.site.register(Audio, AudioAdmin)

