from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
