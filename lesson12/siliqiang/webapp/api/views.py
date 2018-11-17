# coding: utf-8
from django.shortcuts import render,HttpResponse
import os
import subprocess

# Create your views here.

def hello(request):
    return HttpResponse("hello world!")

def command_v1(request):
    cmd_result = """centos"""
    return HttpResponse(cmd_result)

def command_v2(request):
    cmd = request.GET.get('cmd')
    print(cmd)
    cmd_result = os.popen(cmd).read()
    return HttpResponse(cmd_result)

def command_v3(request):
    cmd = request.GET.get('cmd')
    pipe = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
    pipe.wait()
    stdout = pipe.stdout.read().decode("utf-8")
    stderr = pipe.stderr.read().decode("utf-8")
    if stdout:
        s = '''<pre><h1 style="background-color:green;">{}</h1></pre>'''.format(stdout)
        return HttpResponse(s)
    if stderr:
        s = '''<pre><h1 style="background-color:red;">{}</h1></pre>'''.format(stderr)
        return HttpResponse(s)
    return HttpResponse("unexcept")

def command_v4(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    print(num1)
    print(num2)
    if num1 and num2:
        ssum = int(num1) + int(num2)
        return HttpResponse(ssum)
    else:
        return HttpResponse("num1 and num2 params is required.")

def file(request):
    cmd = request.GET.get('file')
    cmd_a = 'cat {}'.format(cmd)
    cmd_result = os.popen(cmd_a).read()

    s = '''<pre><h1 style="background-color:green;">{}</h1></pre>'''.format(cmd_result)
    return HttpResponse(s)

def pageSum_v1(request):
    htmlStr = """
    <!DOCTYPE html>
    <html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<body>
		<form method="get" action="/comma nnd_v4/">
			num1: <input type="text" name="num1" />
			num2: <input type="text" name="num2" />
			<input type="submit" value="求和" />
		</form>
	</body>
    </html>
    """
    return HttpResponse(htmlStr)

def pageSum_v2(request):
    cmd = 'cat templates/form_sum.html'
    pipe = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
    htmlStr = pipe.stdout.read().decode("utf-8")
    return HttpResponse(htmlStr)

def pageSum(request):
    return render(request,"form_sum.html")