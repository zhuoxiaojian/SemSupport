# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 10:09
# @Author  : zjj
# @Email   : 1933860854@qq.com
# @File    : readExcelUtil.py
# @Software: PyCharm

import xlrd
import os
from SemSupport.settings import MEDIA_ROOT
import random
from customers.models import FormCustomer, SEOCustomer
from celery import task
import datetime
MAX_VALUE = 2147483647

@task
def read_excel(excel_path, excel_real_name):
    #文件位置
    print("===================开始导入======================")
    tmp_file = os.path.join(MEDIA_ROOT, excel_real_name)
    if os.path.exists(excel_path):
        ExcelFile = xlrd.open_workbook(excel_path)
        sheet = ExcelFile.sheets()[0]
        excel_name = sheet.name
        rows_num = sheet.nrows
        cols_num = sheet.ncols
        print(excel_name, rows_num, cols_num)
        if rows_num > 0 and cols_num > 0:
            print("有数据")
            for i in range(1, rows_num):
                company_name = None
                url = None
                company_type = None
                phone = None
                qq = None
                wechat = None
                randid = random.randint(1, MAX_VALUE)
                aike_status = 0
                sem_status = 0
                useless_counter = 0
                city = None
                address = None
                remark = None
                keyword = None
                amount = 0
                depart = None
                sales = None
                business = 0
                for j in range(0, cols_num):
                    if "公司名" == sheet.cell_value(0, j):
                        company_name = sheet.cell_value(i, j)
                    if "公司类型" == sheet.cell_value(0, j):
                        company_type = sheet.cell_value(i, j)
                    if "手机号" == sheet.cell_value(0, j):
                        phone = sheet.cell_value(i, j)
                    if "QQ" == sheet.cell_value(0, j):
                        qq = sheet.cell_value(i, j)
                    if "微信号" == sheet.cell_value(0, j):
                        wechat = sheet.cell_value(i, j)
                    if "所在城市" == sheet.cell_value(0, j):
                        city = sheet.cell_value(i, j)
                    if "地址" == sheet.cell_value(0, j):
                        address = sheet.cell_value(i, j)
                    if "备注" == sheet.cell_value(0, j):
                        remark = sheet.cell_value(i, j)
                    if "公司域名" == sheet.cell_value(0, j):
                        url = sheet.cell_value(i, j)
                    if "爱客系统" == sheet.cell_value(0, j):
                        if str(sheet.cell_value(i, j)) != "":
                            aike_status = int(sheet.cell_value(i, j))
                    if "sem客户" == sheet.cell_value(0, j):
                        if str(sheet.cell_value(i, j)) != "":
                            sem_status = int(sheet.cell_value(i, j))
                    if "签单金额" == sheet.cell_value(0, j):
                        if str(sheet.cell_value(i, j)) != "":
                            amount = int(sheet.cell_value(i, j))
                    if "负责销售部门" == sheet.cell_value(0, j):
                        depart = sheet.cell_value(i, j)
                    if "负责销售人员" == sheet.cell_value(0, j):
                        sales = sheet.cell_value(i, j)
                    if "商机" == sheet.cell_value(0, j):
                        if str(sheet.cell_value(i, j)) != "":
                            business = int(sheet.cell_value(i, j))
                    if "搜索关键词" == sheet.cell_value(0, j):
                        keyword = sheet.cell_value(i, j)
                    if not company_name is None and company_name != "":
                        f_old_list = FormCustomer.objects.filter(company_name=company_name)
                        if f_old_list.exists():
                            f_old = f_old_list[0]
                            if not url is None and url != "":
                                f_old.url = url
                            if not phone is None and url != "":
                                f_old.phone = phone
                            if not remark is None and url != "":
                                f_old.remark = remark
                            if not address is None and address != "":
                                f_old.address = address
                            if not qq is None and qq != "":
                                f_old.qq = qq
                            if not wechat is None and wechat != "":
                                f_old.wechat = wechat
                            if not city is None and city != "":
                                f_old.city = city
                            if not company_type is None and company_type != "":
                                f_old.company_type = company_type
                            if not keyword is None and keyword != "":
                                f_old.keyword = keyword

                            f_old.depart = depart
                            f_old.business = business
                            f_old.amount = amount
                            f_old.sales = sales
                            f_old.sem_status = sem_status
                            f_old.aike_status = aike_status
                            f_old.update_time = datetime.datetime.now()
                            f_old.save()
                        else:
                            FormCustomer.objects.create(
                                company_name=company_name, url=url, city=city, company_type=company_type,
                                remark=remark, qq=qq, wechat=wechat, address=address, aike_status=aike_status,
                                sem_status=sem_status, sales=sales, depart=depart, amount=amount, business=business,
                                useless_counter=useless_counter, randid=randid, keyword=keyword, phone=phone,
                                create_time=datetime.datetime.now()
                            )

        os.remove(excel_path)
        print("===================导入完成======================")
        #获取整行或者整列的值
        # rows=sheet.row_values(2)#第三行内容
        # cols=sheet.col_values(1)#第二列内容
        # print(cols,rows)
        ##获取单元格内容
        # print(sheet.cell(1,0).value.encode('utf-8'))
        # print(sheet.cell_value(1,0).encode('utf-8'))
        # print(sheet.row(1)[0].value.encode('utf-8'))
        # #打印单元格内容格式
        # print(sheet.cell(1,0).ctype)


