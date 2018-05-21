# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 14:18
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : tasks.py
# @Software: PyCharm
from celery import task
from customers.models import FormCustomer
from django.db.models import Q, F
from django.db.models import Count, Min, Max, Sum
from addup.models import CountBySale, CountByDepart
from utils.DateFormatUtil import get_today, get_month_count, month_handle
import datetime
from users.models import UserProfile
@task
def count_by_sale():
    monthNum = get_month_count()
    for i in range(0, monthNum):
        oldDay = month_handle(i)
        oldDay_str = str(oldDay).split('-')
        o_year = oldDay_str[0]
        o_month = oldDay_str[1]
        total_list = FormCustomer.objects.filter(~Q(sales=''), Q(sales__isnull=False),
                                                 Q(create_time__year=o_year),
                                                 Q(create_time__month=o_month)).values('sales').annotate(
            total_amount=Sum('amount'),
            total_amountNum=Sum('sem_status'),
            total_business=Sum('business')
        ).order_by()
        if total_list:
            for total in total_list:
                sale = total.get('sales')
                total_amount = 0
                if not total.get('total_amount') is None:
                    total_amount = total.get('total_amount')
                total_business = 0
                if not total.get('total_business') is None:
                    total_business = total.get('total_business')
                total_amountNum = 0
                if not total.get('total_amountNum') is None:
                    total_amountNum = total.get('total_amountNum')
                CBS = CountBySale.objects.filter(Q(create_time__year=o_year),
                                                 Q(create_time__month=o_month),
                                                 sale=sale)
                if CBS.exists():
                    c_s = CountBySale.objects.get(id=CBS[0].id)
                    c_s.total_amountNum = total_amountNum
                    c_s.total_amount = total_amount
                    c_s.total_business = total_business
                    c_s.create_time = oldDay
                    c_s.save()
                    pass
                else:
                    CountBySale.objects.create(sale=sale,
                                               total_amount=total_amount,
                                               total_business=total_business,
                                               total_amountNum=total_amountNum,
                                               create_time=oldDay)

@task
def count_by_depart():
    monthNum = get_month_count()
    for i in range(0, monthNum):
        oldDay = month_handle(i)
        oldDay_str = str(oldDay).split('-')
        o_year = oldDay_str[0]
        o_month = oldDay_str[1]
        total_list = FormCustomer.objects.filter(~Q(depart=''), Q(depart__isnull=False),
                                                 Q(create_time__year=o_year),
                                                 Q(create_time__month=o_month)).values('depart').annotate(
            total_amount=Sum('amount'),
            total_amountNum=Sum('sem_status'),
            total_business=Sum('business')
        ).order_by()
        if total_list:
            for total in total_list:
                depart = total.get('depart')
                total_amount = 0
                if not total.get('total_amount') is None:
                    total_amount = total.get('total_amount')
                total_business = 0
                if not total.get('total_business') is None:
                    total_business = total.get('total_business')
                total_amountNum = 0
                if not total.get('total_amountNum') is None:
                    total_amountNum = total.get('total_amountNum')
                CBS = CountByDepart.objects.filter(Q(create_time__year=o_year),
                                                   Q(create_time__month=o_month),
                                                   depart=depart)
                if CBS.exists():
                    c_s = CountByDepart.objects.get(id=CBS[0].id)
                    c_s.total_amountNum = total_amountNum
                    c_s.total_amount = total_amount
                    c_s.total_business = total_business
                    c_s.create_time = oldDay
                    c_s.save()
                    pass
                else:
                    CountByDepart.objects.create(depart=depart,
                                                 total_amount=total_amount,
                                                 total_business=total_business,
                                                 total_amountNum=total_amountNum,
                                                 create_time=oldDay)

@task
def update_form_customer_depart():
    fc = FormCustomer.objects.filter(~Q(sales=''), Q(sales__isnull=False)).values('sales')
    if fc:
        for f in fc:
            sName = f.get('sales')
            users = UserProfile.objects.all()
            if users.exists():
                for u in users:
                    saleName = u.last_name+u.first_name
                    if sName == saleName:
                        departName = u.depart.departname
                        FormCustomer.objects.filter(sales=saleName).update(depart=departName)

    pass



