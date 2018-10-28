from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "form_sum_new.html")

def command(request):
    return render(request, "command.html")

def ssum(request):
    return render(request, "ssum.html")