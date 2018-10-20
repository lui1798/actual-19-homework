from django.shortcuts import render

# Create your views here.


def UsersView(request):
	return render(request, "users.html")