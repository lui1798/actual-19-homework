from django.shortcuts import render, redirect, HttpResponse
from assets import models


# Create your views here.
def login(request):
    if request.method == "POST":
        u = request.POST.get('email')
        p = request.POST.get('password')
        obj = models.userInfo.objects.filter(username=u, password=p)
        if obj:
            return redirect('/assets/')
        else:
            return HttpResponse('邮箱或密码错误')


def assetsAdd(request):
    if request.method == "GET":
        hostname = request.GET.get('hostname')
        cpu_num = request.GET.get('cpu_num')
        cpu_model = request.GET.get('cpu_model')
        mem_total = request.GET.get('mem_total')
        disk = request.GET.get('disk')
        public_ip = request.GET.get('public_ip')
        private_ip = request.GET.get('private_ip')
        status = request.GET.get('status')
        os_system = request.GET.get('os_system')
        service_line = request.GET.get('service_line')
        op = request.GET.get('op')
        remark = request.GET.get('remark')
        dic = {'hostname': hostname, 'cpu_num': cpu_num, 'cpu_model': cpu_model, 'mem_total': mem_total, 'disk': disk,
               'public_ip': public_ip, 'private_ip': private_ip, 'status': status, 'os_system': os_system,
               'service_line': service_line, 'op': op, 'remark': remark}
        models.assetsInfo.objects.create(**dic)
        return redirect('/assets/')


def assetsUpdate(request, nid):
    if request.method == "GET":
        hostname = request.GET.get('hostname')
        cpu_num = request.GET.get('cpu_num')
        cpu_model = request.GET.get('cpu_model')
        mem_total = request.GET.get('mem_total')
        disk = request.GET.get('disk')
        public_ip = request.GET.get('public_ip')
        private_ip = request.GET.get('private_ip')
        status = request.GET.get('status')
        os_system = request.GET.get('os_system')
        service_line = request.GET.get('service_line')
        op = request.GET.get('op')
        remark = request.GET.get('remark')
        dic = {'hostname': hostname, 'cpu_num': cpu_num, 'cpu_model': cpu_model, 'mem_total': mem_total, 'disk': disk,
               'public_ip': public_ip, 'private_ip': private_ip, 'status': status, 'os_system': os_system,
               'service_line': service_line, 'op': op, 'remark': remark}
        models.assetsInfo.objects.filter(id=nid).update(**dic)
        return redirect('/assets/')
