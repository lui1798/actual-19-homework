from django.shortcuts import render,HttpResponse
import os

# Create your views here.
def home(request):
    context = dict()
    context["home"] = "首页"
    return render(request,"form_home.html",context=context)

def index(request):
    context = dict()
    context["home"] = "首页"
    context["constra"] = "本系统包含命令执行、求和功能，见左侧边框"
    return render(request,"form_home.html",context=context)

def ssum(request):
    context = dict()
    context["home"] = "求和功能"
    context["action"] = "http://127.0.0.1:8000/ssum?"
    x1 = request.GET.get("n1")
    x2 = request.GET.get("n2")
    if x1 or x2:
        try:
            s = int(x1) + int(x2)
            context["constra"] = "{}+{}={}：".format(x1, x2, s)
        except:
            context["constra"] = "输入值类型不符"

    return render(request,"form_sum.html",context=context)


def cmd1(request):
    context = dict()
    context["action"] = "http://127.0.0.1:8000/cmd?"
    context["home"] = "命令执行"
    cmd1 = request.GET.get("cmd1",False)
    if cmd1:
        result = os.popen(cmd1).read()
        context["constra"] = "{}--命令的执行结果：".format(cmd1)
        context["result"] = result
    return render(request,"form_cmd.html",context=context)






