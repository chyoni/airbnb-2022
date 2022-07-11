import os
import requests
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core.files.base import ContentFile
from django.contrib import messages
from . import forms, models


def login_user(request):

    if request.method == "GET":
        form = forms.LoginForm()
        return render(request, "users/login.html", context={"form": form})

    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user=user)
                messages.success(request, "Login Successful")
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", context={"form": form})


def logout_user(request):
    logout(request)
    return redirect(reverse("core:home"))


def signup(request):

    if request.method == "GET":
        form = forms.SignupForm()
        return render(request, "users/signup.html", context={"form": form})

    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=email, password=password)
            if user is not None:
                user.verify_email()
                login(request, user=user)
                return redirect(reverse("core:home"))

        return render(request, "users/signup.html", context={"form": form})


def complete_verification(request, secret):
    print(secret)
    try:
        user = models.User.objects.get(email_secret=secret)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # to do: add success message
    except models.User.DoesNotExist:
        # to do: add error message
        pass

    return redirect(reverse("core:home"))


def github_login(request):
    client_id = os.environ.get("GH_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user"
    )


class UserAlreadyExistException(Exception):
    pass


class SocialLoginException(Exception):
    pass


def github_callback(request):
    try:
        code: str = request.GET.get("code", None)
        client_id = os.environ.get("GH_ID")
        client_secret = os.environ.get("GH_SECRET")
        if code is not None:
            response = requests.post(
                url=f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                headers={"Accept": "application/json"},
            )

            if response.ok and response.status_code == 200:
                bearer_token = response.json()["access_token"]
                github_user = requests.get(
                    url="https://api.github.com/user",
                    headers={
                        "Authorization": f"token {bearer_token}",
                        "Accept": "application/json",
                    },
                )
                profile_json = github_user.json()
                username = profile_json.get("login", None)

                if username is not None:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    bio = profile_json.get("bio")

                    try:
                        user = models.User.objects.get(email=email)
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise SocialLoginException(
                                f"This email is already used social login for {user.login_method}"
                            )
                    except models.User.DoesNotExist:
                        user = models.User.objects.create(
                            username=email,
                            first_name=name,
                            bio=bio,
                            email=email,
                            login_method=models.User.LOGIN_GITHUB,
                            email_verified=True,
                        )
                        user.set_unusable_password()
                        user.save()
                    login(request, user)
                    messages.success(request, "Login successful")
                    return redirect(reverse("core:home"))
                else:
                    raise SocialLoginException(
                        "Github username is none. Please make sure your info agree"
                    )
            elif response.json()["error"] is not None:
                raise SocialLoginException(response.json()["error"])
            else:
                raise SocialLoginException("Unexpected error occured")
        else:
            raise SocialLoginException("Invalid redirect")
    except SocialLoginException as socialError:
        messages.error(request, socialError)
        return redirect(reverse("users:login"))


def kakao_login(request):
    kakao_client_id = os.environ.get("KAKAO_CLIENT_ID")

    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={kakao_client_id}&redirect_uri=http://127.0.0.1:8000/users/login/kakao/callback&response_type=code"
    )


def kakao_callback(request):
    try:
        code = request.GET.get("code", None)
        if code is not None:
            kakao_client_id = os.environ.get("KAKAO_CLIENT_ID")

            response = requests.post(
                url=f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={kakao_client_id}&redirect_uri=http://127.0.0.1:8000/users/login/kakao/callback&code={code}&scope=profile_image,gender,account_email,profile_nickname",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            error = response.json().get("error", None)
            if error is not None:
                raise SocialLoginException(error)
            else:
                access_token = response.json().get("access_token")
                user = requests.get(
                    url="https://kapi.kakao.com/v1/oidc/userinfo",
                    headers={"Authorization": f"Bearer {access_token}"},
                )
                email = user.json().get("email", None)
                nickname = user.json().get("nickname", None)
                profile_image = user.json().get("picture", None)
                if email is None:
                    raise SocialLoginException(
                        "Make sure that agree kakao email info you haved"
                    )
                try:
                    kakao_user = models.User.objects.get(email=email)
                    if kakao_user.login_method != models.User.LOGIN_KAKAO:
                        raise SocialLoginException(
                            f"This email is already used social login for {kakao_user.login_method}"
                        )
                except models.User.DoesNotExist:
                    kakao_user = models.User.objects.create(
                        email=email,
                        username=email,
                        first_name=nickname,
                        login_method=models.User.LOGIN_KAKAO,
                        email_verified=True,
                    )
                    kakao_user.set_unusable_password()
                    kakao_user.save()

                    if profile_image is not None:
                        k_profile = requests.get(profile_image)
                        kakao_user.avatar.save(
                            f"{nickname}-avatar", ContentFile(k_profile.content)
                        )
                login(request, kakao_user)
                messages.success(request, "Login successful")
                return redirect(reverse("core:home"))
        else:
            raise SocialLoginException("Invalid redirect")
    except SocialLoginException as socialError:
        messages.error(request, socialError)
        return redirect(reverse("users:login"))


class UserProfileView(DetailView):

    model = models.User
    template_name = "users/detail.html"
    context_object_name = "user_obj"


def editProfile(request, pk):
    try:
        if request.user.pk != pk:
            pass
            # To do: unauthorized screen

        user = models.User.objects.get(pk=pk)
        return render(request, "users/edit.html", {"user": user})
    except models.User.DoesNotExist:
        pass


def usersListings(request):
    pass
