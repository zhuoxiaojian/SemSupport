# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 14:07
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : tasks.py
# @Software: PyCharm
from celery import task
from counts.models import FormCountTotal
from django.db import connection
from utils.DateFormatUtil import get_yesterday, get_today
from counts.models import FormCount
from counts.models import FormCountTotal
from users.models import UserProfile
from django.db.models import Q
import time
from datetime import datetime
from utils.getNeedDatas import get_sale_id
from departs.models import TSDepart
from django.db.models import Count
@task
def initData():
    get_init_today_data()
    get_init_yesterday_data()
    # yesterday = str(get_yesterday())
    # today = str(get_today())
    # cursor = connection.cursor()
    # cursor.execute("SELECT fc.user_id,fc.xs_name,DATE_FORMAT(fc.create_time,'%Y-%m-%d'),fc.depart_id,count(fc.hit_url) from counts_formcount fc WHERE (DATE_FORMAT(fc.create_time,'%Y-%m-%d')='"+yesterday+"' OR DATE_FORMAT(fc.create_time,'%Y-%m-%d')='"+today+"')  GROUP BY fc.user_id,fc.depart_id,DATE_FORMAT(fc.create_time,'%Y-%m-%d')")
    # datas = cursor.fetchall() #读取所有
    # if datas:
    #     for data in datas:
    #         user = UserProfile.objects.get(id=data[0])
    #         depart = UserProfile.objects.get(id=data[0]).depart
    #         text = data[2]
    #         new_date = datetime.strptime(text, '%Y-%m-%d')
    #         query_data = FormCountTotal.objects.filter(user=user, create_time=new_date, depart=depart)
    #         if query_data.exists():
    #             qdata = query_data[0]
    #             ft = FormCountTotal.objects.get(id=qdata.id)
    #             ft.url_count = data[4]
    #             ft.save()
    #         else:
    #             FormCountTotal.objects.create(user=user, xs_name=data[1], create_time=new_date, depart=depart, url_count=data[4])
    #         # time.sleep(2)

'''新版Q查询-统计今天的数据'''

def get_init_today_data():
    today = str(get_today())
    start_today = today+" 00:00:00"
    end_today = today+" 23:59:59"
    q_new_find = FormCount.objects.filter(Q(create_time__range=(start_today, end_today))).values_list('user', 'depart').annotate(Count('hit_url')).order_by()
    if q_new_find.exists():
        for q_f in q_new_find:
            user_id = q_f[0]
            depart_id = q_f[1]
            url_count = q_f[2]
            user = UserProfile.objects.get(id=user_id)
            xs_name = user.last_name+user.first_name
            depart = TSDepart.objects.get(id=depart_id)
            text = str(get_today())
            new_date = datetime.strptime(text, '%Y-%m-%d')
            query_data = FormCountTotal.objects.filter(user=user, create_time=new_date, depart=depart)
            if query_data.exists():
                qdata = query_data[0]
                ft = FormCountTotal.objects.get(id=qdata.id)
                ft.url_count = url_count
                ft.save()
            else:
                FormCountTotal.objects.create(user=user, create_time=new_date, depart=depart, xs_name=xs_name, url_count=url_count)

'''新版Q查询-统计昨天的数据'''

def get_init_yesterday_data():
    yesterday = str(get_yesterday())
    start_day = yesterday+" 00:00:00"
    end_day = yesterday+" 23:59:59"
    q_new_find = FormCount.objects.filter(Q(create_time__range=(start_day, end_day))).values_list('user', 'depart').annotate(Count('hit_url')).order_by()
    if q_new_find.exists():
        for q_f in q_new_find:
            user_id = q_f[0]
            depart_id = q_f[1]
            url_count = q_f[2]
            user = UserProfile.objects.get(id=user_id)
            xs_name = user.last_name+user.first_name
            depart = TSDepart.objects.get(id=depart_id)
            text = str(get_yesterday())
            new_date = datetime.strptime(text, '%Y-%m-%d')
            query_data = FormCountTotal.objects.filter(user=user, create_time=new_date, depart=depart)
            if query_data.exists():
                qdata = query_data[0]
                ft = FormCountTotal.objects.get(id=qdata.id)
                ft.url_count = url_count
                ft.save()
            else:
                FormCountTotal.objects.create(user=user, create_time=new_date, depart=depart, xs_name=xs_name, url_count=url_count)



#定时更新url点击表中的姓名，所在部门
@task
def update_name_depart():
    id_list = get_sale_id()
    sale_user = UserProfile.objects.filter(id__in=id_list)
    if sale_user.exists():
        for su in sale_user:
            user = su
            depart = su.depart
            up_name = user.last_name+user.first_name
            FormCount.objects.filter(user=user).update(xs_name=up_name, depart=depart)
            FormCountTotal.objects.filter(user=user).update(xs_name=up_name, depart=depart)


