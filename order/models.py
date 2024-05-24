from django.db import models
from account.models import User


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    user_address = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name
