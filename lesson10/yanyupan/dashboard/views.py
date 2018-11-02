from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def ssum(request):
    return render(request, "sum.html")


def command(request):
    return render(request, "command.html")