@task
def read_read_excel_seo(excel_path, excel_real_name):
    #文件位置
    print("===================开始导入SEO资料======================")
    tmp_file = os.path.join(MEDIA_ROOT, excel_real_name)
    if os.path.exists(excel_path):
        ExcelFile = xlrd.open_workbook(excel_path)
        sheet = ExcelFile.sheets()[0]
        excel_name = sheet.name
        rows_num = sheet.nrows
        cols_num = sheet.ncols
        print(excel_name, rows_num, cols_num)
        if rows_num > 0 and cols_num > 0:
            print("有数据")
            for i in range(1, rows_num):
                company_name = None
                legal_man = None
                tel_phone = None
                mobile_phone = None
                prefecture_level_city = None
                registration_authority = None
                produce_address = None
                finance_principal = None
                finance_principal_mobile = None
                rand_id = random.randint(1, MAX_VALUE)
                aike_status = 0
                seo_status = 0
                level = 0
                for j in range(0, cols_num):
                    if "纳税人名称" == sheet.cell_value(0, j):
                        company_name = sheet.cell_value(i, j)
                    if "法人" == sheet.cell_value(0, j):
                        legal_man = sheet.cell_value(i, j)
                    if "法人座机" == sheet.cell_value(0, j):
                        tel_phone = sheet.cell_value(i, j)
                    if "法人手机" == sheet.cell_value(0, j):
                        mobile_phone = sheet.cell_value(i, j)
                    if "城市" == sheet.cell_value(0, j):
                        prefecture_level_city = sheet.cell_value(i, j)
                    if "注册地址" == sheet.cell_value(0, j):
                        registration_authority = sheet.cell_value(i, j)
                    if "生产经营地址" == sheet.cell_value(0, j):
                        produce_address = sheet.cell_value(i, j)
                    if "财务负责人姓名" == sheet.cell_value(0, j):
                        finance_principal = sheet.cell_value(i, j)
                    if "财务负责人移动电话" == sheet.cell_value(0, j):
                        finance_principal_mobile = sheet.cell_value(i, j)
                    if "是否签约" == sheet.cell_value(0, j):
                        if str(sheet.cell_value(i, j)) != "":
                            seo_status = int(sheet.cell_value(i, j))
                    if "是否爱客" == sheet.cell_value(0, j):
                        if str(sheet.cell_value(i, j)) != "":
                            aike_status = int(sheet.cell_value(i, j))

                    if not company_name is None and company_name != "":
                        f_old_list = SEOCustomer.objects.filter(company_name=company_name)
                        if f_old_list.exists():
                            f_old = f_old_list[0]
                            if not legal_man is None and legal_man != "":
                                f_old.legal_man = legal_man
                            if not tel_phone is None and tel_phone != "":
                                f_old.tel_phone = tel_phone
                            if not mobile_phone is None and mobile_phone != "":
                                f_old.mobile_phone = mobile_phone
                            if not prefecture_level_city is None and prefecture_level_city != "":
                                f_old.prefecture_level_city = prefecture_level_city
                            if not registration_authority is None and registration_authority != "":
                                f_old.registration_authority = registration_authority
                            if not produce_address is None and produce_address != "":
                                f_old.produce_address = produce_address
                            if not finance_principal is None and finance_principal != "":
                                f_old.finance_principal = finance_principal
                            if not finance_principal_mobile is None and finance_principal_mobile != "":
                                f_old.finance_principal_mobile = finance_principal_mobile
                            f_old.aike_status = aike_status
                            f_old.seo_status = seo_status
                            f_old.update_date = datetime.datetime.now()
                            f_old.save()
                        else:
                            SEOCustomer.objects.create(company_name=company_name, aike_status=aike_status,
                                                       seo_status=seo_status, legal_man=legal_man,
                                                       prefecture_level_city=prefecture_level_city,
                                                       produce_address=produce_address,
                                                       tel_phone=tel_phone,
                                                       mobile_phone=mobile_phone,
                                                       registration_authority=registration_authority,
                                                       rand_id=rand_id,
                                                       level=level,
                                                       create_date=datetime.datetime.now(),
                                                       update_date=None)
        os.remove(excel_path)
        print("===================SEO资料导入完成======================")