from django.db import models

# Create your models here.
from datetime import datetime
import sys
import random
from django.utils import timezone
from django.utils.safestring import mark_safe
MAX_VALUE = 2147483647

class FormCustomer(models.Model):
    aike_status_level = ((0, u'否'), (1, u'是'))
    # sem_status_level = ((0, u'否'), (1, u'是'))
    company_name = models.CharField(max_length=255,  verbose_name='公司名', unique=True)
    url = models.CharField(max_length=255, verbose_name='公司域名', null=True, blank=True)
    company_type = models.CharField(max_length=255, verbose_name='公司类型', null=True, blank=True)
    phone = models.TextField(verbose_name='手机号', null=True, blank=True)
    qq = models.CharField(max_length=255, verbose_name='QQ', null=True, blank=True)
    wechat = models.CharField(max_length=255, verbose_name='微信号', null=True, blank=True)
    aike_status = models.IntegerField(verbose_name='爱客系统', default=0, choices=aike_status_level)
    sem_status = models.IntegerField(verbose_name='sem客户', default=0)
    useless_counter = models.IntegerField(verbose_name='无效次数', default=0)
    city = models.CharField(max_length=255, verbose_name='所在城市', null=True, blank=True)
    address = models.TextField(verbose_name='地址', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='首次发现', default=datetime.now, blank=True)
    update_time = models.DateTimeField(verbose_name='最后更新', blank=True, null=True, default=None)
    remark = models.TextField(verbose_name='备注', blank=True, null=True)
    randid = models.BigIntegerField(db_index=True, verbose_name='随机数', default=random.randint(1, MAX_VALUE))
    keyword = models.CharField(max_length=255, verbose_name='搜索关键词', null=True, blank=True)
    amount = models.IntegerField(verbose_name='签单金额', null=True, blank=True, default=0)
    depart = models.CharField(max_length=255, verbose_name='负责销售部门', null=True, blank=True)
    sales = models.CharField(max_length=255, verbose_name='负责销售人员', null=True, blank=True)
    business = models.IntegerField(verbose_name='商机', default=0)
    level = models.IntegerField(verbose_name='轮换次数', default=0, null=False, blank=False)
    discover_time = models.DateTimeField(verbose_name='最近发现时间', null=True, blank=True)
    discover_count = models.IntegerField(verbose_name='发现次数', default=1, null=False, blank=False)

    class Meta:
        db_table = 'form_customer'
        verbose_name = '公司信息'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.company_name

    def change_button(self):
        return mark_safe('<a  class="btn btn-primary" onclick="handleSEMMobile'+str(self.id)+'();"><i class="fa fa-trash-o"></i>&nbsp;清空手机号</a><script type="text/javascript">function handleSEMMobile'+str(self.id)+'(){ $.ajax({url:"formCustomerHandle", data:{needId:'+str(self.id)+',action:"handleSEMMobile"},type:"GET", dataType:"json", success:function(returned, status, xhr){window.location.reload();}});}</script>')
    change_button.short_description = '操作'

    def change_url(self):
        # change_url.short_description = "公司域名"

        if self.url.__contains__('https:'):
            return mark_safe('<a href = "'+self.url+'" target="_blank" onclick="handleClick'+str(self.id)+'();">'+self.url+'</a><script type="text/javascript">function handleClick'+str(self.id)+'(){$.ajax({url:"formCustomerHandle", data:{url:"'+self.url+'",action:"handleUrl"},type:"GET",dataType:"json",success:function(returned, status, xhr){console.log(status);}});}</script>')
        else:
            if self.url.__contains__('http:'):
                return mark_safe('<a href = "'+self.url+'" target="_blank" onclick="handleClick'+str(self.id)+'();">'+self.url+'</a><script type="text/javascript">function handleClick'+str(self.id)+'(){$.ajax({url:"formCustomerHandle", data:{url:"'+self.url+'",action:"handleUrl"},type:"GET",dataType:"json",success:function(returned, status, xhr){console.log(status);}});}</script>')
            else:
                return mark_safe('<a href = "http://'+self.url+'" target="_blank" onclick="handleClick'+str(self.id)+'();">'+self.url+'</a><script type="text/javascript">function handleClick'+str(self.id)+'(){$.ajax({url:"formCustomerHandle", data:{url:"'+self.url+'",action:"handleUrl"},type:"GET",dataType:"json",success:function(returned, status, xhr){console.log(status);}});}</script>')
    change_url.short_description = "点击域名"

