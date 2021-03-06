from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path(
        "create/<int:room_pk>/<int:year>-<int:month>-<int:day>",
        views.create,
        name="create",
    ),
    path(
        "<int:pk>/",
        views.detail,
        name="detail",
    ),
    path("<int:pk>/canceled", views.cancel_reservation, name="cancel"),
    path("<int:pk>/confirmed", views.confirm_reservation, name="confirm"),
]
