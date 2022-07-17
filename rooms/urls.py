from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>/", views.room_detail, name="detail"),
    path("<int:pk>/edit", views.room_edit, name="edit"),
    path("<int:pk>/photos", views.edit_photos, name="photos"),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/delete",
        views.delete_photo,
        name="delete-photo",
    ),
    path("search/", views.search, name="search"),
]
