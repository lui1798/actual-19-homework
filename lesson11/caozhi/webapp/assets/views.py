from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Assets
import csv
import time


def favicon(request):
    return render(request, "favicon.ico")

@login_required(login_url="/account/login")
def assetsView(request):
    objs = Assets.objects.all()
    return render(request,"assets.html", context={'objs': objs})

def deleteAssetsView(request):
    pk = request.GET.get("pk")
    obj = Assets.objects.get(pk=pk)
    obj.delete()
    return HttpResponse("Delete {} ok".format(obj.hostname))
    #return HttpResponse("emmby")

@require_http_methods(["GET",])
@login_required(login_url="/account/login")
def AssetsListView(request):
    search_value = request.GET.get('search_value')
    if search_value:
        objs = Assets.objects.filter(hostname=search_value)
    else:
        objs = Assets.objects.all()
    #return HttpResponseRedirect("/assets/list")
    return render(request, "assets.html", context={"context": objs})

@require_http_methods(["POST",])
def AssetsAddView(request):
    data = request.POST.dict()
    print('*********',data)
    Assets.objects.create(**data)
    return HttpResponse("create ok")

@require_http_methods(["DELETE",])
@login_required(login_url="/account/login")
def AssetsDeleteView(request, pk):
    Assets.objects.get(pk=pk).delete()
    return HttpResponse("Delete ok")

@require_http_methods(["GET",])
@login_required(login_url="/account/login")
def AssetsExportView(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="new.csv"'
    writer = csv.writer(response)
    
    objs = Assets.objects.all()
    writer.writerow(['id', 'hostname', 'cpu核数', 'cpu型号', '内存','磁盘容量', '公网ip', '私有ip', '远程ip', '运维负责人', '机器的状态', '操作系统', '所属业务线', '机架', '备注', '创建时间', '修改时间' ])
    for obj in objs:
        writer.writerow([obj.pk, obj.hostname, obj.cpu_num, obj.cpu_model, obj.mem_total, obj.disk, obj.public_ip, obj.private_ip, obj.remote_ip, obj.op, obj.status, obj.os_system, obj.service_line, obj.frame, obj.remark, obj.create_time, obj.update_time])
    return response
    time.sleep(5)
    return HttpResponseRedirect("/assets/list")
