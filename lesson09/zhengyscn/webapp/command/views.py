from django.shortcuts import render

# Create your views here.

def CommandView(request):
	return render(request, "command.html")