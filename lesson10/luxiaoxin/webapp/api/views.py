from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
import os
import subprocess

USENAME = 'admin'
PASSWORD = '51@reboot'
# Create your views here.

def login(request):
    return render(request, 'login.html')


def login_ok(request):
    username =  request.GET.get('username')
    passwd = request.GET.get('passwd')
    status = ''
    print(username,passwd)
    if username == USENAME and passwd == PASSWORD:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


def page_command(request):
    return render(request, 'form_cmd.html')


def command_V3(request):
    cmd = request.GET.get('cmd')
    if cmd:
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        pipe.wait()
        stdout = pipe.stdout.read().decode('utf-8')
        stderr = pipe.stderr.read().decode('utf-8')
        if stdout:
            s = ''' <h5>{0}</h5>'''.format(stdout)
            pageHtml = mark_safe(s)
            return render(request, 'form_cmd.html', {'pageHtml':pageHtml})

        if stderr:
            s = ''' <h4 style="background-color:red">{0}</h4>'''.format(stderr)
            pageHtml = mark_safe(s)
            return render(request, 'form_cmd.html', {'pageHtml':pageHtml})

        s = ''' <h4 style="background-color:red">{0}</h4>'''.format("ERROR:Unknow Except!")
        pageHtml = mark_safe(s)
        return render(request, 'form_cmd.html', {'pageHtml':pageHtml})
    else:
        s = ''' <h4 style="background-color:red">{0}</h4>'''.format("ERROR:Cmd Params Is Required!")
        pageHtml = mark_safe(s)
        return render(request, 'form_cmd.html', {'pageHtml':pageHtml})


def pageSum(request):
    return render(request, 'form_sum_new.html')


def ssum(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 and num2:
        ssum = int(num1) + int(num2)
        s = ''' <h4>{0}</h4>'''.format(ssum)
        pageHtml = mark_safe(s)
        return render(request, 'form_sum_new.html', {'pageHtml':pageHtml})

    else:
        s = ''' <h4 style="background-color:red">{0}</h4>'''.format("ERROR:num1 or num2 params is required!")
        pageHtml = mark_safe(s)
        return render(request, 'form_sum_new.html', {'pageHtml':pageHtml})







def hello(request):
    return HttpResponse('hello world')


def command_V1(request):
    exec_cmd = '''
    Filesystem     1K-blocks    Used Available Use% Mounted on
    /dev/sda2       83845120 9905956  73939164  12% /
    devtmpfs         3987196       0   3987196   0% /dev
    tmpfs            3997036       0   3997036   0% /dev/shm
    tmpfs            3997036    8844   3988192   1% /run
    tmpfs            3997036       0   3997036   0% /sys/fs/cgroup
    /dev/sda1         201380  115264     86116  58% /boot
    tmpfs             799408       0    799408   0% /run/user/0
    '''
    return HttpResponse(exec_cmd)


def command_V2(request):
    cmd = request.GET.get('cmd')
    exec_cmd = os.popen(cmd)
    return HttpResponse(exec_cmd)


def pageSum_V1(request):
    htmlStr = '''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title></title>
            <link href="css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container">
                <br>
                <br>
                <form method="get" action="/ssum">
                    num1:<input type="text" name="num1"/>
                    num2:<input type="text" name="num2"/>
                    <input type="submit" value="求和"/>
                </form>
            </div>
        </body>
    </html>
    '''
    return HttpResponse(htmlStr)


def pageSum_V2(request):
    cmd = 'cat {}'.format('templates/page.html')
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    stdout = pipe.stdout.read().decode('utf-8')
    return HttpResponse(stdout)


def readfile(request):
    filename = request.GET.get('filename')
    if filename:
        cmd = 'cat {}'.format(filename)
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        pipe.wait()
        stdout = pipe.stdout.read().decode('utf-8')
        stderr = pipe.stderr.read().decode('utf-8')
        if stdout:
            s = ''' <pre><h3 style="background-color:green">{0}</h3></pre>'''.format(stdout)
            return HttpResponse(s)

        if stderr:
            s = ''' <pre><h3 style="background-color:red">{0}</h3></pre>'''.format(stderr)
            return HttpResponse(s)

        return HttpResponse("unknow except!")
    else:
        return HttpResponse("filename params is required!")
