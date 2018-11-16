import csv
import logging
from time import time
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, QueryDict
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Users
from utils.user_valid import valid_userinfo


logger = logging.getLogger(__file__)

@require_http_methods(['GET',])
@login_required
def UserListView(request):
    objs = Users.objects.all()
    logger.debug('List Users Success!')
    return  render(request, "user.html", context={'objs': objs})

@require_http_methods(['POST',])
#@login_required(login_url='/account/login')
def UserAddView(request):
    jsondata = request.POST.dict()
    errors, is_valid = valid_userinfo(jsondata)
    if is_valid:
        Users.objects.create(**jsondata)
        logger.debug('Add User {0} Success!'.format(jsondata['username']))
        return JsonResponse({'code' : 200 })
    else:
        logger.warning('Add User {0} Failed! Errors: {1}'.format(jsondata['username'], errors))
        return JsonResponse({ 'code' : 400 ,'errors' : errors })


@require_http_methods(['PUT',])
@login_required
def UserEditView(request, pk):
    data = QueryDict(request.body).dict()
    data['id'] = pk
    errors, is_valid = valid_userinfo(data)
    if is_valid:
        Users.objects.filter(pk=pk).update(**data)
        logger.debug('Edit User ID {0} Success!'.format(data['id']))
        return JsonResponse({'code' : 200 })
    else:
        logger.warning('Edit User ID {0} Failed! Errors: {1}'.format(data['id'], errors))
        return JsonResponse({ 'code' : 400 ,'errors' : errors })


@require_http_methods(['GET',])
@login_required
def UserDetailView(request):
    uid = request.GET.get('pk')
    try:
        data = Users.objects.get(pk=uid)
    except Exception as e:
        raise e
    else:
        jsondata = model_to_dict(data)
        return JsonResponse(jsondata)

@require_http_methods(['DELETE',])
@login_required
def UserDeleteView(request, pk):
    try:
        data = Users.objects.get(pk=pk)
        data.delete()
        logger.debug('Delete User {0} Success!'.format(data['username']))
    except Exception as e:
        logger.warning('Delete User {0} Failed! Errors: {1}'.format(data['username'], e.args))
        return JsonResponse({"code": 400, "error": "pk {0} not found,error {1}".format(pk, e.args)})
    else:
        return JsonResponse({"code": 200})



def UserExportView(request):
    response = HttpResponse(content_type='text/csv')
    filename = str(time())
    response['Content-Disposition'] = 'attachment; filename=' + filename + '.csv'

    writer = csv.writer(response)
    writer.writerow(['ID', 'username', 'sex', 'age', 'city', 'created_time', 'update_time'])

    search_value = request.GET.get('search_value')
    if search_value:
        objs = Users.objects.filter(username=search_value)
    else:
        objs = Users.objects.all()

    for obj in objs.values_list():
        writer.writerow(list(obj))

    logger.debug('Export Users Success!')
    return response
