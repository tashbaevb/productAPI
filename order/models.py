from django.db import models

from product.models import Product


class Order(models.Model):
    user_address = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    counter = models.IntegerField()

    def __str__(self):
        return self.user_name
