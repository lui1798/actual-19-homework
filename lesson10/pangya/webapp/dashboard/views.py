from django.shortcuts import render
from django.utils.safestring import mark_safe
import subprocess


# Create your views here.

def index(request):
    return render(request, "index.html")


def command(request):
    cmd = request.GET.get('cmd')
    if cmd:
        pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pipe.wait()
        stdout = pipe.stdout.read().decode("utf-8")
        stderr = pipe.stderr.read().decode("utf-8")
        if stdout:
            return render(request, "form_cmd.html", {"cmdresult": stdout})
        if stderr:
            return render(request, "form_cmd.html", {"cmdresult": stderr})
    else:
        return render(request, "form_cmd.html", {"cmdresult": "Unkown except."})


def ssum(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 and num2:
        ssum = int(num1) + int(num2)
        return render(request, 'form_sum_new.html', {'pageHtml': ssum})
    else:
        return render(request, 'form_sum_new.html', {'pageHtml': "num1 or num2 params is required!"})
