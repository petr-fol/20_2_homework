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


class Version(models.Model):
    number_of_version = models.IntegerField(default=0, verbose_name='Номер версии')
    current_version = models.BooleanField(default=False, verbose_name='Текущая версия')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f"{self.number_of_version})"
