from django.urls import path
from . import views

app_name = "conversations"

urlpatterns = [
    path("go/<int:u1_pk>/<int:u2_pk>", views.go_conversations, name="go"),
    path(
        "<int:conversation_pk>",
        views.conversation_detail,
        name="detail",
    ),
    path("<int:conversation_pk>/send", views.send, name="send"),
]
