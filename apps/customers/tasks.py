# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 10:22
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : tasks.py
# @Software: PyCharm
from celery import task
from utils.getNeedDatas import get_sale, get_seo_sale
from citys.models import FormRegionCity
from customers.models import FormCustomer, SEOCustomer
from django.db.models import Q, F
from utils.DateFormatUtil import get_today, get_before_oneweek, true_month_handle
from utils.getNeedDatas import get_count, write_count, getHandleCityList, getFilterCityList
from works.models import customerUser
import time
import datetime
from utils.getConstantsUtil import getConstantsVale
# SalecountNum = 250
# SEOInfoNum = 250

@task
def divide_the_work():

    print("==================================开始分配任务===================================")
    SalecountNum_str = getConstantsVale('smsNum')
    if SalecountNum_str is None:
        SalecountNum_str = 250
    SalecountNum = int(SalecountNum_str)
    date_from = getConstantsVale('dateForm')
    if date_from is None:
        date_from = '2017-01-01 00:00:00'
    # date_to = get_before_oneweek()
    saleUser = get_sale()
    count = int(get_count())

    # -----------------work_two------------------------
    handleMonth = getConstantsVale('handleMonth')
    if handleMonth is None:
        handleMonth = 7
    date_from_two = str(true_month_handle(datetime.datetime.now(), int(handleMonth)))
    date_to_two = get_today()
    SalecountNum_two_str = getConstantsVale('smsNewNum')
    if SalecountNum_two_str is None:
        SalecountNum_two_str = 250
    SalecountNum_two = int(SalecountNum_two_str)

    SalecountNum_three_str = getConstantsVale('smsRemoteNum')
    if SalecountNum_three_str is None:
        SalecountNum_three_str = 250
    SalecountNum_three = int(SalecountNum_three_str)
    # -----------------work_two------------------------

    handleCity = getHandleCityList()
    filterCity = getFilterCityList()
    #根据城市分配
    frcDatas = FormRegionCity.objects.all()
    if frcDatas.exists():
        for frcData in frcDatas:
            if frcData.name in handleCity:
                work_two(frcData, saleUser, date_from, date_to_two, date_from_two, date_to_two, SalecountNum_two, count)
            elif frcData.name == '远程':
                work_three(filterCity, saleUser, date_from, date_to_two, date_from_two, date_to_two, SalecountNum_three, count)
            else:
                work_one(frcData, saleUser, date_from, date_to_two, date_from_two, date_to_two, SalecountNum, count)

    write_count(str(count+1))
    print("==================================任务分配完毕===================================")

# 分配方式1 按照discover_time 深圳
def work_one(frcData, saleUser, date_from, date_to, date_from_two, date_to_two, SalecountNum, count):
    city = frcData.name
    #将销售人员的id存在list
    s_user_id = []
    if saleUser.exists():
        for s_user in saleUser:
            if s_user.city.name == city:
                s_user_id.append(s_user.id)
    #进行复杂的Q对象查询
    q_query = FormCustomer.objects.filter(Q(city=city), Q(discover_time__range=(date_from_two, date_to_two)),
                                          Q(create_time__range=(date_from, date_to)) | Q(create_time__isnull=True),
                                          sem_status=0, aike_status=0).order_by('randid')
    # print(q_query.query)
    if q_query.exists():
        frcDataByCityCount = q_query.count()
        if frcDataByCityCount > SalecountNum:
            frcDataByCityCount = frcDataByCityCount - SalecountNum
        if len(s_user_id) > 0:
            for i in s_user_id:
                result = SalecountNum * (i + count) % frcDataByCityCount
                new_reslut = result - 1
                if new_reslut <= 0:
                    result = 1
                q_randid = FormCustomer.objects.filter(Q(city=city),
                                                       Q(discover_time__range=(date_from_two, date_to_two)),
                                                       Q(create_time__range=(date_from, date_to)) |
                                                       Q(create_time__isnull=True),
                                                       sem_status=0, aike_status=0
                                                       ).order_by('randid')[(result-1):result]
                # print(q_randid.query)
                if q_randid.exists():
                    q_randid_id = q_randid[0].randid
                    create_time_now = str(get_today())
                    user_id_now = i
                    query_cc = customerUser.objects.filter(user_id=user_id_now, create_time=create_time_now)
                    #print(query_cc.query)
                    if query_cc.exists():
                        query_c = query_cc[0]
                        id_now = query_c.id
                        customerUser.objects.filter(id=id_now).update(customer_id=q_randid_id)
                    else:
                        customerUser.objects.create(user_id=user_id_now, customer_id=q_randid_id,
                                                    create_time=create_time_now)

