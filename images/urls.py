from django.urls import path
from .views import images_list_view, image_upload_view, edit_image_view, image_detail_view, save_image, remove_image


urlpatterns = [
    path("", images_list_view, name="images_list"),
    path("upload/", image_upload_view, name="image_upload"),
    path("detail/<int:id>/", image_detail_view, name="image_detail"),
    path("edit_image/<int:id>/", edit_image_view, name="edit_image"),
    path("save_image/<int:id>/", save_image, name="save_image"),
    path("remove_image/<int:id>/", remove_image, name="remove_image")
]
