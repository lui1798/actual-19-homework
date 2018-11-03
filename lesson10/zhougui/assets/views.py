from django.shortcuts import render, redirect, HttpResponse
from assets import models


# Create your views here.
def login(request):
    return render(request, 'login.html')


def index(request):
    obj = models.assetsInfo.objects.all()
    return render(request, 'index.html', context={'obj': obj})


def assetsAdd(request):
    return render(request, 'assetsAdd.html')


def assetsInfo(request, nid):
    obj = models.assetsInfo.objects.filter(id=nid)
    return render(request, 'assetsInfo.html', context={'obj': obj})


def assetsDel(request, nid):
    obj = models.assetsInfo.objects.filter(id=nid).delete()
    return redirect('/assets/')


def assetsEdit(request, nid):
    obj = models.assetsInfo.objects.filter(id=nid)
    return render(request, 'assetsEdit.html', context={'obj': obj})
