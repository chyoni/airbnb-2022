from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room}'

    # 어드민 패널에서 함수를 만들지 않은 이유는 이 함수를 프론트에서도 사용할거라서
    def rating_average(self):
        avg = (
            self.accuracy +
            self.communication +
            self.cleanliness +
            self.location +
            self.check_in +
            self.value) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg"
