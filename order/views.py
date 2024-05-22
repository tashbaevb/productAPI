from rest_framework import generics, permissions
from . import models as m, serializers as s


class OrderListAPIView(generics.ListAPIView):
    queryset = m.Order.objects.all()
    serializer_class = s.OrderSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = m.Order.objects.all()
    serializer_class = s.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Order.objects.all()
    serializer_class = s.OrderSerializer
