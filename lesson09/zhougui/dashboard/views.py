from django.shortcuts import render, HttpResponse
import subprocess


# Create your views here.
def index(request):
    return render(request, 'index.html')


def utils(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 is None and num2 is None:
        return render(request, 'utils.html')
    if num1 and num2:
        ssum = int(num1) + int(num2)
        return HttpResponse(ssum)
    else:
        return HttpResponse('Valid failed.')


def command(request):
    cmd = request.GET.get('cmd')
    if cmd:
        pip = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        stdout = pip.stdout.read().decode('utf-8')
        stderr = pip.stderr.read().decode('utf-8')
        if stdout:
            return HttpResponse(stdout)
        if stderr:
            return HttpResponse(stderr)
    else:
        return render(request, 'command.html')
