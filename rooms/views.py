from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
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
