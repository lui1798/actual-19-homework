from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Assets

# Create your views here.

def assetsView(request):
    objs = Assets.objects.all()
    '''
        context 必须是字典类型
    '''
    return render(request, "assets.html", context={'objs' : objs})


def deleteAssetsView(request):
    '''
        GET
        /assets/delete/?pk=3
    '''
    pk = request.GET.get("pk")

    obj = Assets.objects.get(pk=pk)
    obj.delete()
    return HttpResponse("Delete {} ok".format(obj.hostname))


'''
    显示添加的html页面
'''
def addPageAssetsView(request):
    '''
        GET
        /assets/delete/?pk=3
    '''
    return render(request, "assets_add_page.html")


def addAssetsView(request):
    '''
        GET
        /assets/add/?hostname=xxx1&public_ip=xx1&private_ip=xxx3&
    '''
    hostname = request.GET.get('hostname')
    public_ip = request.GET.get('public_ip')
    private_ip = request.GET.get('private_ip')

    data = {}
    Assets.objects.create(**data)
    return HttpResponse("Create {} ok.".format(data['hostname']))