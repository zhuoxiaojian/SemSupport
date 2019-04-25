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

# 获取昨天的时间点
def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

# 获取一周前的数据
def get_before_oneweek():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=6)
    oneweek = today - oneday
    return oneweek

# 获取今天的数据
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

# 获取昨天的一周前的时间点
def get_before_oneweek_yes():
    today = get_yesterday()
    oneday = datetime.timedelta(days=6)
    oneweek = today - oneday
    return oneweek

# 获取几天前的具体时间，返回单个时间点
def get_before_day(dayNum):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=dayNum)
    before_day = today - oneday
    return before_day

# 获取几天前的时间，dayNum = 2, [2019-04-24, 2019-04-23]
def get_more_day_before(dayNum):
    list_day = []
    try:
        today = datetime.date.today()
        for i in range(dayNum):
            oneday = datetime.timedelta(days=i+1)
            yesterday = today - oneday
            list_day.append(yesterday)
        return list_day
    except Exception as e:
        print(e)
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        list_day.append(yesterday)
        return list_day

if __name__ == '__main__':
    # print(get_before_oneweek())
    # print(true_month_handle(get_today(), 7))
    # print(get_today())
    # print(get_before_oneweek_yes())
    # print(get_before_day(2))
    print(get_more_day_before(2))
