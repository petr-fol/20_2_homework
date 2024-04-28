from django.db import models
from slugify import slugify


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Изображение',
                              default='images/default.jpg')
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE, verbose_name='Категория',
                                 null=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, separator='-')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.price})"


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


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
    author = models.ForeignKey('catalog.Student', on_delete=models.CASCADE, verbose_name='Автор', null=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.value_to_string(self), separator='-')
        super().save()

    def __str__(self):
        return self.title
