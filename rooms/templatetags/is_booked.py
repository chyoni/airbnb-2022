import datetime
from django import template
from reservations import models as reservations_models

register = template.Library()


@register.simple_tag
def is_booked(room, date):
    if date.day == 0:
        return
    else:
        try:
            day = datetime.datetime(date.year, date.month, date.day)
            reservations_models.BookedDay.objects.get(day=day, reservation__room=room)
            return True
        except reservations_models.BookedDay.DoesNotExist:
            return False
