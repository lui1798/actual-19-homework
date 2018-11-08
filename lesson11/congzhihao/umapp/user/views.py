#coding:utf-8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from user.models import Users
import csv
import codecs

# Create your views here.
def user_home(request):
    return render(request,"users.html")

def user_list(request):
    all_users = Users.objects.all()

    return render(request,'userlist.html',context={'users':all_users})

def user_detail(request):
    user_id = request.GET.get("id")
    user = Users.objects.get(id=user_id)

    return render(request,"userdetail.html",context={"user":user})

def user_delete(request):
    user_id = request.GET.get("id")
    user = Users.objects.get(id=user_id)
    user.delete()
    return HttpResponse('delete id({}) successfully'.format(user_id))

def user_update(request):
    user_info = request.POST.dict()
    id = user_info.get('id')
    user_info.pop('id')
    Users.objects.filter(id=id).update(**user_info)
    return HttpResponseRedirect('/user/list')


def user_add(request):
    user_info = request.POST.dict()
    if user_info['username'] and user_info['address'] and user_info['id_card']:
        Users.objects.create(**user_info)
    else:
        raise Exception("界面字段不能为空")
    return HttpResponseRedirect('/user/list')

def user_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="allusers.csv"'
    writer = csv.writer(response)
    response.write(codecs.BOM_UTF8) #避免中文乱码
    objs = Users.objects.all()
    writer.writerow(['id', '姓名', '性别', '地址', '备注', '身份证号', '年龄', '创建日期', '修改日期'])
    for obj in objs:
        writer.writerow([obj.id, obj.username, obj.gender, obj.address,obj.remark,obj.id_card,obj.create_time,obj.update_time])
    return response