from django.db import models
from django.contrib.auth.models import User
from images.models import Image
# Create your models here.


#class UserProfile(models.Model, User):
    #userId = models.ForeignKey(User, on_delete=models.CASCADE)
    #profile_pic = models.ForeignKey(, on_delete=models.CASCADE, null=True)


class ImageItemManager(models.Manager):
    def create_ImageItem(self, userId, imageId, imageOwner):
        ImageItem = self.create(userId=userId, imageId=imageId, imageOwner=imageOwner)
        # do something with the book
        return ImageItem

DEFAULT_ID = 1
class ImageItem(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_ID)
    imageId = models.ForeignKey(Image, on_delete=models.CASCADE)
    imageOwner = models.BooleanField(default=False)

    #objects = ImageItemManager()
    
   