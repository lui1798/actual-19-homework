
#coding=UTF-8
from django.shortcuts import render ,HttpResponse
from .models import Assets


# Create your views here.
def assetviews(request):
    objs = Assets.objects.all()
    return render(request,"form_asset.html",context={'objs':objs})

def deleteasset(request):
    id = request.GET.get('id')
    obj = Assets.objects.get(id=id)
    obj.delete()
    return HttpResponse("删除 用户：{}成功".format(obj.host_name))

def addPageAssetsView(request):
    '''
        GET
        /assets/delete/?pk=3
    '''
    return render(request, "assets_add_page.html")


def addAssetsView(request):
    '''
        GET
        /assets/add/?hostname=xxx1&public_ip=xx1&private_ip=xxx3&
    '''

    host_name = request.GET.get('host_name')
    cpu_num = request.GET.get('cpu_num')
    cpu_model = request.GET.get('cpu_model')
    remark = request.GET.get('remark')
    mem_total = request.GET.get('mem_total')
    disk = request.GET.get('disk')
    public_ip = request.GET.get('public_ip')
    private_ip = request.GET.get('private_ip')
    remote_ip = request.GET.get('remote_ip')
    op = request.GET.get('op')
    status = request.GET.get('status')
    os_system = request.GET.get('os_system')
    service_line = request.GET.get('service_line')
    frame = request.GET.get('frame')
    data = {
        "host_name": host_name,
        "cpu_num": cpu_num,
        "cpu_model": cpu_model,
        "remark": remark,
        "mem_total": mem_total,
        "disk": disk,
        "public_ip": public_ip,
        "private_ip": private_ip,
        "remote_ip":remote_ip,
        "op": op,
        "status": status,
        "os_system": os_system,
        "service_line": service_line,
        "frame": frame
    }
    context = {
        "host_name":host_name
    }
    Assets.objects.create(**data)
    return render(request,"form_asset_success.html",context=context)





