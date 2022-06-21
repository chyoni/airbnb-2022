from typing import Any, Optional
from django_seed import Seed
from django.core.management.base import BaseCommand
from users import models as user_models


class Command(BaseCommand):

    help: str = 'This command create users'

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many create user?"
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        number: int = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(user_models.User, number, {
            "is_staff": False,
            "is_superuser": False
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} users created !'))
