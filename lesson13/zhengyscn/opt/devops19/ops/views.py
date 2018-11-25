from django.shortcuts import render

# Create your views here.


def OpsView(request):
    return render(request, "ops.html")


def OpsV2View(request):
    return render(request, "ops2.html")

def OpsV3View(request):
    return render(request, "ops3.html")


def OpsV4View(request):
    return render(request, "ops4.html")