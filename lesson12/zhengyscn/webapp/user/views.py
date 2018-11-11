from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from .models import Users


@require_http_methods(["GET"])
@login_required
def UserListView(request):
    objs = Users.objects.all()
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