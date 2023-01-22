import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Команда для ожидания БД."""

    def handle(self, *args, **options):
        """Ожидает БД."""
        self.stdout.write('Ожидание БД...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('БД недоступна, ожидаем 1 секунду...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('БД доступна!'))
