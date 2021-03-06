# Generated by Django 4.1a1 on 2022-06-22 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0009_alter_photo_file"),
        ("lists", "0002_alter_list_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list",
            name="rooms",
            field=models.ManyToManyField(
                blank=True, related_name="lists", to="rooms.room"
            ),
        ),
    ]
