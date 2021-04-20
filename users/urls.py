from django.urls import path
from .views import created_user_view, register_user_view, profile_view


urlpatterns = [
    path("profile/", profile_view, name="profile"), 
    path("success/<int:id>", created_user_view, name="created_user"),
    path("register/", register_user_view, name="register"),
    
]

# Qwerty4321