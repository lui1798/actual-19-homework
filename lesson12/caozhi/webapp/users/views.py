from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, QueryDict
from django.forms.models import model_to_dict

from .models import Users
import logging
logger = logging.getLogger(__file__)


@require_http_methods(["GET",])
@login_required(login_url="/account/login")
def UserListView(request):
    objs = Users.objects.all()
    logger.debug("objs {}".format(objs))
    return render(request, "user.html", context={"content": objs})

@require_http_methods(["DELETE",])
@login_required(login_url="/account/login")
def UserDeleteView(request, pk):
    try:
        Users.objects.get(pk=pk).delete()
    except Exception as e:
        return JsonResponse({"code":-1,"msg":"pk {} not found,errmsg {}".format(pk, e.args)})
    else:
        return JsonResponse({"code":0,"msg":"delete pk {} ok.".format(pk)})


def valid_userinfo(jsondata):
    logger.debug("jsondata {}".format(jsondata))
    if isinstance(jsondata, dict):
        for k, v in jsondata.items():
            if v == "":
                return "key {},value is required".format(k), False
            if 'sex' in jsondata:
                sex = jsondata.get('sex')
                if sex.isdigit() and sex in ['0', '1']:
                    pass
                else:
                    return "sex params is invalid", False
    return "", True


@require_http_methods(["POST"])
@login_required(login_url="/account/login")
def UserAddView(request):
    jsondata = request.POST.dict()
    logger.debug("jsondata {}".format(jsondata))
    result, ok = valid_userinfo(jsondata)
    if not ok:
        return HttpResponse(result)
    else:
        Users.objects.create(**jsondata)
        return HttpResponse({"code":0, "msg": "Update ok"})


@require_http_methods(["PUT",])
@login_required(login_url="/account/login")
def UserEditView(request, pk):
    jsondata = QueryDict(request.body).dict()
    logger.debug("jsondata {}".format(jsondata))
    try:
        Users.objects.filter(pk=pk).update(**jsondata)
    except Exception as e:
        return JsonResponse({"code": -1, "msg": "pk {} not found, errmsg {}".format(pk, e.args)})
    else:
        return HttpResponse("ok")

@require_http_methods(["GET",])
@login_required(login_url="/account/login")
def UserDetailView(request):
    pk = request.GET.get("pk")
    try:
        obj = Users.objects.get(pk=pk)
    except Exception as e:
        return JsonResponse({"code": -1, "msg": "pk {} not found, errmsg {}".format(pk, e.args)})
    else:
        logger.debug("jsondata {}".format(jsondata))
        jsondata = model_to_dict(obj)
        return JsonResponse({"code":0, "data":jsondata})
































