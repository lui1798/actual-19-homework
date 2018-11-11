from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse, QueryDict
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

from .models import Users

from utils.user_valid import valid_userinfo


import logging
logger = logging.getLogger(__file__)


@require_http_methods(["GET"])
@login_required
def UserListView(request):
    objs = Users.objects.all()
    logger.debug("-----")
    return render(request, "user.html", context={"content" : objs})


@require_http_methods(["DELETE"])
@login_required
def UserDeleteView(request, pk):
    try:
        Users.objects.get(pk=pk).delete()
    except Exception as e:
        return JsonResponse({"code" : -1, "msg" : "pk {} not found, errmsg {}".format(pk, e.args)})
    else:
        return JsonResponse({"code": 0, "msg": "Delete pk {} ok.".format(pk)})



@require_http_methods(["POST"])
# @login_required
def UserAddView(request):
    jsondata = request.POST.dict()
    result, ok = valid_userinfo(jsondata)
    if not ok:
        return HttpResponse(result)
    else:
        Users.objects.create(**jsondata)
        return HttpResponse("ok")


@require_http_methods(["PUT"])
@login_required
def UserEditView(request, pk):
    # print(pk)
    print(request.body)
    print(QueryDict(request.body))
    jsondata = QueryDict(request.body).dict()
    print(jsondata)
    try:
        Users.objects.filter(pk=pk).update(**jsondata)
    except Exception as e:
        return JsonResponse({"code": -1, "msg": "pk {} not found, errmsg {}".format(pk, e.args)})
    else:
        return JsonResponse({"code": 0, "msg": "Update ok."})


@require_http_methods(["GET"])
@login_required
def UserDetailView(request):
    pk = request.GET.get("pk")
    try:
        obj = Users.objects.get(pk=pk)
    except Exception as e:
        return JsonResponse({"code": -1, "msg": "pk {} not found, errmsg {}".format(pk, e.args)})
    else:
        jsondata = model_to_dict(obj)
        return JsonResponse({"code": 0, "data" : jsondata})









