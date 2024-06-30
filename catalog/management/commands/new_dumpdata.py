from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Обновление данных в файлы дампа JSON'

    def handle(self, *args, **kwargs):
        fixtures = [
            ('catalog.Product', 'catalog/fixtures/product.json'),
            ('catalog.ProductVersion', 'catalog/fixtures/productversion.json'),
            ('catalog.ProductCategory', 'catalog/fixtures/productcategory.json'),
            ('blog.Message', 'blog/fixtures/message.json'),
            ('students.Student', 'students/fixtures/student.json'),
            ('auth.Group', 'students/fixtures/student.json'),
            # ('users.User', 'users/fixtures/user.json'),
        ]

        for model, fixture in fixtures:
            call_command('dumpdatautf8', model, indent=4, output=fixture)

        call_command('dumpdatautf8', indent=4, output='data.json')

        self.stdout.write(self.style.SUCCESS('Дампы успешно обновлены'))
