import itertools

from django.db import models
from django.db.models import EmailField

from slugify import slugify


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    email = EmailField(verbose_name='Email', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, separator='-')
            for x in itertools.count(1):
                if not Student.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f'{slugify(self.name)}-{x}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f"{self.name} ({self.age})"


class Subject(models.Model):

    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='студент')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'