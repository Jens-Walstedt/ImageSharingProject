from django.db import models
# Create your models here.


class User(models.Model):
    UserName = models.CharField(max_length=20, default="user")
    Password = models.CharField(max_length=50, default="password")
    Name = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50, default="abc@mail.com")

    def __str__(self):
        return self.UserName