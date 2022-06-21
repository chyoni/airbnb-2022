from typing import Any, Optional
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that i love you?"
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        times = options.get('times')
        for time in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS('i love u'))
