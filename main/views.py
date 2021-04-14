from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def index(request):
    return render(request,'base.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html", {"error": "Invalid username and or password", "username": username})
    return render(request, "login.html", {})


def logout_view(request):
    logout(request)
    return redirect("/")
