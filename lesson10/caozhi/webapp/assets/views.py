from django.shortcuts import render

from .models import Assets

def assetsView(request):
    objs = Assets.objects.all()
    return render(request,"assets.html", context={'objs': objs})

def deleteAssetsView(request):
    pk = request.GET.get("pk")
    obj = Assets.get(pk=pk)
    obj.delete()
    return HttpResponse("Delete {} ok".format(obj.hostname))
