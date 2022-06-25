from math import ceil
from django.shortcuts import render
from . import models


def all_rooms(request):
    page: str = request.GET.get("page", 1)
    page = int(page or 1)
    interval: int = 10

    limit: int = interval * page
    offset: int = limit - interval

    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / interval)
    return render(
        request,
        "rooms/home.html",
        context={"rooms": all_rooms, "page": page, "page_count": page_count},
    )
