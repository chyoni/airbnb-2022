from datetime import timedelta
from . import managers
from django.db import models
from django.utils import timezone
from core import models as core_models


class BookedDay(core_models.TimeStampedModel):

    day = models.DateField()
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.day)

    class Meta:
        verbose_name = "Booked Day"
        verbose_name_plural = "Booked Days"


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        choices=STATUS_CHOICES, max_length=12, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )
    objects = managers.CustomReservationManager()

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    def in_progress(self):
        now = timezone.now().date()
        return (now >= self.check_in) and (now <= self.check_out)

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    # 이거는 어드민 패널에서 볼 때 이쁜 X, Y 표시를 이모티콘으로 보여주는 기능
    in_progress.boolean = True
    is_finished.boolean = True

    def save(self, *args, **kwargs):
        if True:
            start = self.check_in
            end = self.check_out
            difference = end - start

            existing_booked_day = BookedDay.objects.filter(
                day__range=(start, end)
            ).exists()

            if not existing_booked_day:
                super().save(*args, **kwargs)
                for i in range(difference.days + 1):
                    BookedDay.objects.create(
                        day=start + timedelta(days=i), reservation=self
                    )

        super().save(*args, **kwargs)
