from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ["name", "used_by"]

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    # inlines는 admin안에 admin을 넣을 수 있는데 이게 가능한 이유는
    # room 안에 photo가 있다는 것을 우리 장고가 알기 때문에! (relationship)
    inlines = [PhotoInline]

    fieldsets = [
        (
            "Basic Info",
            {"fields": ["name", "description", "city", "country", "address", "price"]},
        ),
        ("Times", {"fields": ["check_in", "check_out"]}),
        ("Spaces", {"fields": ["guests", "beds", "bedrooms", "baths"]}),
        (
            "More About the Space",
            {
                "classes": ["collapse"],
                "fields": ["room_type", "amenities", "facilities", "house_rules"],
            },
        ),
        ("Last Details", {"fields": ["host"]}),
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
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = [
        "instant_book",
        "city",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
    ]

    raw_id_fields = ["host"]

    search_fields = ["name", "city", "host__username"]

    filter_horizontal = ["amenities", "facilities", "house_rules"]

    # self 이 클래스를 말하고 obj는 한 행(row)을 말함
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = ["__str__", "get_thumbnail"]

    # Django는 너무 훌륭해서 함부로 input을 사용하지 못하게 막는다. 그래서 장고야 이건 안전해 ! 라고 말해주는게 mark_safe method이다.
    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="120px" src="{obj.file.url}"/>')

    get_thumbnail.short_description = "Thumbnail"
