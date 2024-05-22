from rest_framework import generics, permissions, status, response as res

from . import models as m, serializers as s


class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = m.Product.objects.all()
    serializer_class = s.ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = m.Product.objects.all()
    serializer_class = s.ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Product.objects.all()
    serializer_class = s.ProductSerializer
