from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition"""

    fieldsets = [
        (
            "Basic Info",
            {"fields": ['name', 'description', 'country', 'address', 'price']}
        ),
        (
            "Times",
            {"fields": ['check_in', 'check_out']}
        ),
        (
            "Spaces",
            {"fields": ['guests', 'beds', 'bedrooms', 'baths']}
        ),
        (
            "More About the Space",
            {
                'classes': ['collapse'],
                "fields": ['room_type', 'amenities', 'facilities', 'house_rules']
            }
        ),
        (
            "Last Details",
            {"fields": ['host']}
        )
    ]

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities"
    )

    list_filter = [
        'instant_book', 'city', "host__superhost",
        'room_type', 'amenities',
        'facilities', 'house_rules'
        ]

    search_fields = ['city', 'host__username']

    filter_horizontal = ['amenities', 'facilities', 'house_rules']

    # self 이 클래스를 말하고 obj는 한 행(row)을 말함
    def count_amenities(self, obj):
        print(obj.amenities.all())


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
