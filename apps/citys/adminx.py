# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 10:51
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from citys.models import FormRegionCity, Area, Province, City
class FormRegionCityAdmin(object):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    model_icon = 'fa fa-cogs'

xadmin.site.register(FormRegionCity, FormRegionCityAdmin)

class AreaAdmin(object):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    model_icon = 'fa fa-cogs'
xadmin.site.register(Area, AreaAdmin)

class ProvinceAdmin(object):
    list_display = ('name', 'area', )
    list_filter = ('name', 'area', )
    search_fields = ('name', )
    model_icon = 'fa fa-cogs'
xadmin.site.register(Province, ProvinceAdmin)

class CityAdmin(object):
    list_display = ('name', 'province')
    list_filter = ('name', 'province')
    search_fields = ('name', )
    model_icon = 'fa fa-cogs'
xadmin.site.register(City, CityAdmin)