class SEOCustomer(models.Model):
    aike_status_level = ((0, u'否'), (1, u'是'))
    seo_status_level = ((0, u'否'), (1, u'是'))
    seo_flag = ((0, u'无效'), (1, u'有效'))
    company_name = models.CharField(max_length=255, verbose_name='公司名称', db_index=True)
    url = models.CharField(max_length=255, verbose_name='公司域名', null=True, blank=True)
    link_man = models.CharField(max_length=255, verbose_name='联系人', null=True, blank=True)
    sex = models.CharField(max_length=255, verbose_name='性别', null=True, blank=True)
    job = models.CharField(max_length=255, verbose_name='职务', null=True, blank=True)
    tel_phone = models.CharField(max_length=255, verbose_name='电话', null=True, blank=True)
    mobile_phone = models.CharField(max_length=255, verbose_name='手机', null=True, blank=True)
    mobile_phone_address = models.CharField(max_length=255, verbose_name='手机归属地', null=True, blank=True)
    mobile_carrieroperator = models.CharField(max_length=255, verbose_name='手机运营', null=True, blank=True)
    is_boss = models.CharField(max_length=255, verbose_name='是否老总', null=True, blank=True)
    isboss_mobile = models.CharField(max_length=255, verbose_name='老总手机', null=True, blank=True)
    legal_man = models.CharField(max_length=255, verbose_name='法定代表', null=True, blank=True)
    province = models.CharField(max_length=255, verbose_name='省份', null=True, blank=True)
    prefecture_level_city = models.CharField(max_length=255, verbose_name='地级市', null=True, blank=True)
    county_district = models.CharField(max_length=255, verbose_name='县区', null=True, blank=True)
    address = models.TextField(verbose_name='源地址', null=True, blank=True)
    zip_code = models.CharField(max_length=255, verbose_name='邮编', null=True, blank=True)
    company_type = models.CharField(max_length=255, verbose_name='公司类型', null=True, blank=True)
    register_year = models.CharField(max_length=255, verbose_name='注册年份', null=True, blank=True)
    register_month = models.CharField(max_length=255, verbose_name='注册月份', null=True, blank=True)
    register_date = models.CharField(max_length=255, verbose_name='注册日子', null=True, blank=True)
    scope_business = models.TextField(verbose_name='经营范围', null=True, blank=True)
    registration_authority = models.TextField(verbose_name='登记机关', null=True, blank=True)
    issue_date = models.CharField(max_length=255, verbose_name='核准日期', null=True, blank=True)
    business_position = models.TextField(verbose_name='经营现状', null=True, blank=True)
    aike_status = models.IntegerField(verbose_name='是否爱客', default=0, choices=aike_status_level)
    seo_status = models.IntegerField(verbose_name='是否签约', default=0, choices=seo_status_level)
    level = models.IntegerField(verbose_name='轮换次数', default=0)
    rand_id = models.IntegerField(db_index=True, verbose_name='随机数', default=random.randint(1, MAX_VALUE))
    create_date = models.DateTimeField(verbose_name='创建时间', default=datetime.now, blank=True)
    update_date = models.DateTimeField(verbose_name='更新时间', blank=True, null=True, default=None)
    produce_address = models.TextField(verbose_name='生产经营地址', blank=True, null=True)
    finance_principal = models.CharField(max_length=255, verbose_name='财务负责人姓名', blank=True, null=True)
    finance_principal_mobile = models.CharField(max_length=255, verbose_name='财务负责人移动电话', null=True, blank=True)

    #渠道1是原来的用户信息，渠道2是新导入的用户信息
    channel = models.CharField(max_length=255, verbose_name='来源渠道', null=True, blank=True)
    seo_flag = models.IntegerField(verbose_name="是否有效", null=False, blank=False, default=1, choices=seo_flag)

    class Meta:
        db_table = 'ys_seo_customer'
        verbose_name = 'seo资料库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company_name


class FormCustomerImport(FormCustomer):

    class Meta:
        verbose_name = '资料导入'
        verbose_name_plural = verbose_name
        proxy = True

    def __str__(self):
        return self.company_name


class NewFormCustomer(FormCustomer):

    class Meta:
        verbose_name = '最新资料'
        verbose_name_plural = verbose_name
        proxy = True

    def __str__(self):
        return self.company_name


class SuccessCustomer(FormCustomer):

    class Meta:
        verbose_name = '成功案例'
        verbose_name_plural = verbose_name
        proxy = True

    def __str__(self):
        return self.company_name

class SeoSaleWork(SEOCustomer):

    class Meta:
        verbose_name = 'SEO任务库'
        ordering = ['-create_date']
        verbose_name_plural = verbose_name
        proxy = True

    def __str__(self):
        return self.company_name

    def chang_flag(self):
        if self.seo_flag == 0:
            return mark_safe('<a class="btn btn-primary" onclick="handleSEOFlag'+str(self.id)+'B();">有效</a><script type="text/javascript">function handleSEOFlag'+str(self.id)+'B(){ $.ajax({url:"seoCustomerHandle", data:{needId:'+str(self.id)+',action:"handleSEOFlagB"},type:"GET", dataType:"json", success:function(returned, status, xhr){console.log(returned.success);window.location.reload();}});}</script>')
        if self.seo_flag == 1:
            return mark_safe('<a class="btn btn-danger" onclick="handleSEOFlag'+str(self.id)+'A();">无效</a><script type="text/javascript">function handleSEOFlag'+str(self.id)+'A(){ $.ajax({url:"seoCustomerHandle", data:{needId:'+str(self.id)+',action:"handleSEOFlagA"},type:"GET", dataType:"json", success:function(returned, status, xhr){window.location.reload();}});}</script>')

    chang_flag.short_description = '操作'