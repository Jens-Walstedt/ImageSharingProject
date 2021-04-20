from django.urls import path
from .views import images_list_view, image_upload_view, edit_image_view, image_detail_view, save_image, delete_image


urlpatterns = [
    path("", images_list_view, name="images_list"),
    path("upload/", image_upload_view, name="image_upload"),
    path("edit/", edit_image_view, name="edit_image"),
    path("detail/<int:id>/", image_detail_view, name="image_detail"),
    path("save_image/<int:id>/", save_image),
    path("delete_image/<int:id>/", delete_image)
]
