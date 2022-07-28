from django.shortcuts import redirect, render
from django.urls import reverse
from rooms import models as room_models
from . import models


def toggle_room(request, room_pk):

    try:
        room = room_models.Room.objects.get(pk=room_pk)
        user = request.user

        lists = models.List.objects.get(user=user)
        isExist: bool = False

        for r in lists.rooms.all():
            if r == room:
                isExist = True
                break

        if isExist:
            lists.rooms.remove(room)
        else:
            lists.rooms.add(room)

        return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))
    except room_models.Room.DoesNotExist:
        return render(request, "404.html")
    except models.List.DoesNotExist:
        list = models.List.objects.create(user=user, name="My List")
        room = room_models.Room.objects.get(pk=room_pk)
        list.add(room)
        list.save()
        return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))
