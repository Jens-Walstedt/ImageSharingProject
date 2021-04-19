from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def edit_image_view(request):
    
    return render(request, "images/edit_image.html")

def images_list_view(request):
    images = Image.objects.all()
    return render(request, "images/images_list.html", {"images": images})


def image_upload_view(request):
    form = ImageForm()
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #logic add imageitem
            return redirect("images_list")

            

    return render(request, "images/image_upload.html", {"form": form})
