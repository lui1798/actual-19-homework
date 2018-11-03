from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import Assets
# Create your views here.
def assetsview(request):
    objs = Assets.objects.all()
    return render(request, 'form_assets.html', context={'objs': objs})

def deleteasset(request):
    data_id = request.GET.get('id')
    obj = Assets.objects.get(pk=data_id)
    obj.delete()
    return HttpResponse("Delete {} complete！".format(obj.hostname))

def add_assetsview(request):
    return render(request, 'form_assets_add.html')

def add_host(request):
    hostdata = request.GET
    hostdata = hostdata.dict()
    hostdata['cpu_num'] = int(hostdata['cpu_num'])
    hostdata['status'] = int(hostdata['status'])
    hostdata['create_time'] = datetime.now()
    hostdata['update_time'] = datetime.now()
    Assets.objects.create(**hostdata)
    return HttpResponse("Add complete！")

def edit_assetsview(request):
    return render(request, 'form_assets_edit.html')

def edit_host(request):
    data_id = request.GET.get('id')
    obj = Assets.objects.get(pk=5)
    print('request:{0}, data_id:{1}, obj:{2}'.format(request, data_id, obj))
    return render(request, 'form_assets_edit.html',obj=obj)
