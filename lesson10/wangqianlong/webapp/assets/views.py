from django.shortcuts import render,HttpResponse

from .models import Assets

# Create your views here.
def assertView(request):
    objs = Assets.objects.all()
    return render(request, 'form_assert.html',context={'objs':objs})

def deleteAssetView(request):

    pk1 = request.GET.get('pk')
    obj = Assets.objects.get(pk=pk1)
    # print(obj)
    obj.delete()
    return HttpResponse('Delete  {} ok '.format(obj.hostname))

def addAssetpage(request):
    # objs = Assets.objects.all()
    return render(request, 'form_addasset.html')


def addAssetView(request):
    try:
        hostname = request.GET.get('hostname')
        cpu_num = request.GET.get('cpu_num')
        cpu_model = request.GET.get('cpu_model')
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
        remark = request.GET.get('remark')
        if hostname and cpu_num and cpu_model and mem_total\
            and disk and public_ip and private_ip and remote_ip\
                and op and status and  os_system and service_line and frame and remark:

            Asset_data = {
                'hostname':hostname,
                'cpu_num': cpu_num,
                'cpu_model':cpu_model ,
                'mem_total':mem_total,
                'disk':disk,
                'public_ip':public_ip,
                'private_ip':private_ip,
                'remote_ip':remote_ip,
                'op':op,
                'status':status,
                'os_system':os_system,
                'service_line':service_line,
                'frame':frame,
                'remark':remark

            }
            Assets.objects.create(**Asset_data)
            return HttpResponse('Add ok ')
            # return render(request, 'form_asset.html')
        else:

            return HttpResponse('someone is null ')

    except Exception as e:
        return HttpResponse(e.args)




