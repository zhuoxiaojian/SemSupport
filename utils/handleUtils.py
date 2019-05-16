# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 9:57
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : Utils.py
# @Software: PyCharm
from citys.models import City, Province, Area
from utils.getConstantsUtil import getConstantsValeOrDefault
from customers.models import FormCustomer
from django.db.models import Count, Q
class Utils(object):
    '''
      静态工具类
    '''


    @staticmethod
    def getDutyArea(filterCityList):
        '''
        获取远程销售负责的城市
        :param filterCityList:
        :return:
        '''

        # 接收库里已有的所有城市列表
        all_city_list = []
        # 默认返回列表
        default_area_list = ['东莞', '中山', '珠海', '惠州', '广东']
        # 返回指定列表
        area_list = []
        # 默认值：广东省
        handleProvinceList = getConstantsValeOrDefault('handleArea', '广东省').split(",")
        provinces = None
        if "全国" in handleProvinceList[0]:
            # group by city
            result_list = FormCustomer.objects.filter(~Q(city__isnull=True), ~Q(city=''), ~Q(city__contains='不'),
                                                      ~Q(city__contains='无效')
                                                      ).values('city').annotate(count=Count("city")
                                                                                ).order_by('city')
            if result_list:
                for result in result_list:
                    city_name = result['city']
                    if filterCityList:
                        if city_name not in filterCityList:
                            all_city_list.append(city_name)
                    else:
                        all_city_list.append(city_name)
            if all_city_list:
                return all_city_list
            else:
                provinces = Province.objects.all()
        elif "地区" in handleProvinceList[0]:
            area_id_list = []
            for areaName in handleProvinceList:
                area_model = Area.objects.filter(name=areaName)
                if area_model:
                    area_id_list.append(area_model[0].id)
            provinces = Province.objects.filter(area_id__in=area_id_list)
        else:
            provinces = Province.objects.filter(name__in=handleProvinceList)
        if provinces:
            for province in provinces:
                province_name = province.name
                area_list.append(province_name[:-1])
                citys = City.objects.filter(province=province.id)
                if citys:
                    for city in citys:
                        cityName = str(city.name)
                        real_name = None
                        if "自治州" in cityName:
                            real_name = cityName[:-3]
                        elif "地区" in cityName:
                            real_name = cityName[:-2]
                        else:
                            real_name = cityName[:-1]
                        if filterCityList:
                            if real_name not in filterCityList:
                                area_list.append(real_name)
                        else:
                            area_list.append(real_name)
        if area_list:
            return area_list
        else:
            return default_area_list