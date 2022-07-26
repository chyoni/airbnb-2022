from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from rooms import models as room_models
from reservations import models as reservation_models
from reviews import forms


def create_review(request, room_pk, reservation_pk):

    if request.method == "POST":

        try:
            form = forms.CreateReviewForm(request.POST)
            room = room_models.Room.objects.get(pk=room_pk)
            reservation = reservation_models.Reservation.objects.get(pk=reservation_pk)

            if form.is_valid():
                form.save(room=room, user=request.user)
                messages.success(request, "Review created")
                return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))

            return render(
                request,
                "reservations/detail.html",
                {"form": form, "reservation": reservation},
            )
        except (
            room_models.Room.DoesNotExist,
            reservation_models.Reservation.DoesNotExist,
            reservation_models.BookedDay.DoesNotExist,
        ):
            messages.error(request, "Page not found.")
            return render(request, "404.html")
