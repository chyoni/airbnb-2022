from django import forms
from . import models


class SendForm(forms.Form):

    message = forms.CharField(max_length=150, required=True)

    def save(self, user, conversation):
        message = self.cleaned_data["message"]

        models.Message.objects.create(
            message=message, user=user, conversation=conversation
        )
