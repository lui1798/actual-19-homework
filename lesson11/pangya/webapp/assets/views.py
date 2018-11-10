import csv
from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from .models import Assets
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
# Create your views here.
'''
def AssetsListView(request):
    if request.user.is_authenticated():
        objs = Assets.objects.all()
        return render(request, "assets.html", context={'objs': objs})  # context 必须是字典类型
    else:
        return HttpResponseRedirect("/account/login/")
'''
@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsListView(request):
    search_value=request.GET.get('search_value')
    if search_value:
        objs=Assets.objects.filter(hostname=search_value)
    else:
        objs =Assets.objects.all()
    return render(request, "assets.html", context={'content': objs})

@require_http_methods(["DELETE",])
def AssetsDeleteView(request,pk):
    Assets.objects.get(pk=pk).delete()
    return HttpResponse("Delete ok.")


@require_http_methods(["POST",])
def AssetsAddView(request):
    data=request.POST.dict()
    full_message=True
    if data['status']=='---请选择---':
        full_message = False
    for str in data.values():
        if str == '':
            full_message = False
    if full_message:
        Assets.objects.create(**data)
        return HttpResponse("Create ok")
    else:
        return HttpResponse(" Incomplete information")


@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def  AssetsDetailView(request,pk):
    obj = Assets.objects.get(pk=pk)
    data = model_to_dict(obj)
    return JsonResponse(data)


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


def AssetsExportCsvView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(
        ['ID', 'hostname', 'cpu_num', 'cpu_model', 'mem_total', 'disk', 'public_ip', 'private_ip', 'remote_ip',
         'status', 'os_system', 'service_line', 'frame', 'op', 'remark', 'create_time', 'update_time'])
    objs = Assets.objects.all()
    for obj in objs.values_list():
        writer.writerow(list(obj))
    return response