from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django_countries import countries
from django.contrib import messages
from rooms import forms
from . import models


def all_rooms(request):
    """all rooms on Home"""
    page: str = request.GET.get("page", 1)

    # 아래 코드가 쿼리셋을 바로 즉시 불러올거라고 에상하겠지만, 쿼리셋은 게으르다. 그래서 이 쿼리셋을 어디선가 호출하여 사용하지 않는 이상 그 때까지는 가져오지 않는다.
    room_list = models.Room.objects.all().order_by("-created")

    paginator = Paginator(room_list, 30, orphans=5)

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
    price: int = int(request.GET.get("price", 0))
    guests: int = int(request.GET.get("guests", 0))
    bedrooms: int = int(request.GET.get("bedrooms", 0))
    beds: int = int(request.GET.get("beds", 0))
    baths: int = int(request.GET.get("baths", 0))
    s_amenities: list = request.GET.getlist("amenities")
    s_facilities: list = request.GET.getlist("facilities")
    s_house_rules: list = request.GET.getlist("house_rules")
    instant: bool = bool(request.GET.get("instant"))
    superhost: bool = bool(request.GET.get("superhost"))

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    house_rules = models.HouseRule.objects.all()

    in_urls = {
        "selected_city": city,
        "selected_country": country,
        "selected_room_type": room_type,
        "selected_amenities": s_amenities,
        "selected_facilities": s_facilities,
        "selected_house_rules": s_house_rules,
        "selected_instant": instant,
        "selected_superhost": superhost,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
    }
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
        "house_rules": house_rules,
    }

    filter_args = {}

    if city != "":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if superhost is True:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        filter_amenities = []
        for s_ame in s_amenities:
            filter_amenities.append(int(s_ame))
        filter_args["amenities__pk__in"] = filter_amenities

    if len(s_facilities) > 0:
        filter_facilities = []
        for s_ame in s_facilities:
            filter_facilities.append(int(s_ame))
        filter_args["facilities__pk__in"] = filter_facilities

    if len(s_house_rules) > 0:
        filter_house_rules = []
        for s_ame in s_house_rules:
            filter_house_rules.append(int(s_ame))
        filter_args["house_rules__pk__in"] = filter_house_rules

    qs = models.Room.objects.filter(**filter_args).order_by("-created")

    paginator = Paginator(qs, 30, orphans=5)

    page = request.GET.get("page", 1)

    rooms = paginator.get_page(page)

    return render(
        request,
        "rooms/search.html",
        context={**in_urls, **choices, "rooms": rooms},
    )


def room_edit(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)

        if request.user != room.host:
            return render(request, "401.html")

        amenities = models.Amenity.objects.all()
        selected_amenities = room.amenities.all()
        c_amenities = ()

        facilities = models.Facility.objects.all()
        selected_facilities = room.facilities.all()
        c_facilities = ()

        house_rules = models.HouseRule.objects.all()
        selected_house_rules = room.house_rules.all()
        c_house_rules = ()

        room_type = models.RoomType.objects.all()

        is_checked = False
        for a in amenities:
            for s_a in selected_amenities:
                if a.pk == s_a.pk:
                    is_checked = True
            if is_checked is True:
                c_amenities = c_amenities + ((a.pk, a.name, "checked"),)
            else:
                c_amenities = c_amenities + ((a.pk, a.name, "unchecked"),)
            is_checked = False

        for a in facilities:
            for s_a in selected_facilities:
                if a.pk == s_a.pk:
                    is_checked = True
            if is_checked is True:
                c_facilities = c_facilities + ((a.pk, a.name, "checked"),)
            else:
                c_facilities = c_facilities + ((a.pk, a.name, "unchecked"),)
            is_checked = False

        for a in house_rules:
            for s_a in selected_house_rules:
                if a.pk == s_a.pk:
                    is_checked = True
            if is_checked is True:
                c_house_rules = c_house_rules + ((a.pk, a.name, "checked"),)
            else:
                c_house_rules = c_house_rules + ((a.pk, a.name, "unchecked"),)
            is_checked = False

        if request.method == "GET":

            form = forms.RoomEditForm(room=room)
            return render(
                request,
                "rooms/edit.html",
                {
                    "form": form,
                    "c_amenities": c_amenities,
                    "c_facilities": c_facilities,
                    "c_house_rules": c_house_rules,
                    "room_type": room_type,
                },
            )

        if request.method == "POST":
            form = forms.RoomEditForm(request.POST, room=room)

            if form.is_valid():
                form.save(room)
                messages.success(request, "Update room successfully")
                return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))

            messages.error(request, "Something wrong")
            return render(
                request,
                "rooms/edit.html",
                {
                    "form": form,
                    "c_amenities": c_amenities,
                    "c_facilities": c_facilities,
                    "c_house_rules": c_house_rules,
                    "room_type": room_type,
                },
            )

    except models.Room.DoesNotExist:
        return render(request, "404.html")
