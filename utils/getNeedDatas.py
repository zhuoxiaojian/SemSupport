# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 10:14
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : getAllSaleUser.py
# @Software: PyCharm
from django.contrib.auth.models import Group
from customers.models import FormCustomer, SEOCustomer
from django.db.models import Q
from utils.DateFormatUtil import get_before_oneweek, get_today
from works.models import customerUser
from citys.models import FormRegionCity
from users.models import UserProfile
import os
from django.db.models import Count, Min, Max, Sum
seo_info_num = 250
sem_info_num = 250
#获取所有销售人员
def get_sale():
    gp = Group.objects.filter(name='销售人员')
    if gp.exists():
        print("========销售人员角色组存在========")
    else:
        Group.objects.create(name='销售人员')

    group = Group.objects.get(name='销售人员')
    users = group.user_set.all()
    return users

#获取销售对应的资料
def get_real_data(user_id, city_name):
    date_from = '2017-01-01 00:00:00'
    date_to = get_before_oneweek()
    now_time = str(get_today())
    user_work = customerUser.objects.filter(user_id=user_id, create_time=now_time)
    randid_list = []
    if user_work.exists():
        q_randid = user_work[0].customer_id
        q_randid_list_data = FormCustomer.objects.filter(Q(randid__gte=q_randid), Q(city=city_name) | Q(city__isnull=True), Q(create_time__range=(date_from, date_to)) | Q(create_time__isnull=True), sem_status=0, aike_status=0).order_by('randid')[0:sem_info_num]
        # print(q_randid_list_data.query)
        if q_randid_list_data.exists():
            for qd in q_randid_list_data:
                randid_list.append(qd.randid)
    return randid_list


#获取所有的销售经理
def get_sale_manager():
    gp = Group.objects.filter(name='销售经理')
    if gp.exists():
        print("=============销售经理角色组存在==================")
    else:
        Group.objects.create(name='销售经理')

    group = Group.objects.get(name='销售经理')
    manage_users = group.user_set.all()
    return manage_users

#获取所有的销售人员id
def get_sale_id():
    sale_id = []
    gp = Group.objects.filter(name='销售人员')
    if gp.exists():
        print("========销售人员角色组存在========")
    else:
        Group.objects.create(name='销售人员')

    group = Group.objects.get(name='销售人员')
    if not group is None:
        manage_users = group.user_set.all()
        if manage_users.exists():
            for u in manage_users:
                sale_id.append(u.id)
    return sale_id

#获取所有的销售经理id
def get_sale_manager_id():
    sale_manager_id = []
    gp = Group.objects.filter(name='销售经理')
    if gp.exists():
        print("=============销售经理角色组存在==================")
    else:
        Group.objects.create(name='销售经理')

    group = Group.objects.get(name='销售经理')
    if not group is None:
        manage_users = group.user_set.all()
        if manage_users.exists():
            for u in manage_users:
                sale_manager_id.append(u.id)
    return sale_manager_id


#获取销售经理需要的资料
def get_saleManager_data():
    dict = {}
    sale_manager = get_sale_manager()
    sale_manager_flag = []
    if sale_manager.exists():
       for saleM in sale_manager:
           sale_manager_flag.append(str(saleM.id)+saleM.username)
       avg_count = len(sale_manager_flag)
       real_list_data = get_new_customer_data(avg_count)
       for flag in range(0, avg_count):
           dict[sale_manager_flag[flag]] = real_list_data[flag]
    return dict

#返回分好的数据
def get_new_customer_data(n):
    new_customer_data_list = []
    date_from = str(get_before_oneweek())
    date_to = str(get_today())
    q_query = FormCustomer.objects.filter(Q(create_time__range=(date_from, date_to)), sem_status=0, aike_status=0).order_by('randid')
    if q_query.exists():
        for qc in q_query:
            new_customer_data_list.append(qc.randid)
    return averageAssing(new_customer_data_list, n)

#将全部最新资料返回给admin
def get_new_customer_data_to_admin():
    new_customer_data_list = []
    date_from = str(get_before_oneweek())
    date_to = str(get_today())
    q_query = FormCustomer.objects.filter(Q(create_time__range=(date_from, date_to)), sem_status=0, aike_status=0).order_by('randid')
    if q_query.exists():
        for qc in q_query:
            new_customer_data_list.append(qc.randid)
    return new_customer_data_list


