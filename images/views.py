from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def upload_view(request):
    return HttpResponse("this is a test")