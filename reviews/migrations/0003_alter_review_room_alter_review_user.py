# Generated by Django 4.1a1 on 2022-06-18 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0007_alter_room_room_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reviews", "0002_rename_message_review_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="rooms.room",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
