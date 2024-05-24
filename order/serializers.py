from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_address', 'user_name', 'owner']
        read_only_fields = ['owner']
