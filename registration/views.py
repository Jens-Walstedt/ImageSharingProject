from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from .forms import UserForm
# Create your views here.


def show_user_view(request):
    users = User.objects.all()
    return HttpResponse(users)

def register_user_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/register/showusers")
        else:
            return render(request, "register.html", {"form": form})
    else:
        form = UserForm()
    return render(request, "register.html", {"form": form})

# def product_details_view(request, id):
#     product = get_object_or_404(Product, pk=id)
#     return render(request, "product_details.html", {"product": product})