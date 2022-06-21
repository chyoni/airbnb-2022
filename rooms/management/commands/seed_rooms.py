import random
from typing import Any, Optional
from django.contrib.admin.utils import flatten
from django_seed import Seed
from django.core.management.base import BaseCommand
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help: str = 'This command create rooms'

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many create room?"
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        number: int = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_room_type = room_models.RoomType.objects.all()
        seeder.add_entity(room_models.Room, number, {
            'name': lambda x: seeder.faker.address(),
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x: random.choice(all_room_type),
            'price': lambda x: random.randint(1, 300),
            'guests': lambda x: random.randint(1, 5),
            'beds': lambda x: random.randint(1, 5),
            'bedrooms': lambda x: random.randint(1, 5),
            'baths': lambda x: random.randint(1, 5)
        })
        inserted_rooms = seeder.execute()
        # list는 dict_values를 list로 바꿔주는거고 flatten은 [[]] -> [] 로 바꿔줌
        inserted_clean = flatten(list(inserted_rooms.values()))
        for pk in inserted_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f'/room_photos/{random.randint(1, 31)}.webp',
                    room=room
                )
        self.stdout.write(self.style.SUCCESS(f'{number} rooms created !'))
