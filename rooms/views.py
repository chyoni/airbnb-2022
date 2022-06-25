from django.shortcuts import render
from . import models


def all_rooms(request):
    page: str = request.GET.get("page", 1)
    interval: int = 10

    limit: int = interval * int(page)
    offset: int = limit - interval

    all_rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", context={'rooms': all_rooms})
