# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 14:28
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin
from customers.models import FormCustomer, SEOCustomer
from utils.getNeedDatas import get_real_data
from utils.getNeedDatas import get_sale_manager_id, get_saleManager_data, get_new_customer_data_to_admin, get_seo_sale_work, get_seo_sale_id, get_sale_id
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from SemSupport.settings import MEDIA_ROOT
from utils.readExcelUtil import read_excel, read_read_excel_seo
from customers.models import FormCustomerImport, NewFormCustomer, SuccessCustomer, SeoSaleWork
from xadmin.layout import Main, Fieldset, Row, Side
from django.utils.translation import ugettext as _
#公司信息
class FormCustomerAdmin(object):

    list_display = ('company_name', 'change_url', 'company_type', 'phone', 'qq', 'wechat', 'city', 'address', 'remark', 'create_time', 'update_time')
    list_filter = ('company_name', 'create_time', 'city', )
    search_fields = ('company_name', )
    list_per_page = 20
    readonly_fields = ['create_time', 'sem_status', 'aike_status', 'depart', 'sales', 'business', 'keyword', 'update_time', 'amount']
    exclude = ['randid', 'useless_counter', ] #不显示列
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    model_icon = 'fa fa-cog'

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
        return super(FormCustomerAdmin, self).get_form_layout()



    def queryset(self):
        user_id = self.user.id
        user_name = self.user.username
        qs = super(FormCustomerAdmin, self).queryset()
        if self.user.is_superuser:
            return qs
        else:
            sm_id = get_sale_manager_id()
            if user_id in sm_id:
                dict_work = get_saleManager_data()
                if dict_work:
                    dict_key = str(user_id)+user_name
                    manage_randid_list = dict_work[dict_key]
                    return qs.filter(randid__in=manage_randid_list)
            else:
                sale_id_list = get_sale_id()
                if user_id in sale_id_list:
                    randid_list = get_real_data(self.user.id, self.user.city.name)
                    return qs.filter(randid__in=randid_list)
                else:
                    return qs

    # def save_models(self):
    #     obj = self.new_obj
    #     print(obj.id)

xadmin.site.register(FormCustomer, FormCustomerAdmin)


#seo公司信息
class SEOCustomerAdmin(object):
    list_display = ('company_name', 'company_type', 'link_man', 'tel_phone', 'mobile_phone', 'address', 'aike_status', 'seo_status', 'prefecture_level_city', 'create_date', )
    list_filter = ('company_name', 'create_date', 'prefecture_level_city', )
    search_fields = ('company_name', )
    list_per_page = 20
    readonly_fields = ['rand_id', 'channel', 'level']
    # exclude = ['randid', ] #不显示列
    show_bookmarks = False #屏蔽书签
    model_icon = 'fa fa-folder-o'
    import_excel = True
    # 修改布局
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset(_('基本信息'),
                             'company_name', 'company_type', 'url', 'legal_man', 'issue_date', 'registration_authority',
                             ),
                    Fieldset(_('联系人物'),
                             'link_man', 'sex', 'job', 'is_boss', 'isboss_mobile',
                             ),
                    Fieldset(_('联系方式'),
                             'tel_phone', 'mobile_phone', 'mobile_phone_address', 'mobile_carrieroperator', 'zip_code'
                             ),
                    Fieldset(_('主要经营'),
                             'scope_business', 'business_position', 'produce_address',
                             ),
                    Fieldset(_('地址详情'),
                             'province', 'prefecture_level_city', 'county_district', 'address',
                             ),
                    Fieldset(_('注册日期'),
                             'register_year', 'register_month', 'register_date',
                             ),
                    Fieldset(_('财务信息'),
                             'finance_principal', 'finance_principal_mobile',
                             ),
                    Fieldset(_('渠道信息'),
                             'channel',
                             ),
                    Fieldset(_('意向信息'),
                             'seo_status', 'aike_status',
                             ),
                    Fieldset(_('时间信息'),
                             'create_date', 'update_date',
                             ),
                ),
                Side(

                )
            )
        return super(SEOCustomerAdmin, self).get_form_layout()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            excelFile = request.FILES.get('excel')
            excel_name = excelFile.name
            path = default_storage.save(excel_name, ContentFile(excelFile.read()))
            tmp_file = os.path.join(MEDIA_ROOT, path)
            read_read_excel_seo.delay(tmp_file, excel_name)
        return super(SEOCustomerAdmin, self).post(request, args, kwargs)


xadmin.site.register(SEOCustomer, SEOCustomerAdmin)




#业支导入资料
class FormCustomerImportAdmin(object):
    list_display = ('company_name', 'url', 'company_type', 'phone', 'qq', 'wechat', 'city', 'address', 'remark', 'create_time', )
    list_filter = ('company_name', 'create_time', 'city', )
    search_fields = ('company_name', )
    list_per_page = 20
    readonly_fields = ['create_time', 'sem_status', ]
    exclude = ['randid', 'useless_counter', ] #不显示列
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    import_excel = True
    model_icon = 'fa fa-download'

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
        return super(FormCustomerImportAdmin, self).get_form_layout()



    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            excelFile = request.FILES.get('excel')
            excel_name = excelFile.name
            path = default_storage.save(excel_name, ContentFile(excelFile.read()))
            tmp_file = os.path.join(MEDIA_ROOT, path)
            read_excel.delay(tmp_file, excel_name)
        return super(FormCustomerImportAdmin, self).post(request, args, kwargs)
