import random
from typing import Any, Optional
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help: str = 'This command create reviews'

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many create reviews?"
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        number = options.get("number")
        seeder = Seed.seeder()
        rooms = room_models.Room.objects.all()
        users = user_models.User.objects.all()
        seeder.add_entity(review_models.Review, number, {
            "accuracy": lambda x: random.randint(1, 5),
            "communication": lambda x: random.randint(1, 5),
            "cleanliness": lambda x: random.randint(1, 5),
            "location": lambda x: random.randint(1, 5),
            "check_in": lambda x: random.randint(1, 5),
            "value": lambda x: random.randint(1, 5),
            "room": lambda x: random.choice(rooms),
            "user": lambda x: random.choice(users)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} reviews created !'))
