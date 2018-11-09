from django.shortcuts import render,HttpResponse
from .models import Assets

# Create your views here.

def assetsView(request):
    objs = Assets.objects.all()
    return render(request, "assets.html", context={ 'objs' : objs })

def assetsDelete(request):
    pk = request.GET.get('pk')
    obj = Assets.objects.get(pk=pk)
    obj.delete()
    return HttpResponse("Delete {} ok".format(obj.hostname))
