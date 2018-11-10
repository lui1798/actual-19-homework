from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.

@login_required(login_url="/account/login")
def index(request):
    #return render(request, "dashboard.html")
    return render(request, "index.html")

def command(request):
    return render(request, "command.html")

def hessum(request):
    return render(request, "hessum.html")
