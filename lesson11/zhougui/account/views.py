from django.shortcuts import render, HttpResponseRedirect
from account import models


# Create your views here.
def index(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def AccountLoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.userInfo.objects.filter(username=username, password=password)
        if obj:
            return HttpResponseRedirect('/home/')
        else:
            return render(request, 'login.html', context={'errmsg': '用户名或密码错误'})
    else:
        return render(request, 'login.html')


def AccountLogoutView(request):
    return HttpResponseRedirect('/')