# 分配方式1 按照create_time
# def work_one(frcData, saleUser, date_from, date_to, SalecountNum, count):
#     city = frcData.name
#     #将销售人员的id存在list
#     s_user_id = []
#     if saleUser.exists():
#         for s_user in saleUser:
#             if s_user.city.name == city:
#                 s_user_id.append(s_user.id)
#     #进行复杂的Q对象查询
#     q_query = FormCustomer.objects.filter(Q(city=frcData.name) | Q(city__isnull=True),
#                                           Q(create_time__range=(date_from, date_to)) | Q(create_time__isnull=True),
#                                           sem_status=0, aike_status=0).order_by('randid')
#     # print(q_query.query)
#     if q_query.exists():
#         frcDataByCityCount = q_query.count()
#         if frcDataByCityCount > SalecountNum:
#             frcDataByCityCount = frcDataByCityCount - SalecountNum
#         if len(s_user_id) > 0:
#             for i in s_user_id:
#                 result = SalecountNum * (i + count) % frcDataByCityCount
#                 new_reslut = result - 1
#                 if new_reslut <= 0:
#                     result = 1
#                 #print("===============result:"+str(result)+"=============city:"+city)
#                 q_randid = FormCustomer.objects.filter(Q(city=frcData.name) | Q(city__isnull=True),
#                                                        Q(create_time__range=(date_from, date_to))
#                                                        | Q(create_time__isnull=True), sem_status=0,
#                                                        aike_status=0).order_by('randid')[(result-1):result]
#                 # print(q_randid.query)
#                 if q_randid.exists():
#                     q_randid_id = q_randid[0].randid
#                     create_time_now = str(get_today())
#                     user_id_now = i
#                     query_cc = customerUser.objects.filter(user_id=user_id_now, create_time=create_time_now)
#                     #print(query_cc.query)
#                     if query_cc.exists():
#                         query_c = query_cc[0]
#                         id_now = query_c.id
#                         customerUser.objects.filter(id=id_now).update(customer_id=q_randid_id)
#                     else:
#                         customerUser.objects.create(user_id=user_id_now, customer_id=q_randid_id, create_time=create_time_now)

# 分配方式2 按照discover_time
def work_two(frcData, saleUser, date_from, date_to, date_from_two, date_to_two, SalecountNum, count):
    city = frcData.name
    city_list = getHandleCityList()
    #将销售人员的id存在list
    s_user_id = []
    if saleUser.exists():
        for s_user in saleUser:
            # if s_user.city.name == city:
            if s_user.city.name in city_list:
                s_user_id.append(s_user.id)
    #进行复杂的Q对象查询
    q_query = FormCustomer.objects.filter(Q(city__in=city_list), Q(discover_time__range=(date_from_two, date_to_two)),
                                          Q(create_time__range=(date_from, date_to)) | Q(create_time__isnull=True),
                                          sem_status=0, aike_status=0).order_by('randid')
    # print(q_query.query)
    if q_query.exists():
        frcDataByCityCount = q_query.count()
        if frcDataByCityCount > SalecountNum:
            frcDataByCityCount = frcDataByCityCount - SalecountNum
        if len(s_user_id) > 0:
            for i in s_user_id:
                result = SalecountNum * (i + count) % frcDataByCityCount
                new_reslut = result - 1
                if new_reslut <= 0:
                    result = 1
                #print("===============result:"+str(result)+"=============city:"+city)
                q_randid = FormCustomer.objects.filter(Q(city__in=city_list),
                                                       Q(discover_time__range=(date_from_two, date_to_two)),
                                                       Q(create_time__range=(date_from, date_to)) |
                                                       Q(create_time__isnull=True),
                                                       sem_status=0, aike_status=0
                                                       ).order_by('randid')[(result-1):result]
                # print(q_randid.query)
                if q_randid.exists():
                    q_randid_id = q_randid[0].randid
                    create_time_now = str(get_today())
                    user_id_now = i
                    query_cc = customerUser.objects.filter(user_id=user_id_now, create_time=create_time_now)
                    #print(query_cc.query)
                    if query_cc.exists():
                        query_c = query_cc[0]
                        id_now = query_c.id
                        customerUser.objects.filter(id=id_now).update(customer_id=q_randid_id)
                    else:
                        customerUser.objects.create(user_id=user_id_now, customer_id=q_randid_id,
                                                    create_time=create_time_now)

