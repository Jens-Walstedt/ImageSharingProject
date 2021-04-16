# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.


# class UserProfile(models.Model):
#      user = models.ForeignKey(User, on_delete=models.CASCADE)
#      bio = models.CharField(max_length=300)
#      profile_pic = models.foreignKey(null=True)
    
#     def __str__(self):
#         return self.pk


# class ImageItem(models.Model):
#     userProfileId = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     imageId = models.foreignKey(Image, on_delete=models.CASCADE)
#     imageOwner = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.pk

   