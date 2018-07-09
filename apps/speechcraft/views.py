from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse
import json
from speechcraft.models import Speechcraft
from django.core.paginator import Paginator
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
# Create your views here.
def speechcraftshow(request):
    return render_to_response('speechcraftshow.html', {})

def checkLoginInfo(request):
    if request.method == "GET":
        message = ""
        if request.user == AnonymousUser():
            message = "fail"
            result_data = {'message': message}
            return HttpResponse(json.dumps(result_data))
        else:
            message = "success"
            result_data = {'message': message}
            return HttpResponse(json.dumps(result_data))

def getSpeechcraftInfo(request):
    if request.method == "GET":
        if request.user == AnonymousUser():
            response_data = {'total': 0, 'rows': []}
            return HttpResponse(json.dumps(response_data))
        else:
            limit = request.GET.get('limit')   # how many items per page
            offset = request.GET.get('offset')  # how many items in total in the DB
            labelSearch = request.GET.get('labelSearch')
            inputSearch = request.GET.get('inputSearch')
            handleType = request.GET.get('handleType')
            # sort_column = request.GET.get('sort')   # which column need to sort
            # order = request.GET.get('order')      # ascending or descending
            if labelSearch:    #    判断是否有搜索字
                if handleType == 'searchMethod' and inputSearch != "":
                    all_records = Speechcraft.objects.filter(Q(speechKeyword__icontains=inputSearch.replace(' ', '')) |
                                                             Q(speechAnswer__icontains=inputSearch.replace(' ', '')) |
                                                             Q(speechGoal__icontains=inputSearch.replace(' ', '')),
                                                             speechLabel__icontains=labelSearch.replace(' ', '')
                                                             ).order_by('-speechCreateTime')
                else:
                    all_records = Speechcraft.objects.filter(speechLabel__icontains=labelSearch.replace(' ', '')
                                                             ).order_by('-speechCreateTime')
            else:
                all_records = Speechcraft.objects.all().order_by('-speechCreateTime')

            all_records_count = all_records.count()

            if not offset:
                offset = 0
            if not limit:
                limit = 20    # 默认是每页20行的内容，与前端默认行数一致
            try:
                pageinator = Paginator(all_records, limit)   # 开始做分页
            except Exception as e:
                print("开始做分页出错了")

            page = int(int(offset) / int(limit) + 1)
            response_data = {'total': all_records_count, 'rows': []}   # 必须带有rows和total这2个key，total表示总页数，rows表示每行的内容


            for asset in pageinator.page(page):
                response_data['rows'].append({
                    "id": asset.id if asset.id else "",
                    "speechTitle": asset.speechTitle if asset.speechTitle else "",
                    "speechKeyword": asset.speechKeyword.replace("\n", "<br/>") if asset.speechKeyword else "",
                    "speechQuestion": asset.speechQuestion if asset.speechQuestion else "",
                    "speechFlow": asset.speechFlow.replace("\n", "<br/>") if asset.speechFlow else "",
                    "speechAnswer": asset.speechAnswer.replace("\n", "<br/>") if asset.speechAnswer else "",
                    "speechGoal": asset.speechGoal.replace("\n", "<br/>") if asset.speechGoal else "",
                    "speechLabel": asset.speechLabel if asset.speechLabel else "",
                    "speechRemark": asset.speechRemark.replace("\n", "<br/>") if asset.speechRemark else "",
                    "speechCount": asset.speechCount if asset.speechCount else "",
                    "speechTarget": asset.speechTarget if asset.speechTarget else "",
                    # "speechCreateTime": asset.speechCreateTime if asset.speechCreateTime else "",
                })

            return HttpResponse(json.dumps(response_data))    # 需要json处理下数据格式
