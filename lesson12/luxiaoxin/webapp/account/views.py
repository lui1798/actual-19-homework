from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def AccountLoginView(request):
    if request.method == "POST":
        username =  request.POST.get('username')
        passwd = request.POST.get('passwd')
        obj = authenticate(username=username, password=passwd)
        if obj:
            #登录成功
            login(request, obj)
            return HttpResponseRedirect("/")
        else:
            #登录失败
            return render(request, "login.html", context={"errmsg": "用户名密码错误！"})
    else:
        return render(request, 'login.html')



def AccountLogoutView(request):
    logout(request)
    return HttpResponseRedirect("/account/login/")
