from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, QueryDict
from utils.user_valid import valid_userinfo
from django.forms.models import model_to_dict
from django.views.decorators.http import require_http_methods
from users import models
import time
import csv
import codecs
import logging
logger = logging.getLogger(__file__)


# Create your views here.
@require_http_methods(['GET', ])
def UserListView(request):
    search_value = request.GET.get('search_value')
    if search_value:
        objs = models.Users.objects.filter(username=search_value)
    else:
        objs = models.Users.objects.all()
    return render(request, 'user.html', context={'content': objs})


@require_http_methods(['POST', ])
def UserAddView(request):
    jsondata = request.POST.dict()
    result, ok = valid_userinfo(jsondata)
    if not ok:
        return HttpResponse(result)
    else:
        models.Users.objects.create(**jsondata)
        return HttpResponse('success')


@require_http_methods(['GET', ])
def UserDeleteView(request, pk):
    try:
        models.Users.objects.get(pk=pk).delete()
    except Exception as e:
        return JsonResponse({'code': -1, 'msg': 'pk {} not found,errormsg'.format(pk, e.args)})
    else:
        return JsonResponse({'code': 0, 'msg': 'Delete pk {} ok'.format(pk)})


@require_http_methods(['PUT', ])
def UserEditView(request, pk):
    # print(request.body)
    # print(QueryDict(request.body))
    # print(QueryDict(request.body).dict())
    if request.method == 'PUT':
        jsondata = QueryDict(request.body).dict()
        try:
            models.Users.objects.filter(pk=pk).update(**jsondata)
        except Exception as e:
            return JsonResponse({"code": -1, "msg": "pk {} not found, errmsg {}".format(pk, e.args)})
        else:
            return JsonResponse({"code": 0, "msg": "Update ok."})


@require_http_methods(['GET', ])
def UserDetailView(request):
    pk = request.GET.get('pk')
    try:
        obj = models.Users.objects.get(pk=pk)
    except Exception as e:
        return JsonResponse({'code': -1, 'msg': 'pk {} not found,errormsg'.format(pk, e.args)})
    else:
        data = model_to_dict(obj)
        return JsonResponse(data)


@require_http_methods(['GET', ])
def UserExportView(request):
    FILENAME = time.strftime("%Y%m%d", time.localtime())
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)  # 解决中文乱码
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(FILENAME)
    writer = csv.writer(response)
    objs = models.Users.objects.all()
    writer.writerow(['用户名', '性别', '年龄', '城市'])
    for obj in objs:
        writer.writerow(
            [obj.username, obj.sex, obj.age, obj.city])
    return response
