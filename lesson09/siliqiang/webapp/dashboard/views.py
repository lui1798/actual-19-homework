from django.shortcuts import render,HttpResponse
import os
import subprocess

# Create your views here.
def catfile(request):
   return render(request,"catfile.html")

def command(request):
    return render(request, "command.html")

def ssum(request):
    return render(request, "ssum.html")