xadmin.site.register(FormCustomerImport, FormCustomerImportAdmin)

#最新资料，销售经理可用
class NewFormCustomerAdmin(object):
    list_display = ('company_name', 'url', 'company_type', 'phone', 'qq', 'wechat', 'city', 'address', 'remark', 'create_time', )
    list_filter = ('company_name', 'create_time', 'city', )
    search_fields = ('company_name', )
    list_per_page = 20
    readonly_fields = ['create_time', ]
    exclude = ['randid', 'useless_counter', 'sem_status', 'aike_status', 'depart', 'sales', 'business', 'keyword', 'update_time', 'amount']
    show_bookmarks = False #屏蔽书签
    list_export = ('xls', )
    model_icon = 'fa fa-level-up'

    def has_change_permission(request, obj=None):
        return False
    def has_delete_permission(request, obj=None):
        return False

    def queryset(self):
        user_id = self.user.id
        user_name = self.user.username
        qs = super(NewFormCustomerAdmin, self).queryset()
        if self.user.is_superuser:
            return qs.filter(randid__in=get_new_customer_data_to_admin())
        else:
            sm_id = get_sale_manager_id()
            if user_id in sm_id:
                dict_work = get_saleManager_data()
                if dict_work:
                    dict_key = str(user_id)+user_name
                    manage_randid_list = dict_work[dict_key]
                    return qs.filter(randid__in=manage_randid_list)
            else:
                sale_id_list = get_sale_id()
                if user_id in sale_id_list:
                    randid_list = get_real_data(self.user.id, self.user.city.name)
                    return qs.filter(randid__in=randid_list)
                else:
                    return qs.filter(randid__in=get_new_customer_data_to_admin())


xadmin.site.register(NewFormCustomer, NewFormCustomerAdmin)

#成功案例
class SuccessCustomerAdmin(object):
    list_display = ('company_name', 'url', 'company_type', 'city', 'create_time', 'update_time')
    list_filter = ('company_name', 'create_time', 'city', )
    search_fields = ('company_name', )
    list_per_page = 20
    readonly_fields = ['create_time', 'sem_status', 'aike_status', 'depart', 'sales', 'business', 'keyword', 'update_time', 'amount']
    exclude = ['randid', 'useless_counter', 'phone', 'qq', 'wechat', 'remark', 'address', ] #不显示列
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    model_icon = 'fa fa-handshake-o'

    # 修改布局
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset(_('基本信息'),
                             'company_name', 'company_type', 'url', 'city', 'keyword',
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
        return super(SuccessCustomerAdmin, self).get_form_layout()

    def queryset(self):
        qs = super(SuccessCustomerAdmin, self).queryset()
        return qs.filter(sem_status=1)
xadmin.site.register(SuccessCustomer, SuccessCustomerAdmin)


class SeoSaleWorkAdmin(object):
    list_display = ('company_name', 'company_type', 'link_man', 'tel_phone', 'mobile_phone', 'address', 'aike_status', 'seo_status', 'prefecture_level_city', 'create_date', )
    list_filter = ('company_name', 'create_date', 'prefecture_level_city', )
    search_fields = ('company_name', )
    list_per_page = 20
    exclude = ['rand_id', 'channel', 'level', ] #不显示列
    show_bookmarks = False #屏蔽书签
    list_export = ()#设置不显示导出按钮
    model_icon = 'fa fa-star-half-o'
    # 修改布局
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset(_('基本信息'),
                             'company_name', 'company_type', 'url', 'legal_man', 'issue_date', 'registration_authority',
                             ),
                    Fieldset(_('联系人物'),
                             'link_man', 'sex', 'job', 'is_boss', 'isboss_mobile',
                             ),
                    Fieldset(_('联系方式'),
                             'tel_phone', 'mobile_phone', 'mobile_phone_address', 'mobile_carrieroperator', 'zip_code'
                             ),
                    Fieldset(_('主要经营'),
                             'scope_business', 'business_position', 'produce_address',
                             ),
                    Fieldset(_('地址详情'),
                             'province', 'prefecture_level_city', 'county_district', 'address',
                             ),
                    Fieldset(_('注册日期'),
                             'register_year', 'register_month', 'register_date',
                             ),
                    Fieldset(_('财务信息'),
                             'finance_principal', 'finance_principal_mobile',
                             ),
                    Fieldset(_('意向信息'),
                             'seo_status', 'aike_status',
                             ),
                    Fieldset(_('时间信息'),
                             'create_date', 'update_date',
                             ),
                ),
                Side(

                )
            )
        return super(SeoSaleWorkAdmin, self).get_form_layout()

    def queryset(self):
        qs = super(SeoSaleWorkAdmin, self).queryset()
        user_id = self.user.id
        seo_sale_id = get_seo_sale_id()
        if user_id in seo_sale_id:
            rand_id_list = get_seo_sale_work(self.user.id)
            return qs.filter(rand_id__in=rand_id_list)
        else:
            return qs
xadmin.site.register(SeoSaleWork, SeoSaleWorkAdmin)