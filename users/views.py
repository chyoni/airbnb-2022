import os
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
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


def github_callback(request):
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
                    if user is not None:
                        return redirect(reverse("users:login"))
                except models.User.DoesNotExist:
                    new_github_user = models.User.objects.create(
                        username=email, first_name=name, bio=bio, email=email
                    )
                    login(request, new_github_user)
                    return redirect(reverse("core:home"))
            else:
                return redirect(reverse("users:login"))
        elif response.json()["error"] is not None:
            print(response.json()["error"])
            return redirect(reverse("core:home"))
        else:
            return redirect(reverse("core:home"))
    else:
        return redirect(reverse("core:home"))
