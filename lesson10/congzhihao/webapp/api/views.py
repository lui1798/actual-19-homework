
from django.shortcuts import render,HttpResponse
import os
import subprocess


# Create your views here.

#打印出hello world
def hello(respond):
    print("-"*44)
    print(dir(respond))
    print("-"*66)
    print(respond.GET)
    #GET自动取是网址"？"后面"键、值"参数，并转成一个字典
    #http://127.0.0.1:8000/hello/?num1=1&num2=11&name=admin&pass=123456
    #<QueryDict: {'num1': ['1'], 'num2': ['11'], 'name': ['admin'], 'pass': ['123456']}>
    return HttpResponse("hello world")

#输入linux命令并打印出来
def command_v1(respond):
    cmd = respond.GET.get("cmd")
    result = os.popen(cmd).read()

    return HttpResponse(result)

#输入linux命令并打印出来。如果命令无效则用红色显示，如果命令正确则用绿色显示正常结果
def command_v3(request):
    cmd = request.GET.get("cmd")
    if cmd:
        print(request.GET)
        pipe = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
        pipe.wait()
        stdout = pipe.stdout.read().decode()
        stderr = pipe.stderr.read().decode()
        if stdout:
            s = '''
            <pre><h2 style="background-color:green">{}</h2></pre>
            '''.format(stdout)
            return HttpResponse(s)
        if stderr:
            s = '''
            <pre><h2 style="background-color:red">{}</h2></pre>
            '''.format(stderr)
            return HttpResponse(s)
        return HttpResponse("error")
    else:
        return HttpResponse("url is wrong(cmd is essential)")

'''http://127.0.0.1:8000/sum/?num1=1&num2=11
输入上面网址，并获取num1和num2的值，返回二者的和
'''
def sssum(request):
    x1 = request.GET.get("num1")
    x2 = request.GET.get("num2")
    if x1 and x2:
        return HttpResponse(int(x1) + int(x2))
    else:
        return HttpResponse("num1 and num2 is required!!")


def file_read(request):
    file = request.GET.get("file")
    cmd = "cat " + file
    result = os.popen(cmd).read()
    print(result)
    return HttpResponse(result)

def page_sum1(request):
    html = '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title></title>
            </head>
            <body>
                
                <form method="get" action="/sum/">
                    num1:<input type="test" name="num1"/>
                    num2:<input type="test" name="num2"/>
                    <input type="submit" value="sum" />
                </form>
                
                
                
                
            </body>
        </html>

    '''
    return HttpResponse(html)

def page_sum2(request):
    cmd = "cat templates/ssum.html"
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    pipe.wait()
    stdout = pipe.stdout.read().decode()
    return HttpResponse(stdout)


def page_sum3(request):
    return render(request,"ssum.html")

def page_sum4(request):
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"templates/ssum.html")
    print(file_path)
    with open(file_path,'r') as f:
        html = f.read()
    return HttpResponse(html)