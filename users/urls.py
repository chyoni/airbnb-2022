from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.login_user, name="login"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("login/kakao", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback", views.kakao_callback, name="kakao-callback"),
    path("logout", views.logout_user, name="logout"),
    path("signup", views.signup, name="signup"),
    path(
        "verify/<str:secret>", views.complete_verification, name="complete-verification"
    ),
    path("<int:pk>", views.UserProfileView.as_view(), name="profile"),
    path("<int:pk>/edit", views.editProfile, name="edit-profile"),
    path("<int:pk>/listings", views.usersListings, name="listings"),
    path("change-password/", views.userChangePassword, name="change-password"),
]
