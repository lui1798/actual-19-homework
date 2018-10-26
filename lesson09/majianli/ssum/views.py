from django.shortcuts import render

# Create your views here.

def ssum(request):
    print(request.GET)
    return render(request, "ssum.html")
