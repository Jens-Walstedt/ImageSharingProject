from django.urls import path
from .views import show_user_view, register_user_view


urlpatterns = [
    path("", show_user_view, name="register"),
    path("register/", register_user_view, name="user_register"),
]