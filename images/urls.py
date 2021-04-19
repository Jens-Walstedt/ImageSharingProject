from django.urls import path
from .views import images_list_view, image_upload_view, edit_image_view


urlpatterns = [
    path("", images_list_view, name="images_list"),
    path("upload/", image_upload_view, name="image_upload"),
    path("edit/", edit_image_view)
]
