from django.shortcuts import render, HttpResponse
import subprocess

# Create your views here.


def cmdView(request):
    cmd = request.GET.get('cmd')
    if cmd:
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        pipe.wait()
        stdout = pipe.stdout.read().decode("utf-8")
        stderr = pipe.stderr.read().decode("utf-8")
        if stdout:
            s = '''<pre><h1 style="color: green; font-size: 14px;">{}</h1></pre>'''.format(stdout)
            return HttpResponse(s)

        if stderr:
            s = '''<pre><h1 style="color: red; font-size: 14px;">{}</h1></pre>'''.format(stderr)
            return HttpResponse(s)

        return HttpResponse('''<pre><h1 style="color: red; font-size: 14px;">unknow except.</h1></pre>''')
    else:
        return HttpResponse('''<pre><h1 style="color: red; font-size: 14px;">cmd params is required.</h1></pre>''')


def sumView(request):
    res = {}
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")

    if num1 and num2:
        try:
            num1 = int(num1)
            num2 = int(num2)
        except Exception as e:
            msg = "num1 and num2 params must be int."
            res['status'] = 'error'
            res['data'] = msg
            return render(request, 'sum.html', res)
        s = sum([num1, num2])
        res['status'] = 'success'
        res['data'] = s
        return render(request, 'sum.html', res)
    else:
        msg = "num1 and num2 params is required."
        res['status'] = 'error'
        res['data'] = msg
        return render(request, 'sum.html', res)