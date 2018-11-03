from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Assets

# Create your views here.

def assetsView(request):
    objs = Assets.objects.all()
    '''
        context 必须是字典类型
    '''
    return render(request, "assets.html", context={'objs' : objs})


def deleteAssetsView(request):
    '''
        GET
        /assets/delete/?pk=3
    '''
    pk = request.GET.get("pk")

    obj = Assets.objects.get(pk=pk)
    obj.delete()
    return HttpResponse("Delete {} ok".format(obj.hostname))


'''
    显示添加的html页面
'''
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
    hostname = request.GET.get('hostname')
    public_ip = request.GET.get('public_ip')
    private_ip = request.GET.get('private_ip')
    cpu_num = request.GET.get('cpu_num')
    cpu_model = request.GET.get('cpu_model')
    remark = request.GET.get('remark')
    mem_total = request.GET.get('mem_total')
    disk = request.GET.get('disk')
    remote_ip = request.GET.get('remote_ip')
    op = request.GET.get('op')
    status = request.GET.get('status')
    os_system = request.GET.get('os_system')
    service_line = request.GET.get('service_line')
    frame = request.GET.get('frame')


    data = {  
      "hostname":host_name,
      "public_ip":public_ip,
      "private_ip":priviate_ip,
      "cpu_num": cpu_num,
      "cpu_model": cpu_model,
      "remark": remark,
      "mem_total": mem_total,
      "disk": disk,
      "remote_ip":remote_ip,
      "op": op,
      "status": status,
      "os_system": os_system,
      "service_line": service_line,
      "frame": frame

      
}
    Assets.objects.create(**data)
    return HttpResponse("Create {} ok.".format(data['hostname']))
