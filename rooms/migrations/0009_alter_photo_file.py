# Generated by Django 4.1a1 on 2022-06-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0008_alter_photo_room_alter_room_amenities_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="file",
            field=models.ImageField(upload_to="room_photos"),
        ),
    ]