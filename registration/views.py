from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
#from .forms import UserForm
# Create your views here.


def register_user_view(request):
    users = User.objects.all()
    return HttpResponse(users)

# def product_details_view(request, id):
#     product = get_object_or_404(Product, pk=id)
#     return render(request, "product_details.html", {"product": product})