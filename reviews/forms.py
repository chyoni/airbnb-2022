from django import forms
from . import models


class CreateReviewForm(forms.Form):

    review = forms.CharField(widget=forms.Textarea, required=True)
    accuracy = forms.IntegerField(required=True, min_value=0, max_value=5)
    communication = forms.IntegerField(required=True, min_value=0, max_value=5)
    cleanliness = forms.IntegerField(required=True, min_value=0, max_value=5)
    location = forms.IntegerField(required=True, min_value=0, max_value=5)
    check_in = forms.IntegerField(required=True, min_value=0, max_value=5)
    value = forms.IntegerField(required=True, min_value=0, max_value=5)

    def save(self, room, user):
        models.Review.objects.create(
            review=self.cleaned_data["review"],
            accuracy=self.cleaned_data["accuracy"],
            communication=self.cleaned_data["communication"],
            cleanliness=self.cleaned_data["cleanliness"],
            location=self.cleaned_data["location"],
            check_in=self.cleaned_data["check_in"],
            value=self.cleaned_data["value"],
            user=user,
            room=room,
        )
