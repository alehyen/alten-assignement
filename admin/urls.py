from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from products.views import ProductViewset


router = routers.DefaultRouter()
router.register(r'products', ProductViewset, basename='products')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
