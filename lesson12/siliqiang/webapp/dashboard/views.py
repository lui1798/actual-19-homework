from django.shortcuts import render,HttpResponse

# Create your views here.

# def index(request):
#    return render(request,"form_sum_new.html")

def index(request):
    return render(request,"index.html")