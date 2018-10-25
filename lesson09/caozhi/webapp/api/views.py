from django.shortcuts import render, HttpResponse
import os
import subprocess

# Create your views here.

def hello(request):
    print(request)
    return HttpResponse('hello world')

def commond(request):
    cmd = request.GET.get('cmd')
    cmd_result = os.popen(cmd).read()
    return HttpResponse(cmd_result)

def ccommond_v1(request):
    cmd = request.GET.get('cmd')
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    pipe.wait()
    stdout = pipe.stdout.read()
    stderr = pipe.stderr.read()
    print(stdout,stderr)
    if stdout:
        so = '''<h2 style="background-color: green;">{}</h2>'''.format(stdout)
        print('1')
        return HttpResponse(so)
    if stderr:
        se = '''<h2 style="background-color: red;">{}</h2>'''.format(stderr)
        print('0')
        return HttpResponse(se)
    return HttpResponse('unknow error')

def cssum(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    cssum = int(num1) + int(num2)
    return HttpResponse(cssum)

def page(request):
    htmlstr = '''
<!doctype html>
<html>

	<head>
		<meta charset="utf-8">
		<title></title>
		<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no" />
		<link href="css/mui.css" rel="stylesheet" />
	</head>

	<body>
		<form method="get" action="http://127.0.0.1/cssum">
			<input type="text" name="num1" />
			<input type="text" name="num2" />
			<input type="submit"  value="sum"/>
		</form>
	</body>

</html>
'''

def cat_cat(request):
    wenjian = request.GET.get('file')
    #cmd = 'cat' + ' ' + wenjian
    cmd_result = os.popen('cat' + ' ' + wenjian).read()
    return HttpResponse(cmd_result)

def pagesum(request):
    return render(request, "form_sum.html")

def pagesum_v2(request):
    cmd = "cat templates/form_sum.html"
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    htmlstr = pipe.stdout.read().decode("utf-8")
    return HttpResponse(htmlstr)


