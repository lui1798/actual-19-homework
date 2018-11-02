from django.shortcuts import render,HttpResponse
from .models import Assets

# Create your views here.

def assetsView(request):
    objs = Assets.objects.all()
    return render(request, "assets.html", context={ 'objs' : objs })

def assetsDelete(request):
    pk = request.GET.get('pk')
    obj = Assets.objects.get(pk=pk)
    obj.delete()
    return HttpResponse("Delete {} ok".format(obj.hostname))

def assetsAdd(request):
    hostname    =   request.GET.get('hostname')
    cpu_num      =   request.GET.get('cpu_num')
    cpu_model     =   request.GET.get('cpu_model')
    mem_total    =   request.GET.get('mem_total')
    disk         =   request.GET.get('disk')
    public_ip    =   request.GET.get('public_ip')
    private_ip   =   request.GET.get('private_ip')
    remote_ip    =   request.GET.get('remote_ip')
    op           =   request.GET.get('op')
    status       =   request.GET.get('status')
    os_system    =   request.GET.get('os_system')
    service_line =   request.GET.get('service_line')
    frame        =   request.GET.get('frame')
    remark       =   request.GET.get('remark')

    data = {
        'hostname'  :   hostname ,
        'cpu_num'   :   cpu_num,
        'cpu_model'  :   cpu_model,
        'mem_total' :   mem_total,
        'disk'      :   disk,
        'public_ip' :   public_ip,
        'private_ip':   private_ip,
        'remote_ip' :   remote_ip,
        'op'        :   op,
        'status'    :   status,
        'os_system'    :   os_system,
        'service_line' : service_line,
        'frame'     :   frame,
        'remark'    :   remark,

    }
    Assets.objects.create(**data)
    return HttpResponse("Create {} ok.".format(data['hostname']))