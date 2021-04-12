from django.db import models
# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=20, default="user")
    password = models.CharField(max_length=50, default="password")
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="abc@mail.com")

    def __str__(self):
        return self.userName