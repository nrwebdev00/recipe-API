# Django Command to wait for db

import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    # Django Command to Wait for DB

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Databse is Still Loading, '
                                  'Waiting For DataBase...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is Loaded.'))
