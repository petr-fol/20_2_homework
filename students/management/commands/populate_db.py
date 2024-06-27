from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'заполнение базы данных для тестирования'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'students/fixtures/student.json')
        self.stdout.write(self.style.SUCCESS('база данных успешно заполнена'))
