from rest_framework import serializers

from product.serializers import ProductSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='product.title', read_only=True)
    description = serializers.CharField(source='product.description', read_only=True)
    price = serializers.FloatField(source='product.price', read_only=True)
    image = serializers.ImageField(source='product.image', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user_address', 'user_name', 'counter', 'title', 'description', 'price', 'image']


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_address', 'user_name', 'product', 'counter']


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user_address', 'user_name', 'product', 'counter']
