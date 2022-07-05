from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.login_user, name="login"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("logout", views.logout_user, name="logout"),
    path("signup", views.signup, name="signup"),
    path("verify/<str:secret>", views.complete_verification, name="complete-verification"),
]
