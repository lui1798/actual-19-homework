#coding:utf-8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from user.models import Users
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, QueryDict
import csv
import codecs
import logging


logger = logging.getLogger(__file__)


# Create your views here.
@require_http_methods(["GET"])
@login_required
def user_home(request):
    return render(request,"users.html")

@require_http_methods(["GET"])
@login_required
def user_list(request):
    all_users = Users.objects.all()
    return render(request,'userlist.html',context={'users':all_users})

@require_http_methods(["GET"])
@login_required
def user_detail(request):
    user_id = request.GET.get("id")
    user = Users.objects.get(id=user_id)
    return render(request,"userdetail.html",context={"user":user})

@require_http_methods(["DELETE"])
@login_required
def user_delete(request,id):
    user = Users.objects.get(id=id)
    user.delete()
    return HttpResponse('delete success')

@require_http_methods(["PUT"])
@login_required
def user_update(request,id):
    jsondata = QueryDict(request.body).dict()
    logger.debug(jsondata)
    try:
        Users.objects.filter(id=id).update(**jsondata)
    except Exception as e:
        return JsonResponse({"code": -1, "msg": "pk {} not found, errmsg {}".format(id, e.args)})
    else:
        return JsonResponse({"code": 0, "msg": "Update ok."})


@require_http_methods(["POST"])
@login_required
def user_add(request):
    user_info = request.POST.dict()
    if user_info['username'] and user_info['address'] and user_info['id_card']:
        Users.objects.create(**user_info)
    else:
        raise Exception("界面字段不能为空")
    return HttpResponseRedirect('/user/list')

@login_required
def user_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="allusers.csv"'
    writer = csv.writer(response)
    response.write(codecs.BOM_UTF8) #避免中文乱码
    objs = Users.objects.all()
    writer.writerow(['id', '姓名', '性别', '地址', '备注', '身份证号', '年龄', '创建日期', '修改日期'])
    for obj in objs:
        writer.writerow([obj.id, obj.username, obj.gender, obj.address,obj.remark,obj.id_card,obj.create_time,obj.update_time])
    return response