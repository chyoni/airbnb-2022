from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . import forms


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
