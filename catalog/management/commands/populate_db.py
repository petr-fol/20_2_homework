from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'заполнение базы данных для тестирования'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'catalog/fixtures/product.json')
        call_command('loaddata', 'catalog/fixtures/productversion.json')
        call_command('loaddata', 'catalog/fixtures/productcategory.json')
        call_command('loaddata', 'blog/fixtures/message.json')
        call_command('loaddata', 'students/fixtures/student.json')
        call_command('loaddata', 'groups.json')
        # call_command('loaddata', 'users/fixtures/user.json')
        self.stdout.write(self.style.SUCCESS('база данных успешно заполнена'))
