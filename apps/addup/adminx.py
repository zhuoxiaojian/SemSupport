# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 10:01
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
from addup.models import addUpByDepart, CountBySale, CountByDepart
from utils.getNeedDatas import get_addup_depart
import xadmin
from django.db.models import Q
from customers.models import FormCustomer
from django.db.models import Count, Min, Max, Sum
from xadmin.layout import Main, Fieldset, Row, Side
from django.utils.translation import ugettext as _
class addUpByDepartAdmin(object):
    list_display = ('depart', 'sales',  'amount', 'business', 'sem_status', )
    list_filter = ('depart', 'create_time', 'sales', )
    search_fields = ('depart', )
    exclude = ['randid', 'useless_counter', ] #不显示列
    aggregate_fields = {'amount': 'sum', 'business': 'sum', 'sem_status': 'sum'}
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    model_icon = 'fa fa-pie-chart'
    #屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False

    # 修改布局
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset(_('基本信息'),
                             'company_name', 'company_type', 'url', 'city', 'keyword',
                             ),
                    Fieldset(_('联系方式'),
                             'qq', 'wechat', 'phone', 'address',
                             ),
                    Fieldset(_('意向信息'),
                             'sem_status', 'aike_status',
                             ),
                    Fieldset(_('签单信息'),
                             'depart', 'sales', 'amount', 'business',
                             ),
                    Fieldset(_('时间信息'),
                             'create_time', 'update_time',
                             ),
                ),
                Side(

                )
            )
        return super(addUpByDepartAdmin, self).get_form_layout()

    def queryset(self):
        qs = super(addUpByDepartAdmin, self).queryset()
        #get_addup_depart()
        return qs.filter(Q(depart__isnull=False), ~Q(depart=''), ~Q(depart='空'))

xadmin.site.register(addUpByDepart, addUpByDepartAdmin)

class CountBySaleAdmin(object):
    list_display = ('sale', 'total_amount',  'total_business', 'total_amountNum', 'create_time', )
    list_filter = ('sale', 'create_time', )
    search_fields = ('sale', )
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    model_icon = 'fa fa-list'
    ordering = ('-create_time', )
    aggregate_fields = {'total_amount': 'sum', 'total_business': 'sum', 'total_amountNum': 'sum'}
    #屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False
xadmin.site.register(CountBySale, CountBySaleAdmin)

class CountByDepartAdmin(object):
    list_display = ('depart', 'total_amount',  'total_business', 'total_amountNum', 'create_time', )
    list_filter = ('depart', 'create_time', )
    search_fields = ('depart', )
    ordering = ('-create_time', )
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    model_icon = 'fa fa-list-ul'
    aggregate_fields = {'total_amount': 'sum', 'total_business': 'sum', 'total_amountNum': 'sum'}
    #屏蔽添加按钮
    def has_add_permission(self):
        return False

    def has_delete_permission(request, obj=None):
        return False

    def has_change_permission(request, obj=None):
        return False
xadmin.site.register(CountByDepart, CountByDepartAdmin)