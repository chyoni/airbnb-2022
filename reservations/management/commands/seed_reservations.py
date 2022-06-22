from datetime import datetime, timedelta
import random
from typing import Any, Optional
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models

NAME: str = 'reservations'


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
        seeder.add_entity(reservation_models.Reservation, number, {
            "status": lambda x: random.choice(['pending', 'confirmed', 'canceled']),
            "guest": lambda x: random.choice(users),
            "room": lambda x: random.choice(all_rooms),
            "check_in": lambda x: datetime.now() - timedelta(days=random.randint(3, 25)),
            "check_out": lambda x: datetime.now() + timedelta(days=random.randint(3, 25))
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} {NAME} created !'))
