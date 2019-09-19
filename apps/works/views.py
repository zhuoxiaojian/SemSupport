from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from customers.tasks import divide_the_work
from django.http import JsonResponse
from works.models import BackUpWork
from utils.DateFormatUtil import get_today

class OneKeyInitWork(View):
    def get(self, request):
        user = request.user
        if user == AnonymousUser():
            return JsonResponse({"msg": "请登录后重试！！"})
        divide_the_work()
        return JsonResponse({"msg": "任务分配成功！！"})


class OneKeyClearWork(View):
    def get(self, request):
        user = request.user
        if user == AnonymousUser():
            return JsonResponse({"msg": "请登录后重试！！"})
        today_str = str(get_today())
        BackUpWork.objects.filter(create_time=today_str).delete()
        return JsonResponse({"msg": "当天任务备份清空成功！！"})
