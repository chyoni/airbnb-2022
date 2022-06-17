from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {
            "fields": (
                "avatar",
                "gender",
                "bio",
                "birthdate",
                "language",
                "currency",
                "superhost",
            )
        }),
    )
