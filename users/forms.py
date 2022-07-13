from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is None:
            raise forms.ValidationError("This field is required")
        if password is None:
            raise forms.ValidationError("This field is required")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignupForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exist with that email")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = models.User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()


class EditForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    language = forms.ChoiceField(
        widget=forms.Select, choices=models.User.LANGUAGE_CHOICES, required=True
    )
    currency = forms.ChoiceField(
        widget=forms.Select, choices=models.User.CURRENCY_CHOICES, required=True
    )

    def clean_first_name(self):
        set_first_name = self.cleaned_data["first_name"]
        if "".__eq__(set_first_name):
            raise forms.ValidationError("First name is required.")
        else:
            return set_first_name

    def clean_last_name(self):
        set_last_name = self.cleaned_data["last_name"]
        if "".__eq__(set_last_name):
            raise forms.ValidationError("Last name is required.")
        else:
            return set_last_name

    def save(self, user):
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        bio = self.cleaned_data["bio"]
        language = self.cleaned_data["language"]
        currency = self.cleaned_data["currency"]

        user = models.User.objects.filter(pk=user.pk).update(
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            language=language,
            currency=currency,
        )
