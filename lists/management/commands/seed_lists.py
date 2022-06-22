import random
from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME: str = 'lists'


class Command(BaseCommand):

    help: str = f'This command create {NAME}'

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help=f'How many create {NAME}?'
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        number = options.get("number")
        seeder = Seed.seeder()
        all_rooms = room_models.Room.objects.all()
        users = user_models.User.objects.all()
        seeder.add_entity(list_models.List, number, {
            "user": lambda x: random.choice(users)
        })

        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = all_rooms[random.randint(0, 5):random.randint(6, 30)]

            # to_add는 querySet임, 나는 querySet을 원하는게 아니고 그 안에 요소들을 원함, 자바스크립트에서 ...과 똑같은거
            list_model.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f'{number} {NAME} created !'))
