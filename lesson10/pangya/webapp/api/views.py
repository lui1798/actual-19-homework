from django.shortcuts import render, HttpResponse
import os
import subprocess


# Create your views here.


def hello(request):
    print(request)
    print(dir(request))
    # print(dir("\n\n\n")
    print("get_full_path: ", request.get_full_path())
    print("method: ", request.method)
    print("environ: ", request.environ)
    return HttpResponse("hello world")


def command_v1(request):
    cmd_execute_reponse = '''
    Filesystem     1K-blocks    Used Available Use% Mounted on
    /dev/sda2       20282236 4648464  14603476  25% /
    tmpfs             514352     224    514128   1% /dev/shm
    /dev/sda1          99150   28268     65762  31% /boot
    /dev/sr0         3757116 3757116         0 100% /media/CentOS_6.5_Fina'''
    return HttpResponse(cmd_execute_reponse)


def command_v3(request):  # 也可以写成command_v3(a):cmd=a.GET.get('cmd')
    cmd = request.GET.get('cmd')
    if cmd:
        cmd_execute_reponse = os.popen(cmd).read()  # os.popen()会把执行命令的输出作为值返回，可实现一个“管道”，从这个命令获取的值可以继续被调用。
        return HttpResponse(cmd_execute_reponse)
    else:
        return HttpResponse("cmd is required")


# 网址为192.168.1.2:8000/command_v2/?cmd=df或192.168.1.2:8000/command_v2/?cmd=date

def command_v4(request):  # 也可以写成command_v3(a):cmd=a.GET.get('cmd')
    cmd = request.GET.get('cmd')
    if cmd:
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pipe.wait()
        stdout = pipe.stdout.read().decode("utf-8")
        stderr = pipe.stderr.read().decode("utf-8")
        if stdout:
            s = '''<h1 style="background-color:green:">{}</h1>'''.format(stdout)
            return HttpResponse(s)
        if stderr:
            s = '''<h1 style="background-color:red:">{}</h1>'''.format(stderr)
            return HttpResponse(s)
    else:
        return HttpResponse("Unkown except.")


"""
实现当输入文件名时，页面返回文件内容，如：http:192.168.1.100:8000/file/?file=/etc/passwd
"""
def catFile(request):
    file=request.GET.get('file')  #用request的get请求接收前端的file参数
    cmd = "cat {}".format(file)   #在后端查看文件
    if cmd:
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pipe.wait()
        stdout = pipe.stdout.read().decode("utf-8")
        stderr = pipe.stderr.read().decode("utf-8")
        if stdout:
            s = '''<h1 style="background-color:green:">{}</h1>'''.format(stdout)
            return HttpResponse(s)
        if stderr:
            s = '''<h1 style="background-color:red:">{}</h1>'''.format(stderr)
            return HttpResponse(s)
    else:
        return HttpResponse("Unkown except.")


def ssum_v1(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 and num2:
        # s = int(num1)+int(num2)
        s = sum([int(num1), int(num2)])  # sum中间必须接收列表
        return HttpResponse(s)
    else:
        return HttpResponse("num1 and num2 is required.")
        # 浏览器输入127.0.0.1:8000/ssum/?num1=3&num2=4 就会返回7


"""
ssum的网页部分也可以放到html文件中
"""


"""
def pageSum_v1(request):
    htmlStr = '''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title></title>
        </head>
        <body>
            <form method="get" action="/ssum/">
                num1: <input type="text" name="num1" />
                num2: <input type="text" name="num2"/>
                <input type="submit" value="求和"/>
            </form>
        </body>
    </html>
    '''
    return HttpResponse(htmlStr)


"""
"""
用这个时需要在urls.py中加url(r'^pageSum_v1/', pageSum_v1),from api.views import pageSum_v1
网址可以直接输入：http://192.168.1.100:8000/PageSum/
"""

"""前端与后端分离方法1"""
def pageSum_v1(request):
    cmd="cat templates/form_sum.html"
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    htmlstr=pipe.stdout.read().decode("utf-8")
    return HttpResponse(htmlstr)
"""前端与后端分离方法1"""
def pageSum(request):
    return render(request,"form_sum.html")