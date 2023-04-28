from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="rest_framework yozilgan Onlin dokin  API",
      default_version='v1',
      description="Onlin dockon uchun tayorlangan API",
      contact=openapi.Contact("Abdullayev Omonjon <figmafigma63@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosi/',include('assosy_app.urls')),
    path('user/',include('user_app.urls')),
    path('Docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('buyurtma/',include('buyurtma_app.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
