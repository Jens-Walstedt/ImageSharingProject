from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'base.html')

def login(request):
    return HttpResponse("Login site")