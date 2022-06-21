import random
from typing import Any, Optional
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
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} rooms created !'))
