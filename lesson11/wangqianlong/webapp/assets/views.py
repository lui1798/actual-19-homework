
import csv
import time
from django.shortcuts import render,HttpResponse

from .models import Assets
from django.http import JsonResponse, QueryDict
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.

'显示'
@require_http_methods('GET')
@login_required(login_url='/account/login/')
def AssetListView(request):
    search_value = request.GET.get('search_value')
    if search_value:
        objs = Assets.objects.filter(hostname=search_value)
    else:
        objs = Assets.objects.all()
    return render(request,'assets.html',context={'content':objs})


'删除'
@require_http_methods('DELETE')
@login_required(login_url='/account/login/')
def AssetDeleteView(request,pk):
    Assets.objects.get(pk=pk).delete()
    return HttpResponse('Delete ok ')



'添加'
@require_http_methods(['POST',])
def AssertAddView(request):
   # hostname = 2 & private_ip = & public_ip = & cpu_num = & cpu_model = & mem_total =
    Asset_data = request.POST.dict()
    if '' in Asset_data.values():
        return HttpResponse('所有输入不能为空，请检查！ ')
    else:
        Assets.objects.create(**Asset_data)
        return HttpResponse('添加成功！ ')



'导出csv'
@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsExportView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Assertinfo.csv"'

    writer = csv.writer(response)

    objs = Assets.objects.all()

    writer.writerow(['id', '主机名', '外网ip', '内网ip',
                     '远程ip','cpu核','cpu型号','内存','磁盘大小',
                     '运维负责人','状态','操作系统','所属业务线','机架','备注','创建时间','修改时间'])
    for obj in objs:
        obj.create_time = obj.create_time.strftime("%Y-%m-%d %H:%M:%S")
        obj.update_time = obj.update_time.strftime("%Y-%m-%d %H:%M:%S")
        if obj.status==1:
            obj.status = '运行'
        elif obj.status==0:
            obj.status = '关机'
        writer.writerow([obj.pk, obj.hostname, obj.public_ip, obj.private_ip,
                         obj.remote_ip,obj.cpu_num,obj.cpu_model,obj.mem_total,
                         obj.disk,obj.op,obj.status,obj.os_system,obj.service_line,
                         obj.frame,obj.remark,obj.create_time,obj.update_time])

    return response


'详情'
@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetDetailView(request):
    pk = request.GET.get("pk")
    obj = Assets.objects.get(pk=pk)
    data = {
        'hostname': obj.hostname,
        'cpu_num': obj.cpu_num,
        'cpu_model': obj.cpu_model,
        'mem_total': obj.mem_total,
        'disk': obj.disk,
        'public_ip': obj.public_ip,
        'private_ip': obj.private_ip,
        'remote_ip': obj.remote_ip,
        'op': obj.op,
        'status': obj.status,
        'os_system': obj.os_system,
        'service_line': obj.service_line,
        'frame': obj.frame,
        'remark': obj.remark
    }
    # print(data)
    return JsonResponse(data)

'编辑'
@require_http_methods(["PUT",])
@login_required(login_url="/account/login/")
def AssetEditView(request, pk):
    # print(request.body)
    data = QueryDict(request.body)
    jsondata = data.dict()
    Assets.objects.filter(pk=pk).update(**jsondata)
    return HttpResponse("Update ok")





def assertView(request):
    objs = Assets.objects.all()
    return render(request, 'form_assert.html',context={'objs':objs})

# def deleteAssetView(request):
#
#     pk1 = request.GET.get('pk')
#     obj = Assets.objects.get(pk=pk1)
#     # print(obj)
#     obj.delete()
#     return HttpResponse('Delete  {} ok '.format(obj.hostname))
#
# def addAssetpage(request):
#     # objs = Assets.objects.all()
#     return render(request, 'form_addasset.html')






