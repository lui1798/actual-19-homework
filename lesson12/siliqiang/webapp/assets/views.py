from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Assets

# Create your views here.

# def assetsView(request):
#     objs = Assets.objects.all()
#     return render(request, "assets.html", context={ 'objs' : objs })
#
# def assetsDelete(request):
#     pk = request.GET.get('pk')
#     obj = Assets.objects.get(pk=pk)
#     obj.delete()
#     return HttpResponse("Delete {} ok".format(obj.hostname))

@require_http_methods(["GET",])
@login_required(login_url="/account/login/")
def AssetsListView(request):
    search_value = request.GET.get('search_value')
    if search_value:
        objs = Assets.objects.filter(hostnam=search_value)
    else:
        objs = Assets.objects.all()
    return render(request,"assets.html",context={"content" : objs})

@require_http_methods(["POST",])
def AssetsAddView(request):
    data = request.POST.dict()
    Assets.objects.create(**data)
    return HttpResponse("Create ok")

@require_http_methods(["DELETE",])
@login_required(login_url="/account/login/")
def AssetsDeleteView(request,pk):
    Assets.objects.get(pk=pk).delete()
    return HttpResponse("Delete ok.")