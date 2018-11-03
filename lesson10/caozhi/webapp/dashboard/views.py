from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "dashboard.html")

def command(request):
    return render(request, "command.html")

def hessum(request):
    return render(request, "hessum.html")
