from django.urls import path
from . import views as v

urlpatterns = [
    path('create/', v.OrderCreateAPIView.as_view()),  # завершающий слэш
    path('all/', v.OrderListAPIView.as_view()),  # завершающий слэш
    path('<int:pk>/', v.OrderDetailAPIView.as_view())
]
