from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = ("username", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
