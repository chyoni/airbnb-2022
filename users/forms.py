from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # 이 clean_ 는 정해진 키워드라 이렇게 사용해야만 한다. clean_data 이런식으로
    # 만약 필드 모두에 접근하려면 그냥 clean() 메소드를 사용하면 된다.
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            # forms에서 에러를 raise하면 그 해당 필드에 아래 에러 문구가 노출된다.
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        print("clean password")
