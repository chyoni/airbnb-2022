from django import template
from lists import models

register = template.Library()


@register.simple_tag
def is_favourites(room, user):
    try:
        list = models.List.objects.get(user=user)

        for r in list.rooms.all():
            if r == room:
                return True
        return False
    except models.List.DoesNotExist:
        return False
