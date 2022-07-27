from django.urls import path
from . import views


app_name = "lists"

urlpatterns = [path("<int:room_pk>/toggle", views.toggle_room, name="toggle-list")]
