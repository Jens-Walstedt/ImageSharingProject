from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm


def show_user_view(request):
    users = User.objects.all()
    return HttpResponse(users)


def register_user_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password1"))
            if user is not None:
                login(request, user)
                return redirect("/register/showusers")
            else:
                return render(request, "register.html", {"form": form})
    
    return render(request, "register.html", {"form": form})

# def product_details_view(request, id):
#     product = get_object_or_404(Product, pk=id)
#     return render(request, "product_details.html", {"product": product})