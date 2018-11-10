from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def AccountLoginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        obj = authenticate(username=username, password=password)

        if obj:
            login(request, obj)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'login.html', context={"errmsg": "登陆失败"})
    else:
        return render(request, "login.html")

def AccountLogoutView(request):
    logout(request)
    return HttpResponseRedirect("/account/login/")


