from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Assets

import csv


# Create your views here.


########################## v1 #################################

@require_http_methods(["GET",])
@login_required
def AssetsListView(request):
    search_value = request.GET.get('search_value')
    print(search_value)
    if search_value:
        objs = Assets.objects.filter(hostname__contains=search_value)
    else:
        objs = Assets.objects.all()
    return render(request, "assets.html", context={'objs': objs})


@require_http_methods(["GET",])
@login_required
def AssetsDetailView(request, pk):
    obj = Assets.objects.get(pk=pk)
    data = {
        "hostname" : obj.hostname,
        'private_ip' : obj.private_ip,
        'public_ip': obj.public_ip,
        'mem_total': obj.mem_total,
        'status' : obj.status,
        'op': obj.op,
        'remark': obj.remark,
    }
    return JsonResponse({"code" : 0, "data" : data}, safe=True)


def AssetsAddView(request):
    '''
        GET
        /assets/add/?hostname=xxx1&public_ip=xx1&private_ip=xxx3&
    '''

    hostname = request.POST.get('hostname')
    data = {
        "hostname" : hostname,
        "public_ip" : request.POST.get('public_ip'),
        "private_ip": request.POST.get('private_ip'),
        "cpu_num": request.POST.get('cpu_num'),
        "cpu_model": request.POST.get('cpu_model'),
        "remote_ip": request.POST.get('remote_ip'),
        "disk": request.POST.get('disk'),
        "mem_total": request.POST.get('mem_total'),
        "os_system": request.POST.get('os_system'),
        "op": request.POST.get('op'),
        "status": request.POST.get('status'),
        "service_line": request.POST.get('service_line'),
        "frame": request.POST.get('frame'),
        "remark": request.POST.get('remark'),
    }
    retdata = {}
    if hostname:
        try:
            Assets.objects.get(hostname=hostname)
        except Exception as e:
            try:
                Assets.objects.create(**data)
            except Exception as e:
                retdata['code'] = -1
                retdata['msg'] = "Create failed, err {}".format(e.args)
            else:
                retdata['code'] = 0
                retdata['msg'] = "Create ok"
        else:
            retdata['code'] = -1
            retdata['msg'] = "hostname {} is exists.".format(hostname)
    else:
        retdata['code'] = -1
        retdata['msg'] = "hostname {} is required.".format(hostname)
    return JsonResponse(retdata)

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


def AssetsDeleteView(request):
    '''
       GET
       /assets/delete/?pk=3
   '''
    pk = request.GET.get("pk")
    obj = Assets.objects.get(pk=pk)
    obj.delete()
    return HttpResponse("Delete {} ok".format(obj.hostname))


def AssetsExportCsvView(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response