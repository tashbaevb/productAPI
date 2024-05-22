from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='v1',
        description="Swagger",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('account/', include('account.urls')),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

