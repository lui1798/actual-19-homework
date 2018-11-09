from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Assets
import csv
import unicodecsv

@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsListView(request):
    search_value = request.GET.get('search_value')
    if search_value:
        objs = Assets.objects.filter(hostname=search_value)
    else:
        objs = Assets.objects.all()
    return render(request,"assets.html",context={"content" : objs})

@require_http_methods(["POST",])
def AssetsAddView(request):
    data = request.POST.dict()
    Assets.objects.create(**data)
    return HttpResponse("Create ok")

@require_http_methods(["DELETE",])
@login_required(login_url="/account/login/")
def AssetsDeleteView(request,pk):
    Assets.objects.get(pk=pk).delete()
    return HttpResponse("Delete ok.")


@require_http_methods(["GET",])
@login_required
def AssetsDetailView(request, pk):
    obj = Assets.objects.get(pk=pk)
    data = {
        'hostname': obj.hostname,
        'cpu_model': obj.cpu_model,
        'cpu_num': obj.cpu_num,
        'mem': obj.mem,
        'disk': obj.disk,
        'ip': obj.ip,
        'op': obj.op,
        'system': obj.system,
        'line': obj.line,
        'status': obj.host_status,
        'remark': obj.remark,
    }
    return JsonResponse({"code": 0, "data": data}, safe=True)


@require_http_methods(["POST",])
@login_required
def AssetsEditView(request):
    data = request.POST.dict()
    print(data)
    pk = data.pop("pk", None)
    retdata = {}
    if not pk:
        retdata['code'] = -1
        retdata['msg'] = "pk not found"
    else:

        Assets.objects.filter(pk=pk).update(**data)

        retdata['code'] = 0
        retdata['msg'] = "Edit ok."

    return JsonResponse(retdata)


@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsExportView(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    # writer = csv.writer(response)
    writer = unicodecsv.writer(response,encoding='utf-8-sig')
    objs = Assets.objects.all()
    writer.writerow(['ID', '主机名', 'CPU核数', 'CPU型号','内存','硬盘',	'IP地址','负责人','操作系统','业务线','备注','运行状态','创建时间','更新时间',])
    for obj in objs:
        writer.writerow([obj.pk, obj.hostname, obj.cpu_num, obj.cpu_model, obj.mem, obj.disk, obj.ip,
                        obj.op,	obj.system, obj.line, obj.remark, obj.host_status, obj.create_time, obj.update_time])

    return response