#将list平均分
def averageAssing(list, n):
    result = []
    remaider = len(list) % n
    number = len(list)//n
    offset = 0
    for i in range(0, n):
        value = None
        if remaider > 0:
            start_index = i*number+offset
            end_index = (i+1)*number+offset+1
            value = list[start_index:end_index]
            remaider = remaider-1
            offset = offset + 1
        else:
            start_index_e = i*number+offset
            end_index_e = (i+1)*number+offset
            value = list[start_index_e:end_index_e]
        result.append(value)
    return result

#得到记录下来的count
def get_count():
    count_path = "/var/log/django/SEMInfo/count.txt"
    count_path_parent = "/var/log/django/SEMInfo"
    count = "0"
    if os.path.exists(count_path_parent):
        if os.path.exists(count_path):
            f = open(count_path, "r")
            count = f.read()
            if count == "" or count is None:
                count = "0"
            f.close()
            pass
    else:
        os.mkdir(count_path_parent)
        f = open(count_path, "w")
        f.write("0")
        f.close()

    return count

#将新count写进文件
def write_count(count_num):
    count_path = "/var/log/django/SEMInfo/count.txt"
    f = open(count_path, "w")
    f.write(str(count_num))
    f.close()

def get_addup_depart():
    total_list = FormCustomer.objects.filter(depart__isnull=False).values('depart').annotate(total_amount=Sum('amount'), total_amountNum=Sum('sem_status'), total_business=Sum('business')).order_by()
    print("==================================")
    print(total_list.query)
    if total_list.exists():
        for tl in total_list:
            print(tl['depart'])
        return total_list
    return None

#获取所有的SEO销售人员
def get_seo_sale():
    gp = Group.objects.filter(name='SEO销售人员')
    if gp.exists():
        print("=============SEO销售人员角色组存在==================")
    else:
        Group.objects.create(name='SEO销售人员')

    group = Group.objects.get(name='SEO销售人员')
    seo_users = group.user_set.all()
    return seo_users

#获取所有的SEO销售人员的id
def get_seo_sale_id():
    seo_sale_id = []
    gp = Group.objects.filter(name='SEO销售人员')
    if gp.exists():
        print("=============SEO销售人员角色组存在==================")
    else:
        Group.objects.create(name='SEO销售人员')

    group = Group.objects.get(name='SEO销售人员')
    if not group is None:
        seo_users = group.user_set.all()
        if seo_users.exists():
            for u in seo_users:
                seo_sale_id.append(u.id)
    return seo_sale_id


#分配SEO销售人员对应的资料
def divide_seo_slae_work():
    dict = {}
    seo_sales = get_seo_sale()
    citys = FormRegionCity.objects.all()
    if citys.exists():
        for city in citys:
            seo_sale_id = []
            if seo_sales.exists():
                for seo_sale in seo_sales:
                    if seo_sale.city.name == city.name:
                        seo_sale_id.append(seo_sale.id)
            if len(seo_sale_id) > 0:
                result_list = []
                num = len(seo_sale_id)
                limitNum = num * seo_info_num
                seo_datas = SEOCustomer.objects.filter(Q(seo_status=0), Q(aike_status=0),
                    prefecture_level_city__icontains=city.name).values('rand_id').\
                                                                                order_by('level',
                                                                                '-create_date',
                                                                                '-rand_id'
                                                                                )[0:limitNum]
                if seo_datas.exists():
                    seo_data_list = []
                    for seo_data in seo_datas:
                        seo_data_list.append(seo_data)
                    result_list = averageAssing(seo_data_list, num)
                if len(result_list) > 0:
                    count = 0
                    for id in seo_sale_id:
                        user = UserProfile.objects.get(id=id)
                        if not user is None:
                            dict[str(id)+user.username] = result_list[count]
                            count = count + 1
    return dict

#获取SEO销售人员对应的资料
def get_seo_sale_work(userId):
    rand_id_list = []
    user = UserProfile.objects.get(id=userId)
    dict = divide_seo_slae_work()
    if not user is None:
        key = str(userId)+user.username
        if dict:
            rand_id = dict.get(key)
            for rand in rand_id:
                rand_id_list.append(rand.get('rand_id'))
    return rand_id_list




















