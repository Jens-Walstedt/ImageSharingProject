from django.urls import path
from .views import pics_list_view


urlpatterns = [
    path("", pics_list_view, name="pics_list")
]