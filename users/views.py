from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import UserForm


def created_user_view(request, id):
    user = get_object_or_404(User, pk=id)
    return HttpResponse(user)


def register_user_view(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password1"))
            if user is not None:
                login(request, user)
                return redirect("users/success/" + str(user.pk))
            else:
                return render(request, "register.html", {"form": form})
    
    return render(request, "register.html", {"form": form})

# def product_details_view(request, id):
#     product = get_object_or_404(Product, pk=id)
#     return render(request, "product_details.html", {"product": product})