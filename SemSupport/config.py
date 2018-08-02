# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 16:14
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : config.py
# @Software: PyCharm
from datetime import timedelta
from SemSupport.settings import TIME_ZONE
# import djcelery
from celery.schedules import crontab
# djcelery.setup_loader()
#本地
# BROKER_URL = 'redis://:123456@127.0.0.1:6379/1'
# CELERY_RESULT_BAKEND = 'redis://:123456@127.0.0.1:6379/2'

#测试服
BROKER_URL = 'redis://:123456@sms_redis:6379/1'
CELERY_RESULT_BAKEND = 'redis://:123456@sms_redis:6379/2'

# celery内容等消息的格式设置
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# celery时区设置，使用settings中TIME_ZONE同样的时区
CELERY_TIMEZONE = TIME_ZONE
#CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24   # 任务过期时间
# 配置定时任务
# celery beat -A  SemSupport  启动定时任务
# celery -A SemSupport worker -l info  启动worker进程
CELERYBEAT_SCHEDULE={
    'init_hit_data': {
        'task': 'counts.tasks.initData',  # tasks.py模块下的getCamp方法
        'schedule': timedelta(seconds=5*60),      # 每隔1分钟运行一次
        # 'args': (23, 12),
    },
    'update_name_depart': {
        'task': 'counts.tasks.update_name_depart',
        'schedule': timedelta(seconds=30*60)
    },
    'init_work_data': {
        'task': 'customers.tasks.divide_the_work',
        #'schedule': timedelta(seconds=60)
        'schedule': crontab(minute=u'10,20,30', hour=u'17',),
    },
    'update_seo_level': {
        'task': 'customers.tasks.update_seo_level',
        'schedule': crontab(minute=u'55', hour=u'17', ),
    },
    'count_by_sale': {
        'task': 'addup.tasks.count_by_sale',
        'schedule': timedelta(seconds=5*60)
    },
    'count_by_depart': {
        'task': 'addup.tasks.count_by_depart',
        'schedule': timedelta(seconds=5*60)
    },
    'update_form_customer_depart': {
        'task': 'addup.tasks.update_form_customer_depart',
        'schedule': timedelta(seconds=30*60)
    }
}