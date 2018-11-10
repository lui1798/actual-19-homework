from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def AccountLoginView(request):
    if request.method == 'POST':
        print("username: ", request.POST.get('username'))
        print("password: ", request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = authenticate(username=username, password=password)
        #redirect_to = request.GET.get('next')
        #print('yutong',redirect_to)
        
        if obj:
            login(request, obj)
            return HttpResponseRedirect("/index")
            #return HttpResponseRedirect(redirect_to)
        else:
            return render(request, "login.html", context={"errmsg": "登录失败"})
    else:
        return render(request, "login.html")

def AccountLogoutView(request):
    logout(request)
    #return render(request, "login.html")
    return HttpResponseRedirect("/account/login")
