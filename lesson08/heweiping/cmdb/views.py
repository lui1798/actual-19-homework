from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

# def index(request):
#     t = loader.get_template("test.html")
#     print(request.GET)
#     print(request.POST)
#     # {{ 变量 }} 书写格式
#     context = {"name": "hello new world"}
#     return HttpResponse(t.render(context, request))

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password == '123456':
            #return HttpResponse('Login Success')
            return render(request, 'cmd.html')
        else:
            return HttpResponse('Login failed')
    else:
        return render(request,'login.html')
