from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image
from users.models import ImageItem, ImageItemManager
from users.forms import ImageItemForm
from django.contrib.auth.decorators import login_required

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
            task = form.save() 
            ImageItem.objects.create_ImageItem(userId=request.user,
            imageId=task,
            imageOwner=True)
            return redirect("images_list")

            

    return render(request, "images/image_upload.html", {"form": form})

@login_required
def image_detail_view(request, id):
    image = get_object_or_404(Image, pk=id)
    UserInfo = ImageItem.objects.get(imageId=image, imageOwner=True).userId
    savedImage = None
    
    #if owner
    try:
        savedImage = ImageItem.objects.get(imageId=id, userId=request.user)
    except:
        pass

    return render(request, "images/image_detail.html", {"image": image, "userinfo": UserInfo, "savedImage": savedImage})
    
    # form = ImageForm()
    # if request.method == "POST":
    #     form = ImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         ImageItem.objects.create_ImageItem(userId=request.user,
    #             imageId=image,
    #             imageOwner=False)
    #         return redirect("profile")
    #     else:
    #         return render(request, "images/image_detail.html", {"error": "This user already has this image", "image": image, "userinfo": UserInfo})

        

@login_required
def save_image(request, id):
    #id = request.GET.get("id")
    image = get_object_or_404(Image, pk=id)
    savedImage = ImageItem.objects.filter(imageId=image, userId=request.user)
    if not savedImage.exists():
        savedImage = ImageItem(userId=request.user, imageId=image, imageOwner=False)
        savedImage.save()
    return redirect("image_detail", id=id)

@login_required
def remove_image(request, id):
    #id = request.GET.get("id")
    image = get_object_or_404(Image, pk=id)
    savedImage = ImageItem.objects.filter(imageId=id, userId=request.user)
    if savedImage.exists():
        savedImage.delete()
    return redirect("image_detail", id=id)