from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login

# Create your views here.

'''
    用户登录
'''
def AccountLoginView(request):
    print(request.GET.get("next"))
    print(dir(request.session))
    print(dir(request.body))
    print(dir(request))
    print("--------")
    print(request.session.keys())
    print(request.session.session_key)
    print("---")
    import json
    body_unicode = request.body.decode('utf-8')
    print(body_unicode)
    if request.method == 'POST':
        print("username: ", request.POST.get('username'))
        print("password: ", request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = authenticate(username=username, password=password)
        if obj:
            # 登录成功
            # return HttpResponse("login ok.")
            login(request, obj)
            return HttpResponseRedirect("/")
        else:
            # 登录失败
            # return HttpResponse("login failed.")
            return render(request, "login.html", context={"errmsg" : "登录失败"})
    else:
        return render(request, "login.html")




'''
    用户退出
'''
def AccountLogoutView(request):
    logout(request)
    return HttpResponseRedirect("/account/login/")

