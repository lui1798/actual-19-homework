from django.shortcuts import render,HttpResponse

# Create your views here.
import os
import subprocess

def apicatfile(request):
    cmd = request.GET.get('filename')
    cmd_a = 'cat {}'.format(cmd)
    cmd_result = os.popen(cmd_a).read()
    return HttpResponse(cmd_result)

def apicommand(request):
    cmd = request.GET.get('cmd')
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    pipe.wait()
    stdout = pipe.stdout.read().decode("utf-8")
    stderr = pipe.stderr.read().decode("utf-8")
    if stdout:
        return HttpResponse(stdout)
    if stderr:
        return HttpResponse(stderr)
    return HttpResponse("unexcept")

def apissum(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 and num2:
        s = sum([int(num1), int(num2)])
        return HttpResponse(s)
    else:
        return HttpResponse("num1 and num2 params is required.")

