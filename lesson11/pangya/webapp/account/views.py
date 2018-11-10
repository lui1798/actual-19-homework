from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth import authenticate,logout,login
# Create your views here.
def AccountLoginView(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        obj=authenticate(username=username, password=password)
        if obj:
            #return HttpResponse("Login ok.")
            login(request,obj)
            return HttpResponseRedirect("/")
        else:
            #return HttpResponse("Login failed.")
            return render(request,"login.html",context={"errmsg":"登录失败"})
    else:
        return render(request, "login.html")

def AccountLogoutView(request):
    #auth.logout
    logout(request)
    return HttpResponseRedirect("/account/login/")
