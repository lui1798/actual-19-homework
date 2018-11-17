from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Users
from utils.user_valid import valid_userinfo
import unicodecsv
import time

import logging

@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def UsersListView(request):
    logging.info("显示用户列表")
    objs = Users.objects.all()
    return render(request, "users.html", context={"content":objs})

@require_http_methods(["DELETE",])
@login_required(login_url="/account/login/")
def UsersDeleteView(request,pk):
    logging.info("删除用户")
    try:
        Users.objects.get(pk=pk).delete()
    except Exception as e:
        return JsonResponse({"code" : -1, "msg" : "pk {} not found,error msg {}".format(pk, e.args)})
    else:
        return JsonResponse({"code" : 0, "msg" : "Delete {} is ok".format(pk)})


@require_http_methods(["POST",])
@login_required(login_url="/account/login/")
def UsersAddView(request):
    logging.info("添加用户")
    jsondata = request.POST.dict()
    result, ok = valid_userinfo(jsondata)
    if not ok:
        return HttpResponse(result)
    else:
        Users.objects.create(**jsondata)
        return HttpResponse("Create ok")


@require_http_methods(["POST",])
@login_required(login_url="/account/login/")
def UsersEditView(request):
    logging.info("编辑用户")
    data = request.POST.dict()
    pk = data.pop("pk", None)
    retdata = {}
    if not pk:
        retdata['code'] = -1
        retdata['msg'] = "pk not found"
    else:

        Users.objects.filter(pk=pk).update(**data)

        retdata['code'] = 0
        retdata['msg'] = "Edit ok."

    return JsonResponse(retdata)


@require_http_methods(["GET", ])
@login_required(login_url="/account/login/")
def UsersDetailView(request,pk):
    logging.info("查看用户详情")
    obj = Users.objects.get(pk=pk)
    data = {
        'username': obj.username,
        'sex': obj.sex,
        'age': obj.age,
        'city': obj.city,
    }
    return JsonResponse({"code": 0, "data": data}, safe=True)


@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def UsersExportView(request):
    logging.info("导出用户")
    response = HttpResponse(content_type='text/csv')
    tm = time.strftime("%Y%m%d%H%M%S", time.localtime())
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(tm)

    # writer = csv.writer(response)
    writer = unicodecsv.writer(response,encoding='utf-8-sig')
    objs = Users.objects.all()
    writer.writerow(['ID', '姓名', '性别', '年龄','城市',])
    for obj in objs:
        writer.writerow([obj.pk, obj.username, obj.sex, obj.age, obj.city])

    return response