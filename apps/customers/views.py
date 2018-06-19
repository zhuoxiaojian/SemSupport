from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import JsonResponse
from counts.models import FormCount
from users.models import UserProfile
from utils.DateFormatUtil import date_string
import datetime
from utils.getNeedDatas import get_sale_id
from django.db.models import Q
from customers.models import FormCustomer, SEOCustomer
from django.contrib.auth.models import AnonymousUser
class formCustomerHandle(View):
    def get(self, request):
        msg = False
        sale_id_list = get_sale_id()
        user = request.user
        if user == AnonymousUser():
            pass
        else:
            user_id = request.user.id
            real_name = None
            depart = None
            if not user_id is None:
                user = UserProfile.objects.get(id=user_id)
                if not user is None:
                    real_name = user.last_name+user.first_name
                if not user.depart is None:
                    depart = user.depart

            url = request.GET.get('url')
            needId = request.GET.get('needId')
            action = request.GET.get('action')
            if action == 'handleUrl':
                if user_id in sale_id_list:
                    list_result = FormCount.objects.filter(Q(create_time__year=datetime.datetime.now().year), Q(create_time__month=datetime.datetime.now().month), Q(create_time__day=datetime.datetime.now().day), user=user, hit_url=url, depart=depart)
                    if list_result.exists():
                        result = list_result[0]
                        hit_count = result.hit_count
                        new_hit_count = hit_count + 1
                        oldFormCount = FormCount.objects.get(id=result.id)
                        oldFormCount.hit_count = new_hit_count
                        oldFormCount.create_time = datetime.datetime.now()
                        oldFormCount.save()
                        print('数据已经存在,已经执行更新')
                    else:
                        FormCount.objects.create(user=user, hit_url=url, xs_name=real_name, hit_count=1, depart=depart, create_time=datetime.datetime.now())
                    msg = True
            if action == 'handleSEMMobile':
                FormCustomer.objects.filter(id=int(needId)).update(phone=None)
                msg = True
        return JsonResponse({'success': msg})


class seoCustomerHandle(View):
    def get(self, request):
        msg = False
        user = request.user
        needId = request.GET.get('needId')
        action = request.GET.get('action')
        if user == AnonymousUser():
            pass
        else:
            if action == 'handleSEOFlagA':
                SEOCustomer.objects.filter(id=int(needId)).update(seo_flag=0)
                msg = True
            if action == 'handleSEOFlagB':
                SEOCustomer.objects.filter(id=int(needId)).update(seo_flag=1)
                msg = True
        return JsonResponse({'success': msg})
