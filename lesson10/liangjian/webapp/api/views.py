import os
import subprocess

from django.shortcuts import render,HttpResponse


# Create your views here.


def hello(request):
    return HttpResponse('hello world.')



def command_v1(request):
    cmd_exec_response = '''
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda1        50G   13G   34G  28% /
devtmpfs        487M     0  487M   0% /dev
tmpfs           497M   24K  497M   1% /dev/shm
tmpfs           497M  536K  496M   1% /run
tmpfs           497M     0  497M   0% /sys/fs/cgroup
tmpfs           100M     0  100M   0% /run/user/0
'''
    return HttpResponse(cmd_exec_response)


def command_v2(request):
    cmd = request.GET.get('cmd')
    cmd_exec_response = os.popen(cmd).read()
    return HttpResponse(cmd_exec_response)

def command_v3(request):
    cmd = request.GET.get('cmd')
    pipe = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
    pipe.wait()
    stdout = pipe.stdout.read()
    stderr = pipe.stderr.read()
    if stdout:
        s = '''<h1 style="background-color:green;">{}</h1>'''.format(stdout)
        return HttpResponse(s)

    if  stderr:
        s = '''<h1 style="background-color:red;">{}</h1>'''.format(stderr)
        return HttpResponse(s)
    return HttpResponse("unknow except")


def ssum(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    #s = int(num1) + int(num2)
    if num1 and num2:
        s = sum([int(num1),int(num2)])
        return HttpResponse("num1 + num2 = {}".format(s))
    else:
        return HttpResponse("num1 and num2 params is required.")


def pageSum(request):
    htmlStr = '''<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<form method="get" action="http://140.143.227.246:9092/ssum/">
			num1:<input type="text" name="num1" />
			num2:<input type="text" name="num2"/>
			<input type="submit"  value="求和"/>
		</form>
	</body>
</html>

'''
    return HttpResponse(htmlStr)


def catFile(request):
    file = request.GET.get('file')
    if file:
        cmd = "cat {}".format(file)
        pipe = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
        pipe.wait()
        stdout = pipe.stdout.read()
        stderr = pipe.stderr.read()
        return HttpResponse(file)


def pageSum_v2(request):
    cmd = "cat templates/form_sum.html"
    pipe = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
    htmlStr = pipe.stdout.read().decode("utf-8")
    print(pipe.stderr.read().decode("utf-8"))
    return HttpResponse(htmlStr)

def pageSum(request):
    return render(request,"form_sum.html")
