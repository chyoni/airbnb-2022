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
                "email_verified",
            )
        }),
    )

    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'language',
        'currency',
        'is_active',
        'is_staff',
        'is_superuser',
        'superhost',
        "email_verified",
        "email_secret",
    ]

    list_filter = UserAdmin.list_filter + (
        'superhost',
    )
