from django.shortcuts import render


def all_rooms(request):
    hungry = True
    return render(request, template_name="all_rooms.html", context={'hungry': hungry})
