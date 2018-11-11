import os
import subprocess

from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request):
    print(dir(request))
    print("\n\n\n")
    print("get_full_path: ", request.get_full_path())
    print("method: ", request.method)
    print("environ: ", request.environ)
    # return "hello world."
    return HttpResponse("hello world.")


def command_v1(request):
    cmd_exec_response = '''
    Filesystem           1K-blocks     Used Available Use% Mounted on
    /dev/mapper/VolGroup-lv_root
                           8561112  3664068   4455496  46% /
    tmpfs                   961132        0    961132   0% /dev/shm
    /dev/sda1               487652    32922    429130   8% /boot
    vagrant              139106468 77364344  61742124  56% /vagrant
    home_vagrant_zhengyscn
                         139106468 77364344  61742124  56% /home/vagrant/zhengyscn

    '''
    return HttpResponse(cmd_exec_response)

def command_v2(request):
    cmd = request.GET.get('cmd')
    cmd_exec_response = os.popen(cmd).read()
    return HttpResponse(cmd_exec_response)


def command_v3(request):
    cmd = request.GET.get('cmd')
    if cmd:
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        pipe.wait()
        stdout = pipe.stdout.read().decode("utf-8")
        stderr = pipe.stderr.read().decode("utf-8")
        if stdout:
            s = '''<pre><h1 style="background-color: green;">{}</h1></pre>'''.format(stdout)
            return HttpResponse(s)

        if stderr:
            s = '''<pre><h1 style="background-color: red;">{}</h1></pre>'''.format(stderr)
            return HttpResponse(s)
        return HttpResponse("unknow except.")
    else:
        return HttpResponse("cmd params is required.")


def ssum(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    print(num1, num2)
    if num1 and num2:
        # s =  int(num1) + int(num2)
        s = sum([int(num1), int(num2)])
        return HttpResponse(s)
    else:
        return HttpResponse("num1 and num2 params is required.")

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

def pageSum_v2(request):
    cmd = "cat templates/form_sum.html"
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    htmlStr = pipe.stdout.read().decode("utf-8")
    print(pipe.stderr.read().decode("utf-8"))
    return HttpResponse(htmlStr)

def pageSum(request):
    return render(request, "form_sum.html")


def catFile(request):
    file = request.GET.get('file')
    if file:
        cmd = "cat {}".format(file)
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        pipe.wait()
        stdout = pipe.stdout.read().decode("utf-8")
        stderr = pipe.stderr.read().decode("utf-8")
        if stdout:
            s = '''<pre><h1 style="background-color: green;">{}</h1></pre>'''.format(stdout)
            return HttpResponse(s)

        if stderr:
            s = '''<pre><h1 style="background-color: red;">{}</h1></pre>'''.format(stderr)
            return HttpResponse(s)
        return HttpResponse("unknow except.")
    else:
        return HttpResponse("cmd params is required.")