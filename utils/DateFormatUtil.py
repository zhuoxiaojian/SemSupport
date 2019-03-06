# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 9:03
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : DateFormatUtil.py
# @Software: PyCharm
import time
import datetime
from dateutil import rrule
from dateutil.relativedelta import relativedelta
def date_string():
    return time.strftime("%Y-%m-%d", time.localtime())

def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

def get_before_oneweek():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=6)
    oneweek = today - oneday
    return oneweek

def get_today():
    today = datetime.date.today()
    return today


#把字符串转成datetime
def string_toDatetime(string):
    #'%Y-%m-%d %H:%M:%S'
    return datetime.datetime.strptime(string, "%Y-%m-%d")

#获取两个日期之间相差的月份数
def get_month_count():
    d1 = string_toDatetime("2017-01-01")
    d2 = get_today()
    months = rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d2).count()
    return months


def month_handle(num):
    datetime_now = datetime.datetime.now()
    datetime_month_ago = datetime_now - relativedelta(months=num)
    return datetime_month_ago

def true_month_handle(datetime_now, num):
    datetime_month_ago = datetime_now - relativedelta(months=num)
    strArrays = str(datetime_month_ago).split('-')
    year_month = strArrays[0] + '-' + strArrays[1]
    day = strArrays[2].split(' ')[0]
    return year_month + '-' + day


if __name__ == '__main__':
    print(get_before_oneweek())
    print(true_month_handle(datetime.datetime.now(), 7))
    print(get_today())
