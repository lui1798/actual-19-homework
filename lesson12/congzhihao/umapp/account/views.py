from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
import json
# Create your views here.

def account_login(request):
    print(request.session.keys())
    # print(request.GET.get('next'))
    # print(request.body.count())
    body_unicode = request.body.decode('utf-8')
    print(body_unicode)
    if request.method == "POST":
        print('username:',request.POST.get('username'))
        print('password:',request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = authenticate(username=username,password=password)
        if obj:
            login(request,obj)
            return HttpResponseRedirect('/user/home')
        else:
            return render(request,'login.html',context={"errmsg" : "登录失败"})
    else:
        return render(request,'login.html')

def account_logout(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')


