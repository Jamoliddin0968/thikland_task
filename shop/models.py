
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['title',]),
        ]
