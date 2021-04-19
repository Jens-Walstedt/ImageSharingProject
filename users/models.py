from django.db import models
from django.contrib.auth.models import User
from images.models import Image
# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #profile_pic = models.ForeignKey(, on_delete=models.CASCADE, null=True)


class ImageItem(models.Model):
    userProfileId = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    imageId = models.ForeignKey(Image, on_delete=models.CASCADE)
    imageOwner = models.BooleanField(default=False)
    
   