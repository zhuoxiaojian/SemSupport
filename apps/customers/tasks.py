# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 10:22
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : tasks.py
# @Software: PyCharm
from celery import task
from utils.getNeedDatas import get_sale
from citys.models import FormRegionCity
from  customers.models import FormCustomer
from django.db.models import Q
from utils.DateFormatUtil import get_today,get_before_oneweek
from utils.getNeedDatas import get_count,write_count
from works.models import customerUser
import time
SalecountNum = 250

@task
def divide_the_work():
    print("==================================开始分配任务===================================")
    date_from = '2017-01-01 00:00:00'
    date_to = get_before_oneweek()
    saleUser = get_sale()
    count = int(get_count())
    #根据城市分配
    frcDatas = FormRegionCity.objects.all()
    if frcDatas.exists():
        for frcData in frcDatas:
            city = frcData.name
            #将销售人员的id存在list
            s_user_id = []
            if saleUser.exists():
                for s_user in saleUser:
                    if s_user.city.name == city:
                        s_user_id.append(s_user.id)
            #进行复杂的Q对象查询
            q_query = FormCustomer.objects.filter(Q(city=frcData.name) | Q(city__isnull=True), Q(create_time__range=(date_from, date_to)) | Q(create_time__isnull=True), sem_status=0, aike_status=0).order_by('randid')
            # print(q_query.query)
            if q_query.exists():
                frcDataByCityCount = q_query.count()
                if frcDataByCityCount > SalecountNum:
                    frcDataByCityCount = frcDataByCityCount - SalecountNum
                if len(s_user_id) > 0:
                    for i in s_user_id:
                        result = SalecountNum * (i + count) % frcDataByCityCount
                        #print("===============result:"+str(result)+"=============city:"+city)
                        q_randid = FormCustomer.objects.filter(Q(city=frcData.name) | Q(city__isnull=True), Q(create_time__range=(date_from, date_to)) | Q(create_time__isnull=True), sem_status=0, aike_status=0).order_by('randid')[(result-1):result]
                        #print(q_randid.query)
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
                                customerUser.objects.create(user_id=user_id_now, customer_id=q_randid_id, create_time=create_time_now)
                        # time.sleep(2)
    write_count(str(count+1))
    print("==================================任务分配完毕===================================")







