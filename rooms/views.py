from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django_countries import countries
from . import models


def all_rooms(request):
    """all rooms on Home"""
    page: str = request.GET.get("page", 1)

    # 아래 코드가 쿼리셋을 바로 즉시 불러올거라고 에상하겠지만, 쿼리셋은 게으르다. 그래서 이 쿼리셋을 어디선가 호출하여 사용하지 않는 이상 그 때까지는 가져오지 않는다.
    room_list = models.Room.objects.all()

    paginator = Paginator(room_list, 10, orphans=3)

    try:
        rooms = paginator.page(page)
        return render(
            request,
            "rooms/home.html",
            context={"rooms": rooms},
        )
    except EmptyPage:
        rooms = paginator.page(1)
        return redirect("/?page=1")


def room_detail(request, pk):
    """Room detail method"""
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))


def search(request):
    city: str = request.GET.get("city", "Maldives")
    country: str = request.GET.get("country", "KR")
    room_type: int = int(request.GET.get("room_type", 0))
    room_types = models.RoomType.objects.all()

    print(room_type)

    in_urls = {
        "selected_city": city,
        "selected_country": country,
        "selected_room_type": room_type,
    }
    choices = {
        "countries": countries,
        "room_types": room_types,
    }
    return render(
        request,
        "rooms/search.html",
        context={**in_urls, **choices},
    )
