import os

from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request)
    print(dir(request))
    print("get_full_path: ", request.get_full_path())
    print("method: ", request.method)
    print("environ: ", request.environ)
    # return "hello world."
    return HttpResponse("hello world.")

def command_v1(request):
    cmd_exec_response = '''
    Filesystem     Type   Size  Used Avail Use% Mounted on
    /dev/sda3      ext4    37G  5.0G   30G  15% /
    tmpfs          tmpfs  491M     0  491M   0% /dev/shm
    /dev/sda1      ext4   477M   31M  421M   7% /boot

    '''
    return HttpResponse(cmd_exec_response)

def command_v2(request):
    cmd = request.GET.get('cmd')
    cmd_exec_response = os.popen(cmd).read()
    return HttpResponse(cmd_exec_response)

def command_v3(request):
    cmd = request.GET.get('cmd')
    pipe = subproces.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    pipe.wait()
    stdout = pipe.stdout.read()
    stdout = pipe.stderr.read()
    if stdout:
        return HttpResponse(stdout)

    if stderr:
       return HttpResponse(stderr)
       s = '''<h1 style="background-color: red;">{}</h1>'''.format(stderr)
       return HttpResponse(s)
    return HttpResponse("unknow except.")

def ssum(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    s = sum([int(num1), int(num2)])
    return HttpResponse(s)

def pageSum(request):
    htmlStr = '''
    <!DOCTYPE html>
<html>
    <head>
    <meta charset="UTF-8">
    <title></title>
    </head>
    <body>
        <form>
           num1: <input type='text' />  
           num2: <input type='text' />
           <input type="button" value='求和'/>
        </form>
    </body>
</html>
   '''

