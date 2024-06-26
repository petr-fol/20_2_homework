from django.db import models


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

