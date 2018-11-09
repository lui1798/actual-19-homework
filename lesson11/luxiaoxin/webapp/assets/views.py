import csv
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, QueryDict
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from datetime import datetime
from .models import Assets
from .validators import AssetsValidator
# Create your views here.

@require_http_methods(['GET',])
@login_required(login_url='/account/login')
def AssetsListView(request):
    search_value = request.GET.get('search_value')
    if search_value:
        objs = Assets.objects.filter(hostname=search_value)
    else:
        objs = Assets.objects.all()
    return render(request, 'assets.html', context={'objs': objs})


@require_http_methods(['POST',])
@login_required(login_url='/account/login')
def AssetsAddView(request):
    data = request.POST.dict()
    is_valid, asset, errors = AssetsValidator.valid_create(data)
    if is_valid:
        Assets.objects.create(**data)
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({ 'code' : 400 ,'errors' : errors })

@require_http_methods(['PUT',])
@login_required(login_url='/account/login')
def  AssetsEditView(request, pk):
    data = QueryDict(request.body).dict()
    data['id'] = pk
    is_valid, asset, errors = AssetsValidator.valid_edit(data)
    print(is_valid, asset, errors)
    if is_valid:
        Assets.objects.filter(pk=pk).update(**data)
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({ 'code' : 400 ,'errors' : errors })


@require_http_methods(['GET',])
@login_required(login_url='/account/login')
def  AssetsDetailView(request):
    pk = request.GET.get('pk')
    try:
        obj = Assets.objects.get(pk=pk)
    except Exception as e:
        raise e
    data = model_to_dict(obj)
    return JsonResponse(data)


@require_http_methods(['DELETE',])
@login_required(login_url='/account/login')
def  AssetsDeleteView(request, pk):
    obj = Assets.objects.get(pk=pk)
    obj.delete()
    return JsonResponse({'code' : 200 })


@require_http_methods(['GET',])
@login_required(login_url='/account/login')
def  AssetsExportView(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="aseetslist.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'hostname', 'cpu_num', 'cpu_model', 'mem_total', 'disk', 'public_ip', 'private_ip', 'remote_ip', 'status', 'os_system', 'service_line', 'frame', 'op', 'remark', 'create_time', 'update_time'])

    search_value = request.GET.get('search_value')
    if search_value:
        objs = Assets.objects.filter(hostname=search_value)
    else:
        objs = Assets.objects.all()

    for obj in objs.values_list():
        writer.writerow(list(obj))

    return response
