from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Изображение', default='images/default.jpg')
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE, verbose_name='Категория', null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

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


