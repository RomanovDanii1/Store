from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ProductViewSet



router = DefaultRouter()


router.register(r'product', ProductViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
]
