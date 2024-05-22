from django.db import models

from account.models import User


from django.db import models
from account.models import User

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name
