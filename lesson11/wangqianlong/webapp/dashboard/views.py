from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def command(request):
    return render(request,"form_command.html")

def s_sum(request):
    return render(request,"form_ssum.html")
