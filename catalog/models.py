from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.name} ({self.price})"
