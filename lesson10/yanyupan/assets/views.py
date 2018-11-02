from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
#import json

from .models import Assets

# Create your views here.


def assetsView(request):
    objs = Assets.objects.all()

    return render(request, "assets.html", context={'objs': objs})


def deleteAssetsView(request):
    pk = request.GET.get("pk")
    obj = Assets.objects.get(pk=pk)
    obj.delete()

    return HttpResponse("删除成功！")


def addAssetsView(request):
    data = {}
    data['hostname'] = request.POST.get("hostname")
    data['cpu_num'] = request.POST.get("cpu_num")
    data['cpu_model'] = request.POST.get("cpu_model")
    data['mem_total'] = request.POST.get("mem_total")
    data['disk'] = request.POST.get("disk")
    data['public_ip'] = request.POST.get("public_ip")
    data['private_ip'] = request.POST.get("private_ip")
    data['remote_ip'] = request.POST.get("remote_ip")
    data['op'] = request.POST.get("op")
    data['status'] = request.POST.get("status")
    data['os_system'] = request.POST.get("os_system")
    data['service_line'] = request.POST.get("service_line")
    data['frame'] = request.POST.get("frame")
    data['remark'] = request.POST.get("remark")

    obj = Assets.objects
    obj.create(**data)

    return HttpResponse("添加主机：{} 成功！".format(data['hostname']))

def editAssetsView(request):
    data = {}
    data['id'] = request.POST.get("id")
    data['hostname'] = request.POST.get("hostname")
    data['cpu_num'] = request.POST.get("cpu_num")
    data['cpu_model'] = request.POST.get("cpu_model")
    data['mem_total'] = request.POST.get("mem_total")
    data['disk'] = request.POST.get("disk")
    data['public_ip'] = request.POST.get("public_ip")
    data['private_ip'] = request.POST.get("private_ip")
    data['remote_ip'] = request.POST.get("remote_ip")
    data['op'] = request.POST.get("op")
    data['status'] = request.POST.get("status")
    data['os_system'] = request.POST.get("os_system")
    data['service_line'] = request.POST.get("service_line")
    data['frame'] = request.POST.get("frame")
    data['remark'] = request.POST.get("remark")

    pk = data["id"]
    obj = Assets.objects.filter(id=pk)
    obj.update(**data)

    return HttpResponse("编辑成功!")


def getAssetsView(request):
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