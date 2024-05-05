from django.db import models
from slugify import slugify


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    age = models.IntegerField(default=0, verbose_name='Возраст')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f"{self.name} ({self.age})"


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, verbose_name='Ссылка')   # потом сделать через чарфилд
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
        super().save()

    def __str__(self):
        return self.title
