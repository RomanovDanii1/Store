from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ProductViewSet


# Создайте объект DefaultRouter
router = DefaultRouter()

# Зарегистрируйте ваш ProductViewSet под именем 'product'
router.register(r'product', ProductViewSet)

# Определите URL-маршруты
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
]
