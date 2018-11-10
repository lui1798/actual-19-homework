# -*- encoding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, QueryDict
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
import csv, codecs

from .models import Assets

# Create your views here.

@require_http_methods(["GET",])
@login_required(login_url="/account/login")
def AssetsListView(request):
    search_value = request.GET.get('search_value')
    if search_value:
        objs = Assets.objects.filter(hostname=search_value)
    else:
        objs = Assets.objects.all()

    return render(request, "assets.html", context={"content": objs})


@require_http_methods(["DELETE",])
@login_required(login_url="/account/login")
def AssetsDeleteView(request, pk):
    Assets.objects.get(pk=pk).delete()

    return HttpResponse("删除成功！")


@require_http_methods(["POST",])
@login_required(login_url="/account/login")
def AssetsAddView(request):
    data = request.POST.dict()
    Assets.objects.create(**data)

    return HttpResponse("添加主机：{} 成功！".format(data['hostname']))

@require_http_methods(["PUT",])
@login_required(login_url="/account/login/")
def AssetsEditView(request, pk):
    data = QueryDict(request.body)
    jsondata = data.dict()
    Assets.objects.filter(pk=pk).update(**jsondata)

    return HttpResponse("编辑成功!")


@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsGetView(request):
    pk = request.GET.get("pk")
    obj = Assets.objects.get(pk=pk)
    data = {}
    data['id'] = obj.id
    data['hostname'] = obj.hostname
    data['cpu_num'] = obj.cpu_num
    data['cpu_model'] = obj.cpu_model
    data['mem_total'] = obj.mem_total
    data['disk'] = obj.disk
    data['public_ip'] = obj.public_ip
    data['private_ip'] = obj.private_ip
    data['remote_ip'] = obj.remote_ip
    data['op'] = obj.op
    data['status'] = obj.status
    data['os_system'] = obj.os_system
    data['service_line'] = obj.service_line
    data['frame'] = obj.frame
    data['remark'] = obj.remark

    # return HttpResponse(json.dumps(data), content_type="application/json")
    return JsonResponse(data)


@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsExportView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)

    objs = Assets.objects.all()
    writer.writerow(['id', '主机名', 'CPU核数', 'CPU型号', '内存', '硬盘', '公网IP', '内网IP', '远程IP', '负责人', '上下线', '操作系统', '所属业务', '机柜位置', '备注'])
    for obj in objs:
        writer.writerow([obj.pk, obj.hostname, obj.cpu_num, obj.cpu_model, obj.mem_total, obj.disk, obj.public_ip, obj.private_ip, obj.remote_ip, obj.op, obj.status, obj.os_system, obj.service_line, obj.frame, obj.remark])

    return response