from django.shortcuts import render,HttpResponseRedirect

from .models import Assets

def assetsView(request):
    objs = Assets.objects.all()
    return render(request,"assets.html", context={'objs': objs})

def deleteAssetsView(request):
    pk = request.GET.get("pk")
    obj = Assets.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect("Delete {} ok".format(obj.hostname))
    #return HttpResponseRedirect("emmby")