# 分配方式3 除去广州，佛山，深圳的资料
def work_three(filterCity, saleUser, date_from, date_to, date_from_two, date_to_two, SalecountNum, count):
    #将销售人员的id存在list
    s_user_id = []
    if saleUser.exists():
        for s_user in saleUser:
            if s_user.city.name == '远程':
                s_user_id.append(s_user.id)
    #进行复杂的Q对象查询
    q_query = FormCustomer.objects.filter(~Q(city__in=filterCity), Q(discover_time__range=(date_from_two, date_to_two)),
                                          Q(create_time__range=(date_from, date_to)) | Q(create_time__isnull=True),
                                          sem_status=0, aike_status=0).order_by('randid')
    # print(q_query.query)
    if q_query.exists():
        frcDataByCityCount = q_query.count()
        if frcDataByCityCount > SalecountNum:
            frcDataByCityCount = frcDataByCityCount - SalecountNum
        if len(s_user_id) > 0:
            for i in s_user_id:
                result = SalecountNum * (i + count) % frcDataByCityCount
                new_reslut = result - 1
                if new_reslut <= 0:
                    result = 1
                q_randid = FormCustomer.objects.filter(~Q(city__in=filterCity),
                                                       Q(discover_time__range=(date_from_two, date_to_two)),
                                                       Q(create_time__range=(date_from, date_to)) |
                                                       Q(create_time__isnull=True),
                                                       sem_status=0, aike_status=0
                                                       ).order_by('randid')[(result-1):result]
                # print(q_randid.query)
                if q_randid.exists():
                    q_randid_id = q_randid[0].randid
                    create_time_now = str(get_today())
                    user_id_now = i
                    query_cc = customerUser.objects.filter(user_id=user_id_now, create_time=create_time_now)
                    #print(query_cc.query)
                    if query_cc.exists():
                        query_c = query_cc[0]
                        id_now = query_c.id
                        customerUser.objects.filter(id=id_now).update(customer_id=q_randid_id)
                    else:
                        customerUser.objects.create(user_id=user_id_now, customer_id=q_randid_id,
                                                    create_time=create_time_now)

#定时更新已分配的SEO资料的level（轮换数）
@task
def update_seo_level():
    #ORDER BY  level asc,create_date desc,rand_id desc limit 250
    print("============================开始更新level标签================================")
    SEOInfoNum_str = getConstantsVale('seoNum')
    if SEOInfoNum_str is None:
        SEOInfoNum_str = str(250)
    SEOInfoNum = int(SEOInfoNum_str)

    seo_sale = get_seo_sale()

    #根据城市分配
    frcDatas = FormRegionCity.objects.all()
    if frcDatas.exists():
        for city in frcDatas:
            if seo_sale.exists():
                for seo in seo_sale:
                    seo_sale_id = []
                    if(seo.city==city):
                        seo_sale_id.append(seo.id)
                    if len(seo_sale_id) > 0:
                        num = len(seo_sale_id)
                        limitNum = num * SEOInfoNum
                        update_city = city.name
                        q = SEOCustomer.objects.filter(Q(seo_status=0), Q(aike_status=0),
                                                       Q(mobile_phone__isnull=False),
                                                       prefecture_level_city__icontains=update_city).order_by('level',
                                                                                                   '-create_date',
                                                                                                   '-rand_id'
                                                                                                   )[0:limitNum]
                        # print(q.query)
                        if q.exists():
                            for qs in q:
                                u_l = SEOCustomer.objects.get(id=qs.id)
                                u_l.level = u_l.level + 1
                                u_l.update_date = datetime.datetime.now()
                                u_l.save()
    #将无效资料的手机号置空
    SEOCustomer.objects.filter(seo_flag=0).update(mobile_phone=None)
    print("============================更新level标签结束================================")


#定时更新SEM资料轮换次数
@task
def update_sem_level():
    print("============================SEM：开始更新level标签================================")
    date_from = getConstantsVale('dateForm')
    if date_from is None:
        date_from = '2017-01-01 00:00:00'
    date_to = get_before_oneweek()
    SEMInfoNum_str = getConstantsVale('smsNum')
    if SEMInfoNum_str is None:
        SEMInfoNum_str = str(250)
    SEMInfoNum = int(SEMInfoNum_str)

    sem_sale = get_sale()

    #根据城市分配
    frcDatas = FormRegionCity.objects.all()
    if frcDatas.exists():
        for city in frcDatas:
            if sem_sale.exists():
                for sem in sem_sale:
                    sem_sale_id = []
                    if(sem.city==city):
                        sem_sale_id.append(sem.id)
                    if len(sem_sale_id) > 0:
                        num = len(sem_sale_id)
                        limitNum = num * SEMInfoNum
                        q = FormCustomer.objects.filter(Q(sem_status=0),
                                                        Q(aike_status=0),
                                                        Q(create_time__range=(date_from, date_to)) | Q(create_time__isnull=True),
                                                        city=city).order_by('level',
                                                                            '-randid',
                                                                            'create_time'
                                                                            )[0:limitNum]
                        # print(q.query)
                        if q.exists():
                            for qs in q:
                                u_l = FormCustomer.objects.get(id=qs.id)
                                u_l.level = u_l.level + 1
                                u_l.update_time = datetime.datetime.now()
                                u_l.save()
    print("============================更新SEM的level标签结束================================")




