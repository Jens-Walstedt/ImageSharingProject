from django.urls import path
from .views import show_user_view, register_user_view


urlpatterns = [
    path("", show_user_view, name="/register/users"),
    path("register/", register_user_view, name="register"),
]