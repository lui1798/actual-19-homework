from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login

from django.contrib.auth.models import  User

# Create your views here.


def AccountLoginView(request):
    if request.method == 'POST':
        print("username: ", request.POST.get('username'))
        print("password: ", request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = authenticate(username=username,password=password)
        if obj:
            login(request,obj)
            return HttpResponseRedirect("/")
        else:
            return render(request, "login.html", context={"message" : "登录失败"})
    else:
        return render(request,"login.html")

def AccountLogoutView(request):
    logout(request)
    return HttpResponseRedirect("/account/login/")
