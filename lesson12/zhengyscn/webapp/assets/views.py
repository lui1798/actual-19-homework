from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, QueryDict
from django.views.decorators.http import require_http_methods

from .models import Assets

import csv

# Create your views here.


'''
def AssetsListView(request):
    if request.user.is_authenticated():
        objs = Assets.objects.all()
        return render(request, "assets.html", context={"context": objs})
    else:
        return HttpResponseRedirect("/account/login/")
'''

@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsListView(request):
    search_value = request.GET.get('search_value')
    if search_value:
        objs = Assets.objects.filter(hostname=search_value)
    else:
        objs = Assets.objects.all()
    return render(request, "assets.html", context={"content": objs})


@require_http_methods(["POST",])
def AssetsAddView(request):
    data = request.POST.dict()
    Assets.objects.create(**data)
    return HttpResponse("Create ok")


@require_http_methods(["DELETE",])
@login_required(login_url="/account/login/")
def AssetsDeleteView(request, pk):
    Assets.objects.get(pk=pk).delete()
    return HttpResponse("Delete ok.")


@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsExportView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)

    objs = Assets.objects.all()
    writer.writerow(['id', '主机名', '外网ip', '内网ip'])
    for obj in objs:
        writer.writerow([obj.pk, obj.hostname, obj.public_ip, obj.private_ip])

    return response

@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsDetailView(request):
    pk = request.GET.get("pk")
    obj = Assets.objects.get(pk=pk)
    data = {
        'hostname' : obj.hostname,
        'public_ip' : obj.public_ip,
        'remark' : obj.remark,
        'private_ip': obj.private_ip,
        'status': obj.status,
    }
    return JsonResponse(data)


@require_http_methods(["PUT",])
@login_required(login_url="/account/login/")
def AssetsEditView(request, pk):
    # print(request.body)
    data = QueryDict(request.body)
    jsondata = data.dict()
    Assets.objects.filter(pk=pk).update(**jsondata)
    return HttpResponse("Update ok")