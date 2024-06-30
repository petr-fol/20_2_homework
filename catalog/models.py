from django.db import models
from slugify import slugify


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Изображение',
                              default='images/default.jpg')
    category = models.ForeignKey('catalog.ProductCategory', on_delete=models.CASCADE, verbose_name='Категория',
                                 null=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name='Владелец',
                              help_text='создатель товара', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

        permissions = [
            ("can_edit_category", "Can edit category"),
            ("can_edit_description", "Can edit description"),
            ("can_edit_is_published", "Can edit is_published"),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, separator='-')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.price})"


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class ProductVersion(models.Model):
    number_of_version = models.IntegerField(default=0, verbose_name='Номер версии')
    current_version = models.BooleanField(default=False, verbose_name='Текущая версия')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f"{self.number_of_version})"
