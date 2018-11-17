from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import JsonResponse, QueryDict
from assets import models
import csv
import codecs
import time


# Create your views here.
def AssetsListView(request):
    search_value = request.GET.get('search_value')
    if search_value:
        objs = models.assetsInfo.objects.filter(hostname=search_value)
    else:
        objs = models.assetsInfo.objects.all()
    return render(request, 'assets.html', context={'objs': objs})


def AssetsAddView(request):
    if request.method == "POST":
        data = request.POST.dict()
        models.assetsInfo.objects.create(**data)
        return HttpResponse('success')
    else:
        return HttpResponse('请正确填写信息')


def AssetsDeleteView(request, pk):
    models.assetsInfo.objects.get(pk=pk).delete()
    return HttpResponse('Delete ok')


def AssetsExportView(request):
    FILENAME = time.strftime("%Y%m%d", time.localtime())
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)  # 解决中文乱码
    response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(FILENAME)
    writer = csv.writer(response)
    objs = models.assetsInfo.objects.all()
    writer.writerow(['主机名', 'CPU核数', 'CPU型号', '内存', '磁盘', '内网IP', '公网IP', '操作系统', '状态', '业务线', '运维负责人', '备注'])
    for obj in objs:
        writer.writerow(
            [obj.hostname, obj.cpu_num, obj.cpu_model, obj.mem_total, obj.disk, obj.private_ip, obj.public_ip,
             obj.os_system, obj.status, obj.service_line, obj.op, obj.remark])
    return response


def DetailAssetView(request):
    if request.method == "GET":
        pk = request.GET.get('pk')
        objs = models.assetsInfo.objects.get(pk=pk)
        data = {
            'hostname': objs.hostname,
            'cpu_num': objs.cpu_num,
            'cpu_model': objs.cpu_model,
            'mem_total': objs.mem_total,
            'disk': objs.disk,
            'private_ip': objs.private_ip,
            'public_ip': objs.public_ip,
            'os_system': objs.os_system,
            'status': objs.status,
            'service_line': objs.service_line,
            'op': objs.op,
            'remark': objs.remark,
        }
        return JsonResponse(data)


def AssetsEditView(request, pk):
    if request.method == 'PUT':
        data = QueryDict(request.body)
        jsondata = data.dict()
        models.assetsInfo.objects.filter(pk=pk).update(**jsondata)
        return HttpResponse('success')
