import itertools

from django.db import models
from slugify import slugify


# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, verbose_name='Ссылка', unique=True)   # потом сделать через чарфилд
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Изображение',
                              default='images/default.jpg')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    # author = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, separator='-')
            for x in itertools.count(1):
                if not Message.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f'{slugify(self.title)}-{x}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
