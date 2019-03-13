# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 19:33
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : tasks.py
# @Software: PyCharm
from celery import task
from utils.DateFormatUtil import get_today
from .models import BackUpWork
import datetime
@task
def back_up_work(user_id, user_name, sql_str):
    now_time = str(get_today())
    buw = BackUpWork.objects.filter(user_id=user_id, create_time=now_time)
    if buw.exists():
        BackUpWork.objects.filter(user_id=user_id, create_time=now_time).\
            update(sql_str=sql_str, update_time=datetime.datetime.now(), user_name=user_name)
    else:
        BackUpWork.objects.create(user_id=user_id, create_time=now_time, sql_str=sql_str, user_name=user_name)
