# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 9:03
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : DateFormatUtil.py
# @Software: PyCharm
import time
import datetime
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


#把datetime转成字符串
def datetime_toString(dt):
        return dt.strftime("%Y-%m-%d-%H")

#把字符串转成datetime
def string_toDatetime(string):
        return datetime.datetime.strptime(string, "%Y-%m-%d-%H")

#把字符串转成datetime
def string_toDatetime_noFormat(string):
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
        return time.mktime(string_toDatetime(strTime).timetuple())

#把时间戳转成字符串形式
def timestamp_toString(stamp):
        return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))

#把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTim):
        return time.mktime(dateTim.timetuple())


if __name__ == '__main__':
    print(type(string_toDatetime_noFormat('2017-04-03 14:54:00')))
