from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "base.html")


def ssum(request):
    return render(request, "sum.html")


def users(request):
    return render(request, "users.html")


def command(request):
    return render(request, "command.html")


