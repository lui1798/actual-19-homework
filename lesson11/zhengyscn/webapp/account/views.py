from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, QueryDict, Http404
from django.contrib import auth
from django.utils.decorators import method_decorator

# Create your views here.


def AccountLoginView(request):
	if request.method == 'GET':
		return render(request, "login.html")
	else:
		username = request.POST.get("username", None)
		password = request.POST.get("password", None)
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect("/")
			else:
				return render(request, "login.html", {"errmsg" : "用户 {} 被禁用".format(username)})
		else:
			return render(request, "login.html", {"errmsg": "用户名 或 密码错误"})


def AccountLogoutView(request):
	auth.logout(request)
	return HttpResponseRedirect("/account/login/")

