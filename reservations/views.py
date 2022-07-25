import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from rooms import models as room_models
from . import models


def create(request, room_pk, year, month, day):

    try:
        room_models.Room.objects.get(pk=room_pk)
        day = datetime.datetime(year, month, day)
        models.BookedDay.objects.get(day=day)
    except room_models.Room.DoesNotExist:
        return render(request, "404.html")
    except models.BookedDay.DoesNotExist:
        room = room_models.Room.objects.get(pk=room_pk)
        reservation = models.Reservation.objects.create(
            check_in=day,
            check_out=day + datetime.timedelta(days=1),
            guest=request.user,
            room=room,
        )
        messages.success(request, "Reservation created")
        return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


def detail(request, pk):
